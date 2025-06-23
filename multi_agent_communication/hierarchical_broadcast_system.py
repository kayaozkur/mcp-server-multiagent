#!/usr/bin/env python3
"""
Hierarchical Broadcast System
Broadcasts with rank-based visibility and priority in common inbox
"""

import subprocess
import time
import threading
import json
import os
import tempfile
from typing import List, Dict, Set
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class Rank(Enum):
    USER = 1        # Highest priority - trumps everything
    LEADER = 2      # Executive level
    MANAGER = 3     # Management level  
    WORKER = 4      # Worker level

@dataclass
class Agent:
    id: str
    rank: Rank
    reports_to: str = None  # Direct supervisor
    manages: List[str] = None  # Direct reports

class HierarchicalBroadcastSystem:
    """Broadcast system with rank-based visibility rules"""
    
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.common_inbox_session = "common_inbox"
        self.temp_dir = tempfile.gettempdir()
        self.message_counter = 0
        
        # Broadcast visibility rules
        self.visibility_rules = {
            Rank.USER: [Rank.USER, Rank.LEADER, Rank.MANAGER, Rank.WORKER],  # User sees everything
            Rank.LEADER: [Rank.LEADER, Rank.MANAGER, Rank.WORKER],          # Leader sees subordinates
            Rank.MANAGER: [Rank.MANAGER, Rank.WORKER],                      # Manager sees workers + peers
            Rank.WORKER: [Rank.WORKER]                                      # Workers see only peer level
        }
        
        # Priority ordering (lower number = higher priority)
        self.priority_order = {
            Rank.USER: 1,
            Rank.LEADER: 2, 
            Rank.MANAGER: 3,
            Rank.WORKER: 4
        }
    
    def add_agent(self, agent_id: str, rank: Rank, reports_to: str = None, manages: List[str] = None):
        """Add an agent with hierarchy information"""
        self.agents[agent_id] = Agent(
            id=agent_id,
            rank=rank,
            reports_to=reports_to,
            manages=manages or []
        )
    
    def setup_example_hierarchy(self):
        """Set up an example organizational hierarchy"""
        # User (highest rank)
        self.add_agent("user", Rank.USER)
        
        # Leadership layer
        self.add_agent("ceo", Rank.LEADER, reports_to="user", manages=["manager1", "manager2"])
        
        # Management layer
        self.add_agent("manager1", Rank.MANAGER, reports_to="ceo", manages=["worker1", "worker2"])
        self.add_agent("manager2", Rank.MANAGER, reports_to="ceo", manages=["worker3", "worker4"])
        
        # Worker layer
        self.add_agent("worker1", Rank.WORKER, reports_to="manager1")
        self.add_agent("worker2", Rank.WORKER, reports_to="manager1") 
        self.add_agent("worker3", Rank.WORKER, reports_to="manager2")
        self.add_agent("worker4", Rank.WORKER, reports_to="manager2")
    
    def initialize_sessions(self):
        """Create all necessary sessions"""
        print("Creating hierarchical broadcast sessions...")
        
        # Create common inbox
        try:
            subprocess.run(["screen", "-dmS", self.common_inbox_session], check=True)
            subprocess.run([
                "screen", "-S", self.common_inbox_session, "-X", "stuff",
                "=== HIERARCHICAL COMMON INBOX ===\n"
            ], check=True)
            print(f"✓ Created: {self.common_inbox_session}")
        except subprocess.CalledProcessError:
            print(f"✗ Failed: {self.common_inbox_session}")
        
        # Create agent sessions
        for agent_id in self.agents:
            sessions = [f"{agent_id}_inbox", f"{agent_id}_outbox", f"{agent_id}_signals"]
            for session in sessions:
                try:
                    subprocess.run(["screen", "-dmS", session], check=True)
                    print(f"✓ Created: {session}")
                except subprocess.CalledProcessError:
                    print(f"✗ Failed: {session}")
    
    def cleanup_sessions(self):
        """Clean up all sessions"""
        # Cleanup common inbox
        try:
            subprocess.run(["screen", "-S", self.common_inbox_session, "-X", "quit"], check=True)
        except subprocess.CalledProcessError:
            pass
        
        # Cleanup agent sessions
        for agent_id in self.agents:
            sessions = [f"{agent_id}_inbox", f"{agent_id}_outbox", f"{agent_id}_signals"]
            for session in sessions:
                try:
                    subprocess.run(["screen", "-S", session, "-X", "quit"], check=True)
                except subprocess.CalledProcessError:
                    pass
    
    def can_see_broadcast(self, viewer_rank: Rank, broadcaster_rank: Rank) -> bool:
        """Determine if viewer can see broadcaster's messages"""
        return broadcaster_rank in self.visibility_rules.get(viewer_rank, [])
    
    def get_broadcast_priority(self, broadcaster_rank: Rank) -> int:
        """Get priority level for broadcast (lower = higher priority)"""
        return self.priority_order.get(broadcaster_rank, 999)
    
    def log_hierarchical_broadcast(self, sender: str, content: str, broadcast_type: str = "broadcast"):
        """Log broadcast to common inbox with hierarchy information"""
        
        if sender not in self.agents:
            print(f"Unknown sender: {sender}")
            return
        
        sender_agent = self.agents[sender]
        self.message_counter += 1
        timestamp = datetime.now().strftime("%H:%M:%S")
        priority = self.get_broadcast_priority(sender_agent.rank)
        
        # Create hierarchical log entry
        rank_symbol = {
            Rank.USER: "👑",      # Crown for user
            Rank.LEADER: "⭐",    # Star for leader  
            Rank.MANAGER: "🔶",   # Diamond for manager
            Rank.WORKER: "🔸"     # Small diamond for worker
        }.get(sender_agent.rank, "•")
        
        log_entry = (f"[{timestamp}] #{self.message_counter:03d} "
                    f"P{priority} {rank_symbol} {sender_agent.rank.name} "
                    f"{sender} BROADCAST: {content}")
        
        try:
            subprocess.run([
                "screen", "-S", self.common_inbox_session, "-X", "stuff",
                f"{log_entry}\n"
            ], check=True)
            print(f"[COMMON INBOX] {log_entry}")
        except subprocess.CalledProcessError:
            print(f"[COMMON INBOX] Failed to log broadcast")
    
    def send_direct_message(self, sender: str, recipient: str, content: str):
        """Send direct message with hierarchy logging"""
        
        if sender not in self.agents or recipient not in self.agents:
            print(f"Unknown agent: {sender} or {recipient}")
            return
        
        sender_agent = self.agents[sender]
        recipient_agent = self.agents[recipient]
        
        # Send to recipient's inbox
        try:
            subprocess.run([
                "screen", "-S", f"{recipient}_inbox", "-X", "stuff",
                f"DIRECT from {sender}: {content}\n"
            ], check=True)
        except subprocess.CalledProcessError:
            return
        
        # Log to common inbox
        self.message_counter += 1
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        log_entry = (f"[{timestamp}] #{self.message_counter:03d} "
                    f"{sender_agent.rank.name} {sender} -> {recipient_agent.rank.name} {recipient}: {content}")
        
        try:
            subprocess.run([
                "screen", "-S", self.common_inbox_session, "-X", "stuff",
                f"{log_entry}\n"
            ], check=True)
            print(f"[COMMON INBOX] {log_entry}")
        except subprocess.CalledProcessError:
            pass

