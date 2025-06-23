#!/usr/bin/env python3
"""
Omniscient Agent Communication System
Each agent can capture ALL screens but communication is controlled by permissions
"""

import subprocess
import json
import time
import tempfile
import os
from typing import Dict, List, Set, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class CommunicationPermission(Enum):
    SEND = "send"
    RECEIVE = "receive"
    BROADCAST = "broadcast"
    OBSERVE = "observe"  # Can see but not interact
    BLOCKED = "blocked"

@dataclass
class PermissionRule:
    """Define communication permissions between agents"""
    from_agent: str
    to_agent: str
    permission: CommunicationPermission
    conditions: List[str] = None  # Optional conditions
    
class TopologyPermissionManager:
    """Manages communication permissions to enforce different topologies"""
    
    def __init__(self, agents: List[str]):
        self.agents = agents
        self.permission_matrix: Dict[Tuple[str, str], CommunicationPermission] = {}
        self.global_observers: Set[str] = set()  # Agents that can observe all
        
    def set_permission(self, from_agent: str, to_agent: str, permission: CommunicationPermission):
        """Set communication permission between two agents"""
        self.permission_matrix[(from_agent, to_agent)] = permission
        
    def get_permission(self, from_agent: str, to_agent: str) -> CommunicationPermission:
        """Get communication permission between two agents"""
        return self.permission_matrix.get((from_agent, to_agent), CommunicationPermission.BLOCKED)
    
    def can_send(self, from_agent: str, to_agent: str) -> bool:
        """Check if agent can send message to another agent"""
        perm = self.get_permission(from_agent, to_agent)
        return perm in [CommunicationPermission.SEND, CommunicationPermission.BROADCAST]
    
    def can_observe(self, observer: str, target: str) -> bool:
        """Check if agent can observe another agent's screen"""
        if observer in self.global_observers:
            return True
        perm = self.get_permission(observer, target)
        return perm in [CommunicationPermission.OBSERVE, CommunicationPermission.SEND, 
                       CommunicationPermission.RECEIVE, CommunicationPermission.BROADCAST]
    
    def add_global_observer(self, agent: str):
        """Add agent as global observer (can see all screens)"""
        self.global_observers.add(agent)
    
    def configure_linear_topology(self):
        """Configure permissions for linear topology: A1 -> A2 -> A3 -> A4"""
        self._clear_permissions()
        
        for i in range(len(self.agents) - 1):
            current = self.agents[i]
            next_agent = self.agents[i + 1]
            
            # Only allow sending to next agent in chain
            self.set_permission(current, next_agent, CommunicationPermission.SEND)
            self.set_permission(next_agent, current, CommunicationPermission.RECEIVE)
            
            # Allow observing next agent
            self.set_permission(current, next_agent, CommunicationPermission.OBSERVE)
    
    def configure_ring_topology(self):
        """Configure permissions for ring topology: A1 -> A2 -> A3 -> A4 -> A1"""
        self.configure_linear_topology()
        
        # Add the ring closure: last -> first
        if len(self.agents) > 1:
            last = self.agents[-1]
            first = self.agents[0]
            self.set_permission(last, first, CommunicationPermission.SEND)
            self.set_permission(first, last, CommunicationPermission.RECEIVE)
    
    def configure_star_topology(self, center_agent: str):
        """Configure permissions for star topology"""
        self._clear_permissions()
        
        for agent in self.agents:
            if agent != center_agent:
                # Center can send to all
                self.set_permission(center_agent, agent, CommunicationPermission.BROADCAST)
                # All can send back to center
                self.set_permission(agent, center_agent, CommunicationPermission.SEND)
                # Center can observe all
                self.set_permission(center_agent, agent, CommunicationPermission.OBSERVE)
    
    def configure_mesh_topology(self):
        """Configure permissions for full mesh topology"""
        self._clear_permissions()
        
        for agent1 in self.agents:
            for agent2 in self.agents:
                if agent1 != agent2:
                    self.set_permission(agent1, agent2, CommunicationPermission.SEND)
                    self.set_permission(agent1, agent2, CommunicationPermission.OBSERVE)
    
    def configure_hierarchical_topology(self):
        """Configure permissions for hierarchical topology"""
        self._clear_permissions()
        
        if len(self.agents) < 3:
            return
            
        leader = self.agents[0]
        lieutenants = self.agents[1:3] if len(self.agents) > 2 else self.agents[1:2]
        workers = self.agents[3:] if len(self.agents) > 3 else []
        
        # Leader -> Lieutenants
        for lt in lieutenants:
            self.set_permission(leader, lt, CommunicationPermission.BROADCAST)
            self.set_permission(lt, leader, CommunicationPermission.SEND)
        
        # Lieutenants -> Workers
        for lt in lieutenants:
            for worker in workers:
                self.set_permission(lt, worker, CommunicationPermission.SEND)
                self.set_permission(worker, lt, CommunicationPermission.SEND)
        
        # Leader can observe all
        self.add_global_observer(leader)
    
    def _clear_permissions(self):
        """Clear all permissions"""
        self.permission_matrix.clear()
        self.global_observers.clear()

