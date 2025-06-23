#!/usr/bin/env python3
"""
Dependency Matrix System for Agent Communication
Works with Prolog-style rules to model complex communication dependencies
"""

import numpy as np
import networkx as nx
from typing import Dict, List, Set, Tuple, Any, Optional
from dataclasses import dataclass
from enum import Enum
import matplotlib.pyplot as plt
from rule_based_agent_config import RuleBasedConfigSystem, AgentFact, ProjectFact

class DependencyType(Enum):
    INFORMATIONAL = "informational"     # A needs to know what B is doing
    BLOCKING = "blocking"               # A cannot proceed without B
    COLLABORATIVE = "collaborative"     # A and B work together
    SUPERVISORY = "supervisory"         # A oversees B
    SUPPORTIVE = "supportive"          # A provides help to B
    SEQUENTIAL = "sequential"          # A → B → C workflow
    PARALLEL = "parallel"              # A and B work independently

@dataclass
class Dependency:
    """Represents a dependency between two agents"""
    from_agent: str
    to_agent: str
    dependency_type: DependencyType
    strength: float  # 0.0 to 1.0
    bidirectional: bool = False
    condition: str = None  # When this dependency applies

class DependencyMatrixSystem:
    """System for managing communication dependencies with multiple matrix representations"""
    
    def __init__(self, rule_system: RuleBasedConfigSystem):
        self.rule_system = rule_system
        self.agents = [agent.agent_id for agent in rule_system.agents]
        self.n_agents = len(self.agents)
        self.agent_to_index = {agent: i for i, agent in enumerate(self.agents)}
        
        # Dependency storage
        self.dependencies: List[Dependency] = []
        
        # Matrix representations
        self.adjacency_matrix = None          # Direct dependencies
        self.reachability_matrix = None       # All paths (transitive closure)
        self.strength_matrix = None           # Weighted by dependency strength
        self.type_matrices = {}               # Separate matrix per dependency type
        self.communication_matrix = None      # Final communication requirements
        
        # Graph representation
        self.dependency_graph = None
        
    def add_dependency(self, from_agent: str, to_agent: str, dep_type: DependencyType, 
                      strength: float = 1.0, bidirectional: bool = False, condition: str = None):
        """Add a dependency between agents"""
        
        if from_agent not in self.agents or to_agent not in self.agents:
            raise ValueError(f"Agents must be in system: {from_agent}, {to_agent}")
        
        dependency = Dependency(
            from_agent=from_agent,
            to_agent=to_agent,
            dependency_type=dep_type,
            strength=strength,
            bidirectional=bidirectional,
            condition=condition
        )
        
        self.dependencies.append(dependency)
        
        if bidirectional:
            reverse_dep = Dependency(
                from_agent=to_agent,
                to_agent=from_agent,
                dependency_type=dep_type,
                strength=strength,
                bidirectional=False,  # Avoid infinite recursion
                condition=condition
            )
            self.dependencies.append(reverse_dep)
    
    def generate_dependencies_from_rules(self):
        """Generate dependencies based on project context and agent roles"""
        
        print("GENERATING DEPENDENCIES FROM CONTEXT")
        print("=" * 40)
        
        # Get project context
        project = self.rule_system.project
        agents = self.rule_system.agents
        
        # Apply dependency generation rules
        self._apply_role_based_dependencies(agents)
        self._apply_phase_based_dependencies(project, agents)
        self._apply_hierarchy_dependencies(agents)
        self._apply_expertise_dependencies(agents)
        self._apply_topology_dependencies()
        
    def _apply_role_based_dependencies(self, agents: List[AgentFact]):
        """Generate dependencies based on agent roles"""
        
        print("\nApplying ROLE-BASED dependencies...")
        
        # Find agents by role
        role_map = {}
        for agent in agents:
            role = agent.role
            if role not in role_map:
                role_map[role] = []
            role_map[role].append(agent.agent_id)
        
        # Rule: Tech leads have supervisory dependency on developers
        if 'tech_lead' in role_map:
            for tech_lead in role_map['tech_lead']:
                for role in ['frontend_developer', 'backend_developer', 'developer']:
                    if role in role_map:
                        for dev in role_map[role]:
                            self.add_dependency(tech_lead, dev, DependencyType.SUPERVISORY, 0.8)
                            self.add_dependency(dev, tech_lead, DependencyType.INFORMATIONAL, 0.7)
                            print(f"  ✓ {tech_lead} supervises {dev}")
        
        # Rule: Designers have collaborative dependency with frontend developers
        if 'designer' in role_map and 'frontend_developer' in role_map:
            for designer in role_map['designer']:
                for frontend in role_map['frontend_developer']:
                    self.add_dependency(designer, frontend, DependencyType.COLLABORATIVE, 0.9, bidirectional=True)
                    print(f"  ✓ {designer} collaborates with {frontend}")
        
        # Rule: QA engineers have blocking dependency on developers
        for qa_role in ['qa_engineer', 'qa_manager']:
            if qa_role in role_map:
                for qa in role_map[qa_role]:
                    for dev_role in ['frontend_developer', 'backend_developer']:
                        if dev_role in role_map:
                            for dev in role_map[dev_role]:
                                self.add_dependency(qa, dev, DependencyType.BLOCKING, 0.8)
                                print(f"  ✓ {qa} blocked by {dev}")
        
        # Rule: DevOps has supportive dependency (others depend on DevOps)
        for devops_role in ['devops', 'devops_engineer']:
            if devops_role in role_map:
                for devops in role_map[devops_role]:
                    for agent in agents:
                        if agent.agent_id != devops and 'developer' in agent.role:
                            self.add_dependency(agent.agent_id, devops, DependencyType.SUPPORTIVE, 0.6)
                            print(f"  ✓ {agent.agent_id} supported by {devops}")
    
    def _apply_phase_based_dependencies(self, project: ProjectFact, agents: List[AgentFact]):
        """Generate dependencies based on project phase"""
        
        print(f"\nApplying {project.phase.upper()} PHASE dependencies...")
        
        if project.phase == "development":
            # Sequential: Backend → Frontend → QA
            backend_devs = [a.agent_id for a in agents if 'backend' in a.role]
            frontend_devs = [a.agent_id for a in agents if 'frontend' in a.role]
            qa_agents = [a.agent_id for a in agents if 'qa' in a.role]
            
            # Backend must complete before frontend
            for backend in backend_devs:
                for frontend in frontend_devs:
                    self.add_dependency(frontend, backend, DependencyType.SEQUENTIAL, 0.9)
                    print(f"  ✓ {frontend} sequentially depends on {backend}")
            
            # QA depends on both backend and frontend
            for qa in qa_agents:
                for dev in backend_devs + frontend_devs:
                    self.add_dependency(qa, dev, DependencyType.BLOCKING, 0.8)
                    print(f"  ✓ {qa} blocked by {dev}")
        
        elif project.phase == "testing":
            # QA agents become central, developers support them
            qa_agents = [a.agent_id for a in agents if 'qa' in a.role]
            dev_agents = [a.agent_id for a in agents if 'developer' in a.role]
            
            for qa in qa_agents:
                for dev in dev_agents:
                    self.add_dependency(qa, dev, DependencyType.INFORMATIONAL, 0.7)
                    self.add_dependency(dev, qa, DependencyType.SUPPORTIVE, 0.6)
                    print(f"  ✓ Testing phase: {qa} ↔ {dev} coordination")
        
        elif project.phase == "deployment":
            # Everyone depends on DevOps
            devops_agents = [a.agent_id for a in agents if 'devops' in a.role]
            other_agents = [a.agent_id for a in agents if 'devops' not in a.role]
            
            for devops in devops_agents:
                for other in other_agents:
                    self.add_dependency(other, devops, DependencyType.BLOCKING, 0.9)
                    print(f"  ✓ Deployment: {other} blocked by {devops}")
    
    def _apply_hierarchy_dependencies(self, agents: List[AgentFact]):
        """Generate dependencies based on organizational hierarchy"""
        
        print("\nApplying HIERARCHY dependencies...")
        
        # Group by activity level (proxy for seniority)
        senior_agents = [a.agent_id for a in agents if a.activity_level == "high"]
        junior_agents = [a.agent_id for a in agents if a.activity_level == "low"]
        
        # Senior agents have informational dependency on junior agents
        for senior in senior_agents:
            for junior in junior_agents:
                self.add_dependency(senior, junior, DependencyType.INFORMATIONAL, 0.5)
                self.add_dependency(junior, senior, DependencyType.SUPERVISORY, 0.6)
                print(f"  ✓ Hierarchy: {senior} ↔ {junior}")
    
    def _apply_expertise_dependencies(self, agents: List[AgentFact]):
        """Generate dependencies based on domain expertise"""
        
        print("\nApplying EXPERTISE dependencies...")
        
        # Find expertise overlaps
        for i, agent1 in enumerate(agents):
            for j, agent2 in enumerate(agents):
                if i != j:
                    # If agents share expertise, they collaborate
                    shared_expertise = agent1.expertise.intersection(agent2.expertise)
                    if shared_expertise:
                        strength = len(shared_expertise) / max(len(agent1.expertise), len(agent2.expertise))
                        self.add_dependency(agent1.agent_id, agent2.agent_id, 
                                          DependencyType.COLLABORATIVE, strength * 0.7)
                        print(f"  ✓ {agent1.agent_id} ↔ {agent2.agent_id} (shared: {shared_expertise})")
    
    def _apply_topology_dependencies(self):
        """Apply dependencies based on chosen topology"""
        
        config = self.rule_system.derived_config
        topology = config.get('topology', 'mesh')
        
        print(f"\nApplying {topology.upper()} TOPOLOGY dependencies...")
        
        if topology == "star":
            center = config.get('star_center', self.agents[0])
            center_idx = self.agent_to_index[center]
            
            # All agents have informational dependency on center
            for agent in self.agents:
                if agent != center:
                    self.add_dependency(agent, center, DependencyType.INFORMATIONAL, 0.8)
                    self.add_dependency(center, agent, DependencyType.SUPERVISORY, 0.7)
                    print(f"  ✓ Star: {agent} ↔ {center}")
        
        elif topology == "linear":
            # Sequential dependencies
            for i in range(len(self.agents) - 1):
                agent1 = self.agents[i]
                agent2 = self.agents[i + 1]
                self.add_dependency(agent2, agent1, DependencyType.SEQUENTIAL, 0.9)
                print(f"  ✓ Linear: {agent2} → {agent1}")
        
        elif topology == "hierarchical":
            # Apply hierarchical dependencies (already done in hierarchy section)
            print("  ✓ Hierarchical dependencies applied via hierarchy rules")
    
    def build_matrices(self):
        """Build all matrix representations"""
        
        print(f"\nBUILDING DEPENDENCY MATRICES")
        print("=" * 32)
        
        # Initialize matrices
        self.adjacency_matrix = np.zeros((self.n_agents, self.n_agents))
        self.strength_matrix = np.zeros((self.n_agents, self.n_agents))
        
        # Initialize type-specific matrices
        for dep_type in DependencyType:
            self.type_matrices[dep_type] = np.zeros((self.n_agents, self.n_agents))
        
        # Populate matrices from dependencies
        for dep in self.dependencies:
            from_idx = self.agent_to_index[dep.from_agent]
            to_idx = self.agent_to_index[dep.to_agent]
            
            # Adjacency matrix (binary)
            self.adjacency_matrix[from_idx][to_idx] = 1
            
            # Strength matrix (weighted)
            self.strength_matrix[from_idx][to_idx] = max(
                self.strength_matrix[from_idx][to_idx], dep.strength
            )
            
            # Type-specific matrix
            self.type_matrices[dep.dependency_type][from_idx][to_idx] = dep.strength
        
        # Build reachability matrix (transitive closure)
        self._build_reachability_matrix()
        
        # Build communication requirements matrix
        self._build_communication_matrix()
        
        print(f"✓ Built adjacency matrix ({self.n_agents}×{self.n_agents})")
        print(f"✓ Built reachability matrix (transitive closure)")
        print(f"✓ Built strength matrix (weighted dependencies)")
        print(f"✓ Built {len(DependencyType)} type-specific matrices")
        print(f"✓ Built communication requirements matrix")
    
    def _build_reachability_matrix(self):
        """Build transitive closure matrix (all possible paths)"""
        
        # Use Floyd-Warshall algorithm for transitive closure
        self.reachability_matrix = self.adjacency_matrix.copy()
        
        for k in range(self.n_agents):
            for i in range(self.n_agents):
                for j in range(self.n_agents):
                    self.reachability_matrix[i][j] = (
                        self.reachability_matrix[i][j] or 
                        (self.reachability_matrix[i][k] and self.reachability_matrix[k][j])
                    )
    
    def _build_communication_matrix(self):
        """Build final communication requirements matrix"""
        
        # Combine different dependency types with weights
        type_weights = {
            DependencyType.BLOCKING: 1.0,        # Highest priority
            DependencyType.SUPERVISORY: 0.9,     # Management needs
            DependencyType.COLLABORATIVE: 0.8,   # Team coordination
            DependencyType.SEQUENTIAL: 0.7,      # Workflow dependencies
            DependencyType.INFORMATIONAL: 0.6,   # Awareness needs
            DependencyType.SUPPORTIVE: 0.5,      # Help relationships
            DependencyType.PARALLEL: 0.3         # Independent work
        }
        
        self.communication_matrix = np.zeros((self.n_agents, self.n_agents))
        
        for dep_type, weight in type_weights.items():
            self.communication_matrix += self.type_matrices[dep_type] * weight
        
        # Normalize to 0-1 range
        max_val = np.max(self.communication_matrix)
        if max_val > 0:
            self.communication_matrix /= max_val
    
    def build_dependency_graph(self):
        """Build NetworkX graph representation"""
        
        print("\nBUILDING DEPENDENCY GRAPH")
        print("=" * 25)
        
        self.dependency_graph = nx.DiGraph()
        
        # Add nodes
        for agent in self.agents:
            self.dependency_graph.add_node(agent)
        
        # Add edges with attributes
        for dep in self.dependencies:
            self.dependency_graph.add_edge(
                dep.from_agent, 
                dep.to_agent,
                dependency_type=dep.dependency_type.value,
                strength=dep.strength,
                bidirectional=dep.bidirectional
            )
        
        print(f"✓ Graph: {len(self.dependency_graph.nodes)} nodes, {len(self.dependency_graph.edges)} edges")
        
        # Calculate graph metrics
        metrics = self._calculate_graph_metrics()
        return metrics
    
    def _calculate_graph_metrics(self) -> Dict[str, Any]:
        """Calculate important graph metrics"""
        
        metrics = {}
        
        # Basic metrics
        metrics['nodes'] = len(self.dependency_graph.nodes)
        metrics['edges'] = len(self.dependency_graph.edges)
        metrics['density'] = nx.density(self.dependency_graph)
        
        # Centrality measures
        metrics['in_degree_centrality'] = nx.in_degree_centrality(self.dependency_graph)
        metrics['out_degree_centrality'] = nx.out_degree_centrality(self.dependency_graph)
        metrics['betweenness_centrality'] = nx.betweenness_centrality(self.dependency_graph)
        
        # Most central agents
        in_central = max(metrics['in_degree_centrality'], key=metrics['in_degree_centrality'].get)
        out_central = max(metrics['out_degree_centrality'], key=metrics['out_degree_centrality'].get)
        between_central = max(metrics['betweenness_centrality'], key=metrics['betweenness_centrality'].get)
        
        metrics['most_depended_on'] = in_central  # Highest in-degree
        metrics['most_dependent'] = out_central   # Highest out-degree  
        metrics['most_central'] = between_central # Highest betweenness
        
        return metrics
    
    def analyze_communication_patterns(self) -> Dict[str, Any]:
        """Analyze communication patterns from matrices"""
        
        analysis = {}
        
        # Critical dependencies (blocking)
        blocking_matrix = self.type_matrices[DependencyType.BLOCKING]
        critical_deps = []
        for i in range(self.n_agents):
            for j in range(self.n_agents):
                if blocking_matrix[i][j] > 0.7:  # High strength blocking
                    critical_deps.append((self.agents[i], self.agents[j], blocking_matrix[i][j]))
        analysis['critical_dependencies'] = critical_deps
        
        # Communication hubs (high total communication requirements)
        comm_totals = np.sum(self.communication_matrix, axis=1) + np.sum(self.communication_matrix, axis=0)
        hub_idx = np.argmax(comm_totals)
        analysis['communication_hub'] = self.agents[hub_idx]
        analysis['hub_score'] = comm_totals[hub_idx]
        
        # Isolated agents (low communication requirements)
        isolated_agents = []
        for i, total in enumerate(comm_totals):
            if total < 0.5:  # Low communication
                isolated_agents.append(self.agents[i])
        analysis['isolated_agents'] = isolated_agents
        
        # Bottlenecks (agents many others depend on)
        in_degrees = np.sum(self.adjacency_matrix, axis=0)
        bottleneck_threshold = np.mean(in_degrees) + np.std(in_degrees)
        bottlenecks = []
        for i, in_degree in enumerate(in_degrees):
            if in_degree > bottleneck_threshold:
                bottlenecks.append((self.agents[i], int(in_degree)))
        analysis['bottlenecks'] = bottlenecks
        
        return analysis
    
    def generate_polling_recommendations(self) -> Dict[str, float]:
        """Generate agent-specific polling recommendations based on dependencies"""
        
        recommendations = {}
        
        for i, agent in enumerate(self.agents):
            # Base polling from rule system
            base_normal = self.rule_system.derived_config.get('normal_poll_interval', 5.0)
            base_urgent = self.rule_system.derived_config.get('urgent_poll_interval', 1.0)
            
            # Adjust based on communication requirements
            comm_score = np.sum(self.communication_matrix[i]) + np.sum(self.communication_matrix[:, i])
            
            # Higher communication needs = faster polling
            if comm_score > 0.8:
                factor = 0.5  # 2x faster
            elif comm_score > 0.5:
                factor = 0.7  # 1.4x faster
            else:
                factor = 1.0  # Normal speed
            
            recommendations[agent] = {
                'normal_interval': base_normal * factor,
                'urgent_interval': base_urgent * factor,
                'communication_score': comm_score,
                'reasoning': f"Communication score: {comm_score:.2f}"
            }
        
        return recommendations
    
    def print_matrices(self):
        """Print all matrices in readable format"""
        
        print(f"\nDEPENDENCY MATRICES")
        print("=" * 20)
        
        # Helper function to print matrix
        def print_matrix(matrix, title):
            print(f"\n{title}:")
            print("    ", end="")
            for agent in self.agents:
                print(f"{agent[:6]:>8}", end="")
            print()
            
            for i, from_agent in enumerate(self.agents):
                print(f"{from_agent[:6]:>6}", end=" ")
                for j, to_agent in enumerate(self.agents):
                    value = matrix[i][j]
                    if isinstance(value, bool):
                        print(f"{'T' if value else 'F':>8}", end="")
                    else:
                        print(f"{value:.2f}:>8", end="")
                print()
        
        # Print key matrices
        print_matrix(self.adjacency_matrix, "ADJACENCY MATRIX (Direct Dependencies)")
        print_matrix(self.reachability_matrix, "REACHABILITY MATRIX (All Paths)")
        print_matrix(self.communication_matrix, "COMMUNICATION MATRIX (Final Requirements)")
        
        # Print type-specific matrices for important types
        important_types = [DependencyType.BLOCKING, DependencyType.COLLABORATIVE, DependencyType.SUPERVISORY]
        for dep_type in important_types:
            print_matrix(self.type_matrices[dep_type], f"{dep_type.value.upper()} DEPENDENCIES")