class HierarchicalAgent:
    """Agent that understands hierarchy and broadcast visibility"""
    
    def __init__(self, agent_id: str, hierarchy_system: HierarchicalBroadcastSystem):
        self.agent_id = agent_id
        self.hierarchy_system = hierarchy_system
        self.temp_dir = tempfile.gettempdir()
        
        # Get agent info
        self.agent_info = hierarchy_system.agents.get(agent_id)
        if not self.agent_info:
            raise ValueError(f"Agent {agent_id} not found in hierarchy")
        
        # Personal sessions
        self.inbox_session = f"{agent_id}_inbox"
        self.outbox_session = f"{agent_id}_outbox"
        self.signals_session = f"{agent_id}_signals"
        
        # Monitoring
        self.monitoring_active = False
        self.monitor_thread = None
    
    def broadcast_message(self, content: str):
        """Send hierarchical broadcast"""
        
        # Determine who should receive this broadcast
        my_rank = self.agent_info.rank
        recipients = []
        
        for agent_id, agent in self.hierarchy_system.agents.items():
            if (agent_id != self.agent_id and 
                self.hierarchy_system.can_see_broadcast(agent.rank, my_rank)):
                recipients.append(agent_id)
        
        # Send to recipient inboxes
        for recipient in recipients:
            try:
                subprocess.run([
                    "screen", "-S", f"{recipient}_inbox", "-X", "stuff",
                    f"BROADCAST from {my_rank.name} {self.agent_id}: {content}\n"
                ], check=True)
                
                # Trigger polling
                subprocess.run([
                    "screen", "-S", f"{recipient}_signals", "-X", "stuff",
                    f"POLL_TRIGGER:broadcast\n"
                ], check=True)
            except subprocess.CalledProcessError:
                pass
        
        # Log to own outbox
        try:
            subprocess.run([
                "screen", "-S", self.outbox_session, "-X", "stuff",
                f"BROADCAST ({my_rank.name}) to {len(recipients)} agents: {content}\n"
            ], check=True)
        except subprocess.CalledProcessError:
            pass
        
        # Log to hierarchical common inbox
        self.hierarchy_system.log_hierarchical_broadcast(self.agent_id, content)
        
        print(f"[{self.agent_id}] Broadcast sent to {len(recipients)} agents")
    
    def send_direct_message(self, recipient: str, content: str):
        """Send direct message"""
        self.hierarchy_system.send_direct_message(self.agent_id, recipient, content)
    
    def start_monitoring(self):
        """Start monitoring with hierarchy awareness"""
        self.monitoring_active = True
        self.monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitor_thread.start()
        print(f"[{self.agent_id}] Started hierarchical monitoring")
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.monitoring_active = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2)
    
    def _monitoring_loop(self):
        """Monitor with hierarchy-aware filtering"""
        while self.monitoring_active:
            try:
                # Monitor personal inbox
                self._check_personal_inbox()
                
                # Monitor common inbox with hierarchy filtering
                self._check_hierarchical_common_inbox()
                
                time.sleep(2)
                
            except Exception as e:
                if self.monitoring_active:
                    print(f"[{self.agent_id}] Monitor error: {e}")
                time.sleep(1)
    
    def _check_personal_inbox(self):
        """Check personal inbox"""
        try:
            inbox_file = os.path.join(self.temp_dir, f"personal_{self.agent_id}")
            subprocess.run([
                "screen", "-S", self.inbox_session, "-X", "hardcopy", inbox_file
            ], check=True)
            
            with open(inbox_file, 'r') as f:
                content = f.read()
            
            os.remove(inbox_file)
            
            # Process new messages
            lines = content.split('\n')
            for line in lines:
                if ("DIRECT from" in line or "BROADCAST from" in line) and line.strip():
                    print(f"[{self.agent_id}] RECEIVED: {line.strip()}")
                        
        except Exception:
            pass
    
    def _check_hierarchical_common_inbox(self):
        """Check common inbox with hierarchy-based filtering"""
        try:
            common_file = os.path.join(self.temp_dir, f"common_{self.agent_id}")
            subprocess.run([
                "screen", "-S", self.hierarchy_system.common_inbox_session, "-X", "hardcopy", common_file
            ], check=True)
            
            with open(common_file, 'r') as f:
                content = f.read()
            
            os.remove(common_file)
            
            # Filter messages based on hierarchy
            lines = content.split('\n')
            for line in lines:
                if "] #" in line and line.strip():
                    should_see = self._should_see_common_message(line)
                    if should_see and self.agent_id not in line:
                        print(f"[{self.agent_id}] NETWORK: {line.strip()}")
                        
        except Exception:
            pass
    
    def _should_see_common_message(self, message: str) -> bool:
        """Determine if this agent should see this common inbox message"""
        
        # Extract sender rank from message
        for rank in Rank:
            if rank.name in message:
                sender_rank = rank
                break
        else:
            return True  # If no rank found, show by default
        
        # Check if our rank can see messages from sender rank
        my_rank = self.agent_info.rank
        return self.hierarchy_system.can_see_broadcast(my_rank, sender_rank)
    
    def get_hierarchy_view(self) -> Dict:
        """Get this agent's view of the hierarchy"""
        my_rank = self.agent_info.rank
        
        return {
            "agent_id": self.agent_id,
            "my_rank": my_rank.name,
            "can_see_ranks": [rank.name for rank in self.hierarchy_system.visibility_rules.get(my_rank, [])],
            "reports_to": self.agent_info.reports_to,
            "manages": self.agent_info.manages,
            "hierarchy_peers": [
                agent_id for agent_id, agent in self.hierarchy_system.agents.items()
                if agent.rank == my_rank and agent_id != self.agent_id
            ]
        }