class OmniscientAgent:
    """Agent that can capture all screens but is constrained by permissions"""
    
    def __init__(self, agent_id: str, all_agents: List[str], permission_manager: TopologyPermissionManager):
        self.agent_id = agent_id
        self.all_agents = all_agents
        self.permission_manager = permission_manager
        self.temp_dir = tempfile.gettempdir()
        self.screen_data: Dict[str, str] = {}  # agent_id -> latest screen content
        
    def capture_all_screens(self) -> Dict[str, str]:
        """Capture ALL agent screens regardless of permissions"""
        captured_data = {}
        
        for agent in self.all_agents:
            inbox_session = f"{agent}_inbox"
            outbox_session = f"{agent}_outbox"
            
            # Capture inbox
            try:
                inbox_file = os.path.join(self.temp_dir, f"capture_{agent}_inbox")
                subprocess.run([
                    "screen", "-S", inbox_session, "-X", "hardcopy", inbox_file
                ], check=True)
                
                with open(inbox_file, 'r') as f:
                    inbox_content = f.read()
                os.remove(inbox_file)
                
                captured_data[f"{agent}_inbox"] = inbox_content
                
            except (subprocess.CalledProcessError, FileNotFoundError):
                captured_data[f"{agent}_inbox"] = ""
            
            # Capture outbox
            try:
                outbox_file = os.path.join(self.temp_dir, f"capture_{agent}_outbox")
                subprocess.run([
                    "screen", "-S", outbox_session, "-X", "hardcopy", outbox_file
                ], check=True)
                
                with open(outbox_file, 'r') as f:
                    outbox_content = f.read()
                os.remove(outbox_file)
                
                captured_data[f"{agent}_outbox"] = outbox_content
                
            except (subprocess.CalledProcessError, FileNotFoundError):
                captured_data[f"{agent}_outbox"] = ""
        
        self.screen_data = captured_data
        return captured_data
    
    def get_observable_screens(self) -> Dict[str, str]:
        """Get only screens this agent is permitted to observe"""
        observable = {}
        
        for agent in self.all_agents:
            if self.permission_manager.can_observe(self.agent_id, agent):
                if f"{agent}_inbox" in self.screen_data:
                    observable[f"{agent}_inbox"] = self.screen_data[f"{agent}_inbox"]
                if f"{agent}_outbox" in self.screen_data:
                    observable[f"{agent}_outbox"] = self.screen_data[f"{agent}_outbox"]
        
        # Always can observe own screens
        if f"{self.agent_id}_inbox" in self.screen_data:
            observable[f"{self.agent_id}_inbox"] = self.screen_data[f"{self.agent_id}_inbox"]
        if f"{self.agent_id}_outbox" in self.screen_data:
            observable[f"{self.agent_id}_outbox"] = self.screen_data[f"{self.agent_id}_outbox"]
        
        return observable
    
    def send_message(self, recipient: str, message: str) -> bool:
        """Send message if permitted"""
        if not self.permission_manager.can_send(self.agent_id, recipient):
            print(f"[{self.agent_id}] BLOCKED: Cannot send to {recipient}")
            return False
        
        try:
            # Send to recipient's inbox
            subprocess.run([
                "screen", "-S", f"{recipient}_inbox", "-X", "stuff", 
                f"MSG from {self.agent_id}: {message}\n"
            ], check=True)
            
            # Log in own outbox
            subprocess.run([
                "screen", "-S", f"{self.agent_id}_outbox", "-X", "stuff",
                f"SENT to {recipient}: {message}\n"
            ], check=True)
            
            print(f"[{self.agent_id}] SENT to {recipient}: {message}")
            return True
            
        except subprocess.CalledProcessError:
            return False
    
    def broadcast_message(self, message: str) -> int:
        """Broadcast message to all permitted recipients"""
        sent_count = 0
        
        for agent in self.all_agents:
            if agent != self.agent_id and self.send_message(agent, f"BROADCAST: {message}"):
                sent_count += 1
        
        return sent_count
    
    def get_intelligence_report(self) -> Dict:
        """Generate intelligence report based on observable screens"""
        self.capture_all_screens()
        observable = self.get_observable_screens()
        
        report = {
            "agent_id": self.agent_id,
            "timestamp": time.time(),
            "total_screens_captured": len(self.screen_data),
            "observable_screens": len(observable),
            "blocked_screens": len(self.screen_data) - len(observable),
            "permissions": {},
            "intelligence": []
        }
        
        # Add permission summary
        for agent in self.all_agents:
            if agent != self.agent_id:
                report["permissions"][agent] = {
                    "can_send": self.permission_manager.can_send(self.agent_id, agent),
                    "can_observe": self.permission_manager.can_observe(self.agent_id, agent)
                }
        
        # Add intelligence from observable screens
        for screen_name, content in observable.items():
            if content.strip():
                report["intelligence"].append({
                    "screen": screen_name,
                    "content_length": len(content),
                    "has_messages": "MSG from" in content
                })
        
        return report