def demonstrate_dependency_system():
    """Demonstrate the complete dependency matrix system"""
    
    # Create base rule system
    rule_system = RuleBasedConfigSystem()
    
    # Add agents for a software development team
    rule_system.add_agent("tech_lead", "tech_lead", "high", {"leadership", "architecture", "development"})
    rule_system.add_agent("backend_dev", "backend_developer", "high", {"api", "database", "python"})
    rule_system.add_agent("frontend_dev", "frontend_developer", "high", {"react", "typescript", "ui"})
    rule_system.add_agent("designer", "designer", "medium", {"ui", "ux", "design"})
    rule_system.add_agent("qa_engineer", "qa_engineer", "medium", {"testing", "automation", "quality"})
    rule_system.add_agent("devops", "devops_engineer", "low", {"deployment", "infrastructure", "monitoring"})
    
    # Set project context
    rule_system.set_project_context("startup", "development", "critical", 6, "distributed")
    
    # Generate base configuration
    config = rule_system.generate_configuration()
    
    # Create dependency system
    dep_system = DependencyMatrixSystem(rule_system)
    
    # Generate dependencies and build matrices
    dep_system.generate_dependencies_from_rules()
    dep_system.build_matrices()
    graph_metrics = dep_system.build_dependency_graph()
    
    # Analyze patterns
    patterns = dep_system.analyze_communication_patterns()
    polling_recs = dep_system.generate_polling_recommendations()
    
    # Print results
    dep_system.print_matrices()
    
    print(f"\n\nGRAPH METRICS")
    print("=" * 15)
    print(f"Nodes: {graph_metrics['nodes']}, Edges: {graph_metrics['edges']}")
    print(f"Density: {graph_metrics['density']:.3f}")
    print(f"Most depended on: {graph_metrics['most_depended_on']}")
    print(f"Most dependent: {graph_metrics['most_dependent']}")
    print(f"Most central: {graph_metrics['most_central']}")
    
    print(f"\nCOMMUNICATION ANALYSIS")
    print("=" * 22)
    print(f"Communication hub: {patterns['communication_hub']} (score: {patterns['hub_score']:.2f})")
    print(f"Critical dependencies: {len(patterns['critical_dependencies'])}")
    for dep in patterns['critical_dependencies'][:3]:  # Show top 3
        print(f"  • {dep[0]} → {dep[1]} (strength: {dep[2]:.2f})")
    print(f"Bottlenecks: {patterns['bottlenecks']}")
    print(f"Isolated agents: {patterns['isolated_agents']}")
    
    print(f"\nPOLLING RECOMMENDATIONS")
    print("=" * 23)
    for agent, rec in polling_recs.items():
        print(f"{agent}: {rec['normal_interval']:.1f}s/{rec['urgent_interval']:.1f}s "
              f"(comm score: {rec['communication_score']:.2f})")

if __name__ == "__main__":
    demonstrate_dependency_system()
    
    print(f"\n\nDEPENDENCY MATRIX SYSTEM FEATURES")
    print("=" * 37)
    print("✓ Adjacency Matrix - Direct dependencies")
    print("✓ Reachability Matrix - All possible paths (transitive closure)")
    print("✓ Strength Matrix - Weighted by dependency strength") 
    print("✓ Type-specific Matrices - Per dependency type")
    print("✓ Communication Matrix - Final requirements synthesis")
    print("✓ NetworkX Graph - Advanced graph analysis")
    print("✓ Centrality Analysis - Key agents identification")
    print("✓ Bottleneck Detection - Communication chokepoints")
    print("✓ Polling Optimization - Dependency-based frequencies")
    print("✓ Pattern Analysis - Communication insights")