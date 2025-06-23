#!/usr/bin/env python3
"""
Hybrid Topology System
Shows how complex topologies are combinations of basic patterns
"""

from typing import Dict, List, Set, Tuple
from dataclasses import dataclass
from enum import Enum

class BasicTopology(Enum):
    LINEAR = "linear"
    MESH = "mesh" 
    STAR = "star"
    RING = "ring"

@dataclass
class TopologyLayer:
    """A layer in a hierarchical topology"""
    name: str
    agents: List[str]
    internal_topology: BasicTopology
    parent_layer: str = None
    child_layers: List[str] = None

class HybridTopologyBuilder:
    """Build complex topologies by combining basic patterns"""
    
    def __init__(self, all_agents: List[str]):
        self.all_agents = all_agents
        self.layers: Dict[str, TopologyLayer] = {}
        self.inter_layer_connections: List[Tuple[str, str, str]] = []  # (layer1, layer2, pattern)
    
    def hierarchical_sequential_mesh(self) -> Dict[str, any]:
        """Hierarchical = Sequential between layers + Mesh within layers"""
        
        if len(self.all_agents) < 6:
            # Simple 2-layer hierarchy
            return self._simple_hierarchical()
        
        # Complex multi-layer hierarchy
        leader_layer = TopologyLayer(
            name="leadership",
            agents=[self.all_agents[0]],  # Single leader
            internal_topology=BasicTopology.STAR  # Leader is center of star
        )
        
        lieutenant_layer = TopologyLayer(
            name="management", 
            agents=self.all_agents[1:4],  # 3 lieutenants
            internal_topology=BasicTopology.MESH,  # Lieutenants coordinate in mesh
            parent_layer="leadership"
        )
        
        worker_layer = TopologyLayer(
            name="workers",
            agents=self.all_agents[4:],  # Remaining agents are workers
            internal_topology=BasicTopology.LINEAR,  # Workers in pipeline
            parent_layer="management"
        )
        
        self.layers = {
            "leadership": leader_layer,
            "management": lieutenant_layer, 
            "workers": worker_layer
        }
        
        # Inter-layer connections are SEQUENTIAL (hierarchical)
        self.inter_layer_connections = [
            ("leadership", "management", "star_to_mesh"),  # Leader broadcasts to lieutenant mesh
            ("management", "workers", "mesh_to_linear")    # Lieutenants coordinate worker pipeline
        ]
        
        return {
            "topology_type": "Hierarchical (Sequential + Mesh)",
            "layers": self.layers,
            "inter_layer_patterns": self.inter_layer_connections,
            "description": "Leader -> Lieutenant Mesh -> Worker Pipeline"
        }
    
    def _simple_hierarchical(self) -> Dict[str, any]:
        """Simple hierarchy for smaller agent counts"""
        
        leader_layer = TopologyLayer(
            name="leadership",
            agents=[self.all_agents[0]],
            internal_topology=BasicTopology.STAR
        )
        
        subordinate_layer = TopologyLayer(
            name="subordinates",
            agents=self.all_agents[1:],
            internal_topology=BasicTopology.MESH,
            parent_layer="leadership"
        )
        
        self.layers = {
            "leadership": leader_layer,
            "subordinates": subordinate_layer
        }
        
        self.inter_layer_connections = [
            ("leadership", "subordinates", "star_to_mesh")
        ]
        
        return {
            "topology_type": "Simple Hierarchical (Star + Mesh)",
            "layers": self.layers,
            "inter_layer_patterns": self.inter_layer_connections,
            "description": "Leader broadcasts to subordinate mesh"
        }
    
    def matrix_organization(self) -> Dict[str, any]:
        """Matrix organization = Multiple overlapping hierarchies"""
        
        # Functional hierarchy (by role)
        functional_layers = {
            "executives": TopologyLayer("executives", [self.all_agents[0]], BasicTopology.STAR),
            "managers": TopologyLayer("managers", self.all_agents[1:3], BasicTopology.MESH),  
            "workers": TopologyLayer("workers", self.all_agents[3:], BasicTopology.LINEAR)
        }
        
        # Project hierarchy (by project)
        project_teams = {
            "project_leads": TopologyLayer("project_leads", [self.all_agents[1]], BasicTopology.STAR),
            "project_members": TopologyLayer("project_members", self.all_agents[2:], BasicTopology.MESH)
        }
        
        return {
            "topology_type": "Matrix Organization",
            "functional_hierarchy": functional_layers,
            "project_hierarchy": project_teams,
            "description": "Agents belong to multiple overlapping hierarchies"
        }
    
    def federated_mesh(self) -> Dict[str, any]:
        """Federated Mesh = Multiple mesh clusters with star-connected leaders"""
        
        # Divide agents into clusters
        cluster_size = max(2, len(self.all_agents) // 3)
        clusters = []
        
        for i in range(0, len(self.all_agents), cluster_size):
            cluster_agents = self.all_agents[i:i + cluster_size]
            if cluster_agents:
                clusters.append(TopologyLayer(
                    name=f"cluster_{i//cluster_size + 1}",
                    agents=cluster_agents,
                    internal_topology=BasicTopology.MESH
                ))
        
        # Leaders of each cluster form a star network
        cluster_leaders = [cluster.agents[0] for cluster in clusters]
        leader_network = TopologyLayer(
            name="cluster_leaders",
            agents=cluster_leaders,
            internal_topology=BasicTopology.STAR
        )
        
        return {
            "topology_type": "Federated Mesh",
            "clusters": clusters,
            "leader_network": leader_network,
            "description": "Mesh clusters connected via star leader network"
        }
    
    def pipeline_with_supervisors(self) -> Dict[str, any]:
        """Pipeline with Supervisors = Linear pipeline + Star supervision"""
        
        # Main pipeline
        pipeline_agents = self.all_agents[1:]  # All except first
        pipeline = TopologyLayer(
            name="pipeline",
            agents=pipeline_agents,
            internal_topology=BasicTopology.LINEAR
        )
        
        # Supervisor oversees pipeline
        supervisor = TopologyLayer(
            name="supervisor", 
            agents=[self.all_agents[0]],
            internal_topology=BasicTopology.STAR
        )
        
        return {
            "topology_type": "Supervised Pipeline",
            "pipeline": pipeline,
            "supervisor": supervisor,
            "pattern": "Star supervision over linear pipeline",
            "description": "Supervisor monitors/controls linear processing pipeline"
        }

def demonstrate_hybrid_topologies():
    """Demonstrate how complex topologies combine basic patterns"""
    
    print("HYBRID TOPOLOGY COMBINATIONS")
    print("=" * 35)
    
    agents = [f"agent{i}" for i in range(1, 9)]  # 8 agents for complex examples
    builder = HybridTopologyBuilder(agents)
    
    print(f"Working with {len(agents)} agents: {', '.join(agents)}")
    print()
    
    # 1. Hierarchical = Sequential + Mesh
    print("1. HIERARCHICAL TOPOLOGY")
    print("-" * 25)
    hierarchical = builder.hierarchical_sequential_mesh()
    
    print(f"Type: {hierarchical['topology_type']}")
    print(f"Description: {hierarchical['description']}")
    print("\nLayers:")
    for layer_name, layer in hierarchical['layers'].items():
        print(f"  {layer_name.upper()}:")
        print(f"    Agents: {', '.join(layer.agents)}")
        print(f"    Internal Pattern: {layer.internal_topology.value}")
        if layer.parent_layer:
            print(f"    Reports to: {layer.parent_layer}")
    
    print("\nInter-layer Connections:")
    for conn in hierarchical['inter_layer_patterns']:
        print(f"  {conn[0]} -> {conn[1]}: {conn[2]}")
    
    # 2. Matrix Organization
    print("\n\n2. MATRIX ORGANIZATION")
    print("-" * 22)
    matrix = builder.matrix_organization()
    
    print(f"Type: {matrix['topology_type']}")
    print(f"Description: {matrix['description']}")
    print("\nFunctional Hierarchy:")
    for layer_name, layer in matrix['functional_hierarchy'].items():
        print(f"  {layer_name}: {', '.join(layer.agents)} ({layer.internal_topology.value})")
    
    print("\nProject Hierarchy:")
    for layer_name, layer in matrix['project_hierarchy'].items():
        print(f"  {layer_name}: {', '.join(layer.agents)} ({layer.internal_topology.value})")
    
    # 3. Federated Mesh
    print("\n\n3. FEDERATED MESH")
    print("-" * 17)
    federated = builder.federated_mesh()
    
    print(f"Type: {federated['topology_type']}")
    print(f"Description: {federated['description']}")
    print("\nClusters:")
    for cluster in federated['clusters']:
        print(f"  {cluster.name}: {', '.join(cluster.agents)} ({cluster.internal_topology.value})")
    
    print(f"\nLeader Network:")
    leader_net = federated['leader_network']
    print(f"  {leader_net.name}: {', '.join(leader_net.agents)} ({leader_net.internal_topology.value})")
    
    # 4. Supervised Pipeline
    print("\n\n4. SUPERVISED PIPELINE")
    print("-" * 22)
    supervised = builder.pipeline_with_supervisors()
    
    print(f"Type: {supervised['topology_type']}")
    print(f"Description: {supervised['description']}")
    print(f"\nSupervisor: {', '.join(supervised['supervisor'].agents)}")
    print(f"Pipeline: {', '.join(supervised['pipeline'].agents)} ({supervised['pipeline'].internal_topology.value})")
    print(f"Pattern: {supervised['pattern']}")

def show_topology_mathematics():
    """Show the mathematical combinations of basic topologies"""
    
    print("\n\nTOPOLOGY MATHEMATICS")
    print("=" * 25)
    
    combinations = [
        {
            "name": "Hierarchical",
            "formula": "Sequential(layers) + Mesh(within_layer)",
            "example": "Leader -> [Lieutenant Mesh] -> [Worker Pipeline]",
            "complexity": "O(layers) + O(n²) per layer"
        },
        {
            "name": "Matrix",
            "formula": "Multiple overlapping hierarchies",
            "example": "Functional hierarchy ∩ Project hierarchy",
            "complexity": "O(h1 * h2) where h1, h2 are hierarchy depths"
        },
        {
            "name": "Federated",
            "formula": "Star(cluster_leaders) + Mesh(per_cluster)",
            "example": "[Mesh Cluster] <-> Star <-> [Mesh Cluster]",
            "complexity": "O(clusters) + O(n²/clusters)"
        },
        {
            "name": "Supervised Pipeline",
            "formula": "Star(supervision) over Linear(processing)",
            "example": "Supervisor -> [A1 -> A2 -> A3 -> A4]",
            "complexity": "O(1) + O(n) = O(n)"
        }
    ]
    
    for combo in combinations:
        print(f"\n{combo['name']}:")
        print(f"  Formula: {combo['formula']}")
        print(f"  Example: {combo['example']}")
        print(f"  Complexity: {combo['complexity']}")

if __name__ == "__main__":
    demonstrate_hybrid_topologies()
    show_topology_mathematics()
    
    print("\n\nKEY INSIGHTS:")
    print("=" * 15)
    print("• Hierarchical = Sequential between layers + Mesh within layers")
    print("• Complex topologies are combinations of basic patterns")
    print("• Each layer can have different internal communication patterns")
    print("• Inter-layer connections follow different rules than intra-layer")
    print("• Matrix organizations have multiple overlapping hierarchies")
    print("• Federated systems combine local mesh with global star patterns")