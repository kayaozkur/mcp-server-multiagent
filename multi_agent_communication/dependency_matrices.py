#!/usr/bin/env python3
"""
Dependency Matrix System for Agent Communication
Multiple matrix representations working with Prolog-style rules
"""

import numpy as np
from typing import Dict, List, Set, Tuple, Any, Optional
from dataclasses import dataclass
from enum import Enum

# Import our rule system
import sys
import os
sys.path.append(os.path.dirname(__file__))

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

@dataclass
class AgentFact:
    """Simplified agent fact for standalone demo"""
    agent_id: str
    role: str
    activity_level: str
    expertise: Set[str]
    team: str = None

@dataclass 
class ProjectFact:
    """Simplified project fact for standalone demo"""
    project_type: str
    phase: str
    urgency: str
    team_size: int
    distribution: str

class DependencyMatrixSystem:
    """Complete dependency matrix system"""
    
    def __init__(self, agents: List[str]):
        self.agents = agents
        self.n_agents = len(self.agents)
        self.agent_to_index = {agent: i for i, agent in enumerate(self.agents)}
        
        # Dependency storage
        self.dependencies: List[Dependency] = []
        
        # Matrix representations
        self.adjacency_matrix = None          # Direct dependencies (binary)
        self.reachability_matrix = None       # All paths (transitive closure)
        self.strength_matrix = None           # Weighted by dependency strength
        self.type_matrices = {}               # Separate matrix per dependency type
        self.communication_matrix = None      # Final communication requirements
        
        # Analysis results
        self.centrality_scores = {}
        self.communication_hubs = []
        self.bottlenecks = []
        
    def add_dependency(self, from_agent: str, to_agent: str, dep_type: DependencyType, 
                      strength: float = 1.0, bidirectional: bool = False):
        """Add a dependency between agents"""
        
        if from_agent not in self.agents or to_agent not in self.agents:
            raise ValueError(f"Agents must be in system: {from_agent}, {to_agent}")
        
        dependency = Dependency(
            from_agent=from_agent,
            to_agent=to_agent,
            dependency_type=dep_type,
            strength=strength,
            bidirectional=bidirectional
        )
        
        self.dependencies.append(dependency)
        print(f"Added dependency: {from_agent} → {to_agent} ({dep_type.value}, {strength:.2f})")
        
        if bidirectional:
            reverse_dep = Dependency(
                from_agent=to_agent,
                to_agent=from_agent,
                dependency_type=dep_type,
                strength=strength,
                bidirectional=False
            )
            self.dependencies.append(reverse_dep)
            print(f"Added reverse: {to_agent} → {from_agent} ({dep_type.value}, {strength:.2f})")
    
    def generate_dependencies_from_context(self, agents_data: List[AgentFact], project: ProjectFact):
        """Generate dependencies based on context"""
        
        print("GENERATING DEPENDENCIES FROM CONTEXT")
        print("=" * 40)
        
        self._apply_role_dependencies(agents_data)
        self._apply_phase_dependencies(project, agents_data)
        self._apply_expertise_dependencies(agents_data)
        self._apply_hierarchy_dependencies(agents_data)
    
    def _apply_role_dependencies(self, agents_data: List[AgentFact]):
        """Generate role-based dependencies"""
        
        print("\nROLE-BASED DEPENDENCIES:")
        print("-" * 25)
        
        # Create role mapping
        role_agents = {}
        for agent in agents_data:
            if agent.role not in role_agents:
                role_agents[agent.role] = []
            role_agents[agent.role].append(agent.agent_id)
        
        # Tech lead supervises developers
        if 'tech_lead' in role_agents:
            for tech_lead in role_agents['tech_lead']:
                for role in ['backend_developer', 'frontend_developer']:
                    if role in role_agents:
                        for dev in role_agents[role]:
                            self.add_dependency(tech_lead, dev, DependencyType.SUPERVISORY, 0.8)
                            self.add_dependency(dev, tech_lead, DependencyType.INFORMATIONAL, 0.7)
        
        # Designer collaborates with frontend
        if 'designer' in role_agents and 'frontend_developer' in role_agents:
            for designer in role_agents['designer']:
                for frontend in role_agents['frontend_developer']:
                    self.add_dependency(designer, frontend, DependencyType.COLLABORATIVE, 0.9, True)
        
        # QA blocks on developers
        if 'qa_engineer' in role_agents:
            for qa in role_agents['qa_engineer']:
                for role in ['backend_developer', 'frontend_developer']:
                    if role in role_agents:
                        for dev in role_agents[role]:
                            self.add_dependency(qa, dev, DependencyType.BLOCKING, 0.8)
        
        # DevOps supports everyone
        if 'devops_engineer' in role_agents:
            for devops in role_agents['devops_engineer']:
                for agent in agents_data:
                    if 'developer' in agent.role:
                        self.add_dependency(agent.agent_id, devops, DependencyType.SUPPORTIVE, 0.6)
    
    def _apply_phase_dependencies(self, project: ProjectFact, agents_data: List[AgentFact]):
        """Generate phase-specific dependencies"""
        
        print(f"\n{project.phase.upper()} PHASE DEPENDENCIES:")
        print("-" * 30)
        
        if project.phase == "development":
            # Sequential: Backend → Frontend
            backend_devs = [a.agent_id for a in agents_data if 'backend' in a.role]
            frontend_devs = [a.agent_id for a in agents_data if 'frontend' in a.role]
            
            for backend in backend_devs:
                for frontend in frontend_devs:
                    self.add_dependency(frontend, backend, DependencyType.SEQUENTIAL, 0.9)
        
        elif project.phase == "testing":
            # QA becomes central
            qa_agents = [a.agent_id for a in agents_data if 'qa' in a.role]
            dev_agents = [a.agent_id for a in agents_data if 'developer' in a.role]
            
            for qa in qa_agents:
                for dev in dev_agents:
                    self.add_dependency(qa, dev, DependencyType.INFORMATIONAL, 0.8)
    
    def _apply_expertise_dependencies(self, agents_data: List[AgentFact]):
        """Generate expertise-based dependencies"""
        
        print(f"\nEXPERTISE DEPENDENCIES:")
        print("-" * 22)
        
        for i, agent1 in enumerate(agents_data):
            for j, agent2 in enumerate(agents_data):
                if i != j:
                    shared = agent1.expertise.intersection(agent2.expertise)
                    if shared:
                        strength = len(shared) / max(len(agent1.expertise), len(agent2.expertise))
                        if strength > 0.3:  # Significant overlap
                            self.add_dependency(agent1.agent_id, agent2.agent_id, 
                                              DependencyType.COLLABORATIVE, strength * 0.6)
    
    def _apply_hierarchy_dependencies(self, agents_data: List[AgentFact]):
        """Generate hierarchy-based dependencies"""
        
        print(f"\nHIERARCHY DEPENDENCIES:")
        print("-" * 23)
        
        # Activity level as proxy for seniority
        high_activity = [a.agent_id for a in agents_data if a.activity_level == "high"]
        low_activity = [a.agent_id for a in agents_data if a.activity_level == "low"]
        
        for high in high_activity:
            for low in low_activity:
                self.add_dependency(high, low, DependencyType.INFORMATIONAL, 0.5)
                self.add_dependency(low, high, DependencyType.SUPERVISORY, 0.6)
    
    def build_matrices(self):
        """Build all matrix representations"""
        
        print(f"\nBUILDING MATRICES")
        print("=" * 17)
        
        # Initialize matrices
        self.adjacency_matrix = np.zeros((self.n_agents, self.n_agents), dtype=int)
        self.strength_matrix = np.zeros((self.n_agents, self.n_agents))
        
        # Initialize type-specific matrices
        for dep_type in DependencyType:
            self.type_matrices[dep_type] = np.zeros((self.n_agents, self.n_agents))
        
        # Populate matrices
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
        
        # Build derived matrices
        self._build_reachability_matrix()
        self._build_communication_matrix()
        
        print(f"✓ Adjacency Matrix: {self.n_agents}×{self.n_agents}")
        print(f"✓ Reachability Matrix (transitive closure)")
        print(f"✓ Strength Matrix (weighted)")
        print(f"✓ Type Matrices: {len(DependencyType)} types")
        print(f"✓ Communication Matrix (combined)")
    
    def _build_reachability_matrix(self):
        """Build transitive closure using Floyd-Warshall"""
        
        self.reachability_matrix = self.adjacency_matrix.copy().astype(bool)
        
        # Floyd-Warshall for transitive closure
        for k in range(self.n_agents):
            for i in range(self.n_agents):
                for j in range(self.n_agents):
                    self.reachability_matrix[i][j] = (
                        self.reachability_matrix[i][j] or 
                        (self.reachability_matrix[i][k] and self.reachability_matrix[k][j])
                    )
    
    def _build_communication_matrix(self):
        """Build final communication requirements matrix"""
        
        # Weight different dependency types
        type_weights = {
            DependencyType.BLOCKING: 1.0,        # Highest priority
            DependencyType.SUPERVISORY: 0.9,     
            DependencyType.COLLABORATIVE: 0.8,   
            DependencyType.SEQUENTIAL: 0.7,      
            DependencyType.INFORMATIONAL: 0.6,   
            DependencyType.SUPPORTIVE: 0.5,      
            DependencyType.PARALLEL: 0.3         
        }
        
        self.communication_matrix = np.zeros((self.n_agents, self.n_agents))
        
        for dep_type, weight in type_weights.items():
            self.communication_matrix += self.type_matrices[dep_type] * weight
        
        # Normalize to 0-1 range
        max_val = np.max(self.communication_matrix)
        if max_val > 0:
            self.communication_matrix /= max_val
    
    def analyze_network(self):
        """Analyze the dependency network"""
        
        print(f"\nNETWORK ANALYSIS")
        print("=" * 16)
        
        # Calculate centrality scores
        self._calculate_centrality()
        
        # Find communication hubs
        self._find_communication_hubs()
        
        # Identify bottlenecks
        self._identify_bottlenecks()
        
        # Critical path analysis
        self._analyze_critical_paths()
    
    def _calculate_centrality(self):
        """Calculate centrality scores for each agent"""
        
        self.centrality_scores = {}
        
        for i, agent in enumerate(self.agents):
            # In-degree centrality (how many depend on this agent)
            in_degree = np.sum(self.adjacency_matrix[:, i])
            
            # Out-degree centrality (how many this agent depends on)
            out_degree = np.sum(self.adjacency_matrix[i, :])
            
            # Communication centrality (total communication load)
            comm_in = np.sum(self.communication_matrix[:, i])
            comm_out = np.sum(self.communication_matrix[i, :])
            
            self.centrality_scores[agent] = {
                'in_degree': in_degree,
                'out_degree': out_degree,
                'total_degree': in_degree + out_degree,
                'comm_load': comm_in + comm_out
            }
        
        print("Centrality Scores:")
        for agent, scores in self.centrality_scores.items():
            print(f"  {agent}: in={scores['in_degree']}, out={scores['out_degree']}, "
                  f"comm={scores['comm_load']:.2f}")
    
    def _find_communication_hubs(self):
        """Identify agents with high communication requirements"""
        
        comm_scores = {agent: scores['comm_load'] 
                      for agent, scores in self.centrality_scores.items()}
        
        # Sort by communication load
        sorted_agents = sorted(comm_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Top 30% are hubs
        hub_count = max(1, len(sorted_agents) // 3)
        self.communication_hubs = sorted_agents[:hub_count]
        
        print(f"\nCommunication Hubs (top {hub_count}):")
        for agent, score in self.communication_hubs:
            print(f"  {agent}: {score:.2f}")
    
    def _identify_bottlenecks(self):
        """Identify potential bottlenecks"""
        
        # Agents with high in-degree (many depend on them)
        in_degrees = {agent: scores['in_degree'] 
                     for agent, scores in self.centrality_scores.items()}
        
        mean_in_degree = np.mean(list(in_degrees.values()))
        std_in_degree = np.std(list(in_degrees.values()))
        threshold = mean_in_degree + std_in_degree
        
        self.bottlenecks = [(agent, degree) for agent, degree in in_degrees.items() 
                           if degree > threshold]
        
        print(f"\nBottlenecks (in-degree > {threshold:.1f}):")
        for agent, degree in self.bottlenecks:
            print(f"  {agent}: {degree} dependencies")
    
    def _analyze_critical_paths(self):
        """Analyze critical paths in the network"""
        
        # Find longest paths using adjacency matrix
        critical_deps = []
        
        # Look for chains of blocking dependencies
        blocking_matrix = self.type_matrices[DependencyType.BLOCKING]
        for i in range(self.n_agents):
            for j in range(self.n_agents):
                if blocking_matrix[i][j] > 0.7:  # High-strength blocking
                    critical_deps.append((self.agents[i], self.agents[j], blocking_matrix[i][j]))
        
        print(f"\nCritical Dependencies (blocking > 0.7):")
        for from_agent, to_agent, strength in critical_deps:
            print(f"  {from_agent} blocks {to_agent} (strength: {strength:.2f})")
    
    def generate_polling_recommendations(self, base_interval: float = 5.0) -> Dict[str, Dict]:
        """Generate polling recommendations based on communication matrix"""
        
        recommendations = {}
        
        for i, agent in enumerate(self.agents):
            # Calculate communication intensity
            comm_intensity = (np.sum(self.communication_matrix[i, :]) + 
                            np.sum(self.communication_matrix[:, i]))
            
            # Adjust polling based on intensity
            if comm_intensity > 1.5:
                factor = 0.3  # Very fast
                reason = "High communication hub"
            elif comm_intensity > 1.0:
                factor = 0.5  # Fast
                reason = "Moderate communication load"
            elif comm_intensity > 0.5:
                factor = 0.7  # Slightly faster
                reason = "Some communication needs"
            else:
                factor = 1.0  # Normal
                reason = "Low communication needs"
            
            recommendations[agent] = {
                'normal_interval': base_interval * factor,
                'urgent_interval': base_interval * factor * 0.2,
                'communication_intensity': comm_intensity,
                'reasoning': reason
            }
        
        return recommendations
    
    def print_matrices(self):
        """Print all matrices in readable format"""
        
        print(f"\nDEPENDENCY MATRICES")
        print("=" * 19)
        
        def print_matrix(matrix, title, format_func=None):
            print(f"\n{title}:")
            
            # Header
            print("        ", end="")
            for agent in self.agents:
                print(f"{agent[:6]:>8}", end="")
            print()
            
            # Rows
            for i, from_agent in enumerate(self.agents):
                print(f"{from_agent[:6]:>6}  ", end="")
                for j in range(self.n_agents):
                    value = matrix[i][j]
                    if format_func:
                        formatted = format_func(value)
                    elif isinstance(value, (bool, np.bool_)):
                        formatted = "T" if value else "."
                    elif isinstance(value, (int, np.integer)):
                        formatted = str(int(value)) if value != 0 else "."
                    else:
                        formatted = f"{value:.2f}" if value > 0.01 else "."
                    print(f"{formatted:>8}", end="")
                print()
        
        # Print key matrices
        print_matrix(self.adjacency_matrix, "ADJACENCY MATRIX (Direct Dependencies)")
        print_matrix(self.reachability_matrix, "REACHABILITY MATRIX (All Paths)")
        print_matrix(self.communication_matrix, "COMMUNICATION MATRIX (Final Requirements)")
        
        # Print blocking dependencies specifically
        if DependencyType.BLOCKING in self.type_matrices:
            print_matrix(self.type_matrices[DependencyType.BLOCKING], "BLOCKING DEPENDENCIES")

def demonstrate_dependency_matrices():
    """Demonstrate the complete dependency matrix system"""
    
    print("DEPENDENCY MATRIX SYSTEM DEMONSTRATION")
    print("=" * 42)
    
    # Define agents
    agents = ["tech_lead", "backend_dev", "frontend_dev", "designer", "qa_engineer", "devops"]
    
    # Create agent data
    agents_data = [
        AgentFact("tech_lead", "tech_lead", "high", {"leadership", "architecture"}),
        AgentFact("backend_dev", "backend_developer", "high", {"api", "database", "python"}),
        AgentFact("frontend_dev", "frontend_developer", "high", {"react", "typescript", "ui"}),
        AgentFact("designer", "designer", "medium", {"ui", "ux", "design"}),
        AgentFact("qa_engineer", "qa_engineer", "medium", {"testing", "automation"}),
        AgentFact("devops", "devops_engineer", "low", {"deployment", "infrastructure"})
    ]
    
    # Create project context
    project = ProjectFact("startup", "development", "critical", 6, "distributed")
    
    # Create dependency system
    dep_system = DependencyMatrixSystem(agents)
    
    # Generate dependencies and build matrices
    dep_system.generate_dependencies_from_context(agents_data, project)
    dep_system.build_matrices()
    dep_system.analyze_network()
    
    # Generate polling recommendations
    polling_recs = dep_system.generate_polling_recommendations()
    
    # Print matrices
    dep_system.print_matrices()
    
    print(f"\nPOLLING RECOMMENDATIONS")
    print("=" * 23)
    for agent, rec in polling_recs.items():
        print(f"{agent}: {rec['normal_interval']:.1f}s/{rec['urgent_interval']:.1f}s "
              f"({rec['reasoning']})")

if __name__ == "__main__":
    demonstrate_dependency_matrices()
    
    print(f"\n\nMATRIX SYSTEM FEATURES")
    print("=" * 22)
    print("✓ Adjacency Matrix - Direct dependencies (binary)")
    print("✓ Reachability Matrix - All paths via transitive closure") 
    print("✓ Strength Matrix - Weighted dependency strengths")
    print("✓ Type Matrices - Separate matrix per dependency type")
    print("✓ Communication Matrix - Combined final requirements")
    print("✓ Centrality Analysis - Hub and bottleneck identification")
    print("✓ Critical Path Analysis - Blocking dependency chains")
    print("✓ Polling Optimization - Matrix-based recommendations")
    print("✓ Network Metrics - Comprehensive dependency analysis")