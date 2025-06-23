#!/usr/bin/env python3
"""
Advanced Communication Patterns for Multi-Agent Networks
Demonstrates various non-linear communication topologies
"""

from multi_agent_screen_network import *
import random
import asyncio

class CommunicationPatterns:
    """Advanced communication patterns and topologies"""
    
    @staticmethod
    def ring_topology(network: MultiAgentNetworkManager, message: str):
        """Agents communicate in a ring: A1 -> A2 -> A3 -> A4 -> A1"""
        agents = list(network.agents.keys())
        
        for i, agent_id in enumerate(agents):
            next_agent = agents[(i + 1) % len(agents)]
            network.agents[agent_id].send_message(next_agent, f"Ring message: {message}")
    
    @staticmethod
    def star_topology_broadcast(network: MultiAgentNetworkManager, center_agent: str, message: str):
        """One agent broadcasts to all others (star pattern)"""
        if center_agent in network.agents:
            network.agents[center_agent].broadcast_message(f"Star broadcast: {message}")
    
    @staticmethod
    def mesh_discussion(network: MultiAgentNetworkManager, topic: str):
        """Full mesh discussion where each agent talks to every other agent"""
        agents = list(network.agents.keys())
        
        for sender in agents:
            for receiver in agents:
                if sender != receiver:
                    network.agents[sender].send_message(
                        receiver, 
                        f"Discussing '{topic}' - {sender}'s perspective"
                    )
    
    @staticmethod
    def consensus_protocol(network: MultiAgentNetworkManager, proposal: str):
        """Implement a consensus protocol where agents vote and reach agreement"""
        agents = list(network.agents.keys())
        
        # Phase 1: Broadcast proposal
        initiator = agents[0]
        network.agents[initiator].broadcast_message(f"PROPOSAL:{proposal}")
        
        # Each agent would implement voting logic in their handlers
        # This demonstrates the structure for consensus building
    
    @staticmethod
    def hierarchical_communication(network: MultiAgentNetworkManager):
        """Hierarchical communication pattern (leader -> subordinates)"""
        agents = list(network.agents.keys())
        if len(agents) < 3:
            return
        
        leader = agents[0]
        lieutenants = agents[1:3] if len(agents) > 2 else agents[1:2]
        workers = agents[3:] if len(agents) > 3 else []
        
        # Leader to lieutenants
        for lt in lieutenants:
            network.agents[leader].send_message(lt, "DIRECTIVE:Execute tasks")
        
        # Lieutenants to workers
        for lt in lieutenants:
            for worker in workers:
                network.agents[lt].send_message(worker, f"TASK:From {lt}")

class AdvancedAgentBehaviors:
    """Advanced agent behaviors and interaction patterns"""
    
    @staticmethod
    def create_negotiating_agents(network: MultiAgentNetworkManager):
        """Create agents that negotiate and make deals"""
        
        def negotiator_handler(agent_id: str):
            def handler(message: Message):
                if "OFFER:" in message.content:
                    # Simple negotiation logic
                    offer_value = message.content.split("OFFER:")[1]
                    response = f"COUNTER:{int(float(offer_value)) + 10}"
                    network.agents[agent_id].send_message(message.sender, response)
                elif "COUNTER:" in message.content:
                    print(f"[{agent_id}] Received counter-offer: {message.content}")
                    # Could accept or make another counter
                    network.agents[agent_id].send_message(message.sender, "ACCEPT")
            return handler
        
        for agent_id in network.agents:
            network.agents[agent_id].register_message_handler("text", negotiator_handler(agent_id))
    
    @staticmethod
    def create_collaborative_agents(network: MultiAgentNetworkManager):
        """Create agents that collaborate on tasks"""
        
        task_assignments = {}
        
        def collaborator_handler(agent_id: str):
            def handler(message: Message):
                if "TASK_REQUEST:" in message.content:
                    task = message.content.split("TASK_REQUEST:")[1]
                    # Assign task part to this agent
                    task_assignments[agent_id] = task
                    network.agents[agent_id].send_message(message.sender, f"TASK_ACCEPTED:{task}")
                elif "RESULT:" in message.content:
                    print(f"[{agent_id}] Received result: {message.content}")
                    # Could aggregate results here
            return handler
        
        for agent_id in network.agents:
            network.agents[agent_id].register_message_handler("text", collaborator_handler(agent_id))
    
    @staticmethod
    def create_competitive_agents(network: MultiAgentNetworkManager):
        """Create agents that compete for resources"""
        
        resources = {"resource1": 100, "resource2": 50, "resource3": 25}
        
        def competitor_handler(agent_id: str):
            def handler(message: Message):
                if "BID:" in message.content:
                    # Simple auction logic
                    bid_info = message.content.split("BID:")[1]
                    resource, amount = bid_info.split(",")
                    
                    # Make a competitive bid
                    counter_bid = int(amount) + random.randint(1, 10)
                    network.agents[agent_id].send_message(
                        message.sender, 
                        f"COUNTER_BID:{resource},{counter_bid}"
                    )
            return handler
        
        for agent_id in network.agents:
            network.agents[agent_id].register_message_handler("text", competitor_handler(agent_id))

def demo_communication_patterns():
    """Demonstrate various communication patterns"""
    
    print("Creating 4-agent mesh network for pattern demonstration...")
    
    network = MultiAgentNetworkManager()
    user = network.add_user()
    
    # Create 4 agents
    agents = []
    for i in range(1, 5):
        agent = network.add_agent(f"agent{i}")
        agents.append(agent)
    
    # Add basic message handlers
    for agent in agents:
        def make_basic_handler(agent_id):
            def handler(message: Message):
                print(f"[{agent_id.upper()}] {message.sender} -> {message.content[:50]}...")
            return handler
        agent.register_message_handler("text", make_basic_handler(agent.agent_id))
    
    try:
        network.start_network()
        time.sleep(2)
        
        print("\n1. Ring Topology Communication")
        CommunicationPatterns.ring_topology(network, "Hello ring!")
        time.sleep(3)
        
        print("\n2. Star Topology Broadcast")
        CommunicationPatterns.star_topology_broadcast(network, "agent1", "Important announcement!")
        time.sleep(3)
        
        print("\n3. Mesh Discussion")
        CommunicationPatterns.mesh_discussion(network, "AI Ethics")
        time.sleep(3)
        
        print("\n4. Hierarchical Communication")
        CommunicationPatterns.hierarchical_communication(network)
        time.sleep(3)
        
        print("\nDemonstration complete!")
        
    except KeyboardInterrupt:
        print("\nInterrupted...")
    finally:
        network.stop_network()

if __name__ == "__main__":
    demo_communication_patterns()