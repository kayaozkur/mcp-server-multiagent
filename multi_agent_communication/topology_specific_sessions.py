#!/usr/bin/env python3
"""
Topology-Specific Session Management
Shows how different communication patterns require different session setups
"""

from typing import Dict, List, Set, Tuple
from dataclasses import dataclass

@dataclass
class TopologyConfig:
    """Configuration for a specific communication topology"""
    name: str
    description: str
    sessions_needed: List[str]
    capture_patterns: Dict[str, List[str]]  # agent -> sessions they monitor
    communication_rules: List[str]
    efficiency_rating: str

class TopologySessionManager:
    """Manages sessions based on communication topology"""
    
    def __init__(self, num_agents: int):
        self.num_agents = num_agents
        self.agents = [f"agent{i}" for i in range(1, num_agents + 1)]
    
    def linear_topology(self) -> TopologyConfig:
        """Linear chain: A1 -> A2 -> A3 -> A4"""
        sessions = []
        capture_patterns = {}
        
        # Only adjacent agents need to communicate
        for i in range(self.num_agents):
            agent = self.agents[i]
            sessions.extend([f"{agent}_inbox", f"{agent}_outbox"])
            
            # Each agent only monitors their own inbox
            capture_patterns[agent] = [f"{agent}_inbox"]
        
        return TopologyConfig(
            name="Linear Chain",
            description="Sequential communication: A1 -> A2 -> A3 -> A4",
            sessions_needed=sessions,
            capture_patterns=capture_patterns,
            communication_rules=[
                "Agent N communicates only with Agent N+1",
                "Unidirectional flow",
                "No loops or cycles"
            ],
            efficiency_rating="HIGH - Minimal sessions needed"
        )
    
    def ring_topology(self) -> TopologyConfig:
        """Ring: A1 -> A2 -> A3 -> A4 -> A1"""
        sessions = []
        capture_patterns = {}
        
        for i in range(self.num_agents):
            agent = self.agents[i]
            sessions.extend([f"{agent}_inbox", f"{agent}_outbox"])
            capture_patterns[agent] = [f"{agent}_inbox"]
        
        return TopologyConfig(
            name="Ring Topology",
            description="Circular communication: A1 -> A2 -> A3 -> A4 -> A1",
            sessions_needed=sessions,
            capture_patterns=capture_patterns,
            communication_rules=[
                "Each agent sends to next agent in ring",
                "Last agent sends back to first",
                "Messages travel in one direction around ring"
            ],
            efficiency_rating="HIGH - Same as linear, different flow"
        )
    
    def star_topology(self, center_agent: str = "agent1") -> TopologyConfig:
        """Star: Center agent broadcasts to all others"""
        sessions = []
        capture_patterns = {}
        
        for agent in self.agents:
            sessions.extend([f"{agent}_inbox", f"{agent}_outbox"])
            capture_patterns[agent] = [f"{agent}_inbox"]
        
        # Center agent is the only one that needs to send to multiple agents
        # Others only respond to center
        
        return TopologyConfig(
            name="Star Topology",
            description=f"Hub-and-spoke: {center_agent} broadcasts to all others",
            sessions_needed=sessions,  
            capture_patterns=capture_patterns,
            communication_rules=[
                f"{center_agent} sends to all other agents",
                "Other agents only respond to center",
                "No peer-to-peer communication"
            ],
            efficiency_rating="MEDIUM - Centralized but efficient"
        )
    
    def mesh_topology(self) -> TopologyConfig:
        """Full mesh: Every agent talks to every other agent"""
        sessions = []
        capture_patterns = {}
        
        for agent in self.agents:
            sessions.extend([f"{agent}_inbox", f"{agent}_outbox"])
            # In mesh, each agent must monitor their own inbox for messages from ALL others
            capture_patterns[agent] = [f"{agent}_inbox"]
        
        return TopologyConfig(
            name="Full Mesh",
            description="Every agent communicates with every other agent",
            sessions_needed=sessions,
            capture_patterns=capture_patterns,
            communication_rules=[
                "N*(N-1) possible communication channels",
                "Each agent can send to any other agent",
                "Highly redundant and fault-tolerant"
            ],
            efficiency_rating="LOW - Maximum sessions, maximum flexibility"
        )
    
    def hierarchical_topology(self) -> TopologyConfig:
        """Hierarchical: Leader -> Lieutenants -> Workers"""
        sessions = []
        capture_patterns = {}
        
        # Assign roles
        leader = self.agents[0] if self.agents else None
        lieutenants = self.agents[1:3] if len(self.agents) > 2 else self.agents[1:2] if len(self.agents) > 1 else []
        workers = self.agents[3:] if len(self.agents) > 3 else []
        
        # All agents still need sessions
        for agent in self.agents:
            sessions.extend([f"{agent}_inbox", f"{agent}_outbox"])
            capture_patterns[agent] = [f"{agent}_inbox"]
        
        roles = []
        if leader:
            roles.append(f"Leader: {leader}")
        if lieutenants:
            roles.append(f"Lieutenants: {', '.join(lieutenants)}")
        if workers:
            roles.append(f"Workers: {', '.join(workers)}")
        
        return TopologyConfig(
            name="Hierarchical",
            description="Command structure: Leader -> Lieutenants -> Workers",
            sessions_needed=sessions,
            capture_patterns=capture_patterns,
            communication_rules=[
                "Leader sends commands to Lieutenants",
                "Lieutenants distribute tasks to Workers", 
                "Workers report back up the chain",
                f"Roles: {'; '.join(roles)}"
            ],
            efficiency_rating="MEDIUM - Structured but limited paths"
        )
    
    def optimized_topology_for_use_case(self, use_case: str) -> TopologyConfig:
        """Choose optimal topology based on use case"""
        
        optimizations = {
            "broadcast": self.star_topology(),
            "pipeline": self.linear_topology(),
            "consensus": self.mesh_topology(),
            "command_control": self.hierarchical_topology(),
            "load_balancing": self.ring_topology()
        }
        
        return optimizations.get(use_case, self.mesh_topology())