def demonstrate_hierarchical_broadcasts():
    """Demonstrate hierarchical broadcast system"""
    
    print("HIERARCHICAL BROADCAST SYSTEM")
    print("=" * 35)
    
    # Create system and hierarchy
    hierarchy = HierarchicalBroadcastSystem()
    hierarchy.setup_example_hierarchy()
    hierarchy.initialize_sessions()
    
    # Create agents
    agents = {}
    for agent_id in hierarchy.agents:
        agents[agent_id] = HierarchicalAgent(agent_id, hierarchy)
    
    try:
        # Start monitoring
        for agent in agents.values():
            agent.start_monitoring()
        
        time.sleep(2)
        
        print("\n" + "="*60)
        print("ORGANIZATIONAL HIERARCHY:")
        print("="*60)
        
        for agent_id, agent_obj in agents.items():
            view = agent_obj.get_hierarchy_view()
            print(f"{agent_id.upper()} ({view['my_rank']}):")
            print(f"  Can see: {', '.join(view['can_see_ranks'])}")
            if view['reports_to']:
                print(f"  Reports to: {view['reports_to']}")
            if view['manages']:
                print(f"  Manages: {', '.join(view['manages'])}")
            print()
        
        print("BROADCAST SCENARIOS:")
        print("="*60)
        
        # Scenario 1: Worker broadcast (limited visibility)
        print("\n1. WORKER BROADCAST (limited scope):")
        agents["worker1"].broadcast_message("Need help with task X")
        time.sleep(2)
        
        # Scenario 2: Manager broadcast (trickles down)
        print("\n2. MANAGER BROADCAST (trickles down):")
        agents["manager1"].broadcast_message("Team meeting at 3 PM")
        time.sleep(2)
        
        # Scenario 3: Leader broadcast (wide visibility)
        print("\n3. LEADER BROADCAST (company-wide):")
        agents["ceo"].broadcast_message("Quarterly results are excellent!")
        time.sleep(2)
        
        # Scenario 4: User broadcast (trumps everything)
        print("\n4. USER BROADCAST (highest priority):")
        agents["user"].broadcast_message("URGENT: System maintenance in 5 minutes")
        time.sleep(3)
        
        print("\nLetting system process messages...")
        time.sleep(2)
        
    except KeyboardInterrupt:
        print("\nInterrupted...")
    finally:
        # Cleanup
        for agent in agents.values():
            agent.stop_monitoring()
        hierarchy.cleanup_sessions()

if __name__ == "__main__":
    demonstrate_hierarchical_broadcasts()
    
    print("\n\nHIERARCHY RULES:")
    print("=" * 16)
    print("👑 USER: Sees everything, highest priority")
    print("⭐ LEADER: Sees leader/manager/worker levels")  
    print("🔶 MANAGER: Sees manager/worker levels")
    print("🔸 WORKER: Sees only worker level")
    print()
    print("BROADCAST FLOW:")
    print("• Worker broadcasts: Only workers see it")
    print("• Manager broadcasts: Managers + workers see it") 
    print("• Leader broadcasts: Everyone except user sees it")
    print("• User broadcasts: EVERYONE sees it (trumps all)")