def demonstrate_omniscient_system():
    """Demonstrate the omniscient agent system with different topologies"""
    
    print("OMNISCIENT AGENT SYSTEM DEMONSTRATION")
    print("=" * 45)
    
    agents = ["agent1", "agent2", "agent3", "agent4"]
    permission_manager = TopologyPermissionManager(agents)
    
    # Create omniscient agents
    omniscient_agents = {}
    for agent_id in agents:
        omniscient_agents[agent_id] = OmniscientAgent(agent_id, agents, permission_manager)
    
    # Create screen sessions for demo
    print("\nCreating screen sessions...")
    for agent in agents:
        try:
            subprocess.run(["screen", "-dmS", f"{agent}_inbox"], check=True)
            subprocess.run(["screen", "-dmS", f"{agent}_outbox"], check=True)
        except subprocess.CalledProcessError:
            pass
    
    print("Sessions created!")
    
    # Test different topologies
    topologies = [
        ("Linear Chain", lambda: permission_manager.configure_linear_topology()),
        ("Ring", lambda: permission_manager.configure_ring_topology()),
        ("Star (agent1 center)", lambda: permission_manager.configure_star_topology("agent1")),
        ("Full Mesh", lambda: permission_manager.configure_mesh_topology()),
        ("Hierarchical", lambda: permission_manager.configure_hierarchical_topology())
    ]
    
    for topology_name, configure_func in topologies:
        print(f"\n{'='*20} {topology_name} {'='*20}")
        configure_func()
        
        # Test communication
        agent1 = omniscient_agents["agent1"]
        
        if topology_name == "Linear Chain":
            agent1.send_message("agent2", "Hello from linear chain!")
        elif topology_name == "Star (agent1 center)":
            agent1.broadcast_message("Star broadcast from center!")
        elif topology_name == "Full Mesh":
            agent1.send_message("agent3", "Mesh message to agent3!")
        
        time.sleep(1)
        
        # Generate intelligence reports
        for agent_id, agent in omniscient_agents.items():
            report = agent.get_intelligence_report()
            print(f"\n{agent_id} Intelligence Report:")
            print(f"  Captured {report['total_screens_captured']} screens")
            print(f"  Observable: {report['observable_screens']}")
            print(f"  Blocked: {report['blocked_screens']}")
            
            print(f"  Permissions:")
            for target, perms in report['permissions'].items():
                print(f"    {target}: Send={perms['can_send']}, Observe={perms['can_observe']}")
    
    # Cleanup
    print("\nCleaning up sessions...")
    for agent in agents:
        try:
            subprocess.run(["screen", "-S", f"{agent}_inbox", "-X", "quit"], check=True)
            subprocess.run(["screen", "-S", f"{agent}_outbox", "-X", "quit"], check=True)
        except subprocess.CalledProcessError:
            pass

if __name__ == "__main__":
    demonstrate_omniscient_system()
    
    print("\n\nKEY INSIGHTS:")
    print("=" * 15)
    print("• All agents can capture ALL screens (omniscient capability)")
    print("• Communication topology controlled by permission matrix")
    print("• Agents can 'see' everything but only 'act' within permissions")
    print("• Intelligence gathering vs. communication are separate concerns")
    print("• Enables sophisticated monitoring and debugging capabilities")
    print("• Security through permissions, not technical limitations")