def compare_session_requirements():
    """Compare session requirements across topologies"""
    
    print("SESSION REQUIREMENTS BY TOPOLOGY")
    print("=" * 50)
    
    num_agents = 4
    manager = TopologySessionManager(num_agents)
    
    topologies = [
        manager.linear_topology(),
        manager.ring_topology(),
        manager.star_topology(),
        manager.mesh_topology(),
        manager.hierarchical_topology()
    ]
    
    for topology in topologies:
        print(f"\n{topology.name.upper()}")
        print("-" * len(topology.name))
        print(f"Description: {topology.description}")
        print(f"Total Sessions: {len(topology.sessions_needed)}")
        print(f"Efficiency: {topology.efficiency_rating}")
        
        print(f"\nSessions Required:")
        for session in topology.sessions_needed:
            print(f"  • {session}")
        
        print(f"\nCapture Patterns:")
        for agent, sessions in topology.capture_patterns.items():
            print(f"  {agent} monitors: {', '.join(sessions)}")
        
        print(f"\nCommunication Rules:")
        for rule in topology.communication_rules:
            print(f"  • {rule}")

def show_capture_optimization():
    """Show how capture patterns can be optimized per topology"""
    
    print("\n\nCAPTURE PATTERN OPTIMIZATIONS")
    print("=" * 40)
    
    optimizations = [
        {
            "topology": "Linear Chain",
            "standard": "Each agent monitors own inbox (4 captures)",
            "optimized": "Each agent monitors own inbox (4 captures)",
            "savings": "None - already optimal"
        },
        {
            "topology": "Ring",
            "standard": "Each agent monitors own inbox (4 captures)",
            "optimized": "Each agent monitors own inbox (4 captures)", 
            "savings": "None - already optimal"
        },
        {
            "topology": "Star",
            "standard": "Each agent monitors own inbox (4 captures)",
            "optimized": "Center agent monitors own inbox, others monitor own inbox (4 captures)",
            "savings": "None - but center agent does more work"
        },
        {
            "topology": "Mesh",
            "standard": "Each agent monitors own inbox (4 captures)",
            "optimized": "Each agent monitors own inbox (4 captures)",
            "savings": "None - but handles N*(N-1) possible message sources"
        },
        {
            "topology": "Hierarchical", 
            "standard": "Each agent monitors own inbox (4 captures)",
            "optimized": "Leader monitors more frequently, workers less frequently",
            "savings": "Can adjust polling frequency by role"
        }
    ]
    
    for opt in optimizations:
        print(f"\n{opt['topology']}:")
        print(f"  Standard: {opt['standard']}")
        print(f"  Optimized: {opt['optimized']}")
        print(f"  Savings: {opt['savings']}")

def demonstrate_dynamic_topology_switching():
    """Show how to switch between topologies dynamically"""
    
    print("\n\nDYNAMIC TOPOLOGY SWITCHING")
    print("=" * 35)
    
    manager = TopologySessionManager(4)
    
    scenarios = [
        {
            "phase": "Initialization",
            "topology": manager.star_topology(),
            "reason": "Central coordinator distributes initial tasks"
        },
        {
            "phase": "Parallel Processing", 
            "topology": manager.linear_topology(),
            "reason": "Sequential processing pipeline"
        },
        {
            "phase": "Consensus Building",
            "topology": manager.mesh_topology(),
            "reason": "All agents need to agree on result"
        },
        {
            "phase": "Status Reporting",
            "topology": manager.hierarchical_topology(),
            "reason": "Structured reporting up the chain"
        }
    ]
    
    print("A complex workflow might use different topologies:")
    print()
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"Phase {i}: {scenario['phase']}")
        print(f"  Topology: {scenario['topology'].name}")
        print(f"  Reason: {scenario['reason']}")
        print(f"  Sessions: {len(scenario['topology'].sessions_needed)}")
        print()

if __name__ == "__main__":
    compare_session_requirements()
    show_capture_optimization()
    demonstrate_dynamic_topology_switching()
    
    print("\nKEY INSIGHTS:")
    print("=" * 15)
    print("• All topologies need same number of sessions (2 per agent)")
    print("• Difference is in WHO sends TO whom, not capture mechanism")
    print("• Each agent always monitors only their own inbox")
    print("• Topology affects message routing, not session requirements")
    print("• Optimization comes from message frequency and routing rules")