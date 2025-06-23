#!/usr/bin/env python3
"""
Common Inbox System
Single shared inbox where ALL communications are visible to everyone
"""

import subprocess
import time
import threading
import json
import os
import tempfile
from typing import List, Dict
from datetime import datetime

class CommonInboxSystem:
    """System with shared common inbox for all communications"""
    
    def __init__(self, agents: List[str]):
        self.agents = agents
        self.common_inbox_session = "common_inbox"
        self.temp_dir = tempfile.gettempdir()
        self.message_counter = 0
    
    def initialize_sessions(self):
        """Create all necessary sessions"""
        print("Creating sessions...")
        
        # Create common inbox
        try:
            subprocess.run(["screen", "-dmS", self.common_inbox_session], check=True)
            subprocess.run([
                "screen", "-S", self.common_inbox_session, "-X", "stuff",
                "=== COMMON INBOX - ALL COMMUNICATIONS ===\n"
            ], check=True)
            print(f"✓ Created: {self.common_inbox_session}")
        except subprocess.CalledProcessError:
            print(f"✗ Failed: {self.common_inbox_session}")
        
        # Create personal sessions for each agent
        for agent in self.agents:
            sessions = [f"{agent}_inbox", f"{agent}_outbox", f"{agent}_signals"]
            for session in sessions:
                try:
                    subprocess.run(["screen", "-dmS", session], check=True)
                    subprocess.run([
                        "screen", "-S", session, "-X", "stuff",
                        f"=== {session.upper()} ===\n"
                    ], check=True)
                    print(f"✓ Created: {session}")
                except subprocess.CalledProcessError:
                    print(f"✗ Failed: {session}")
    
    def cleanup_sessions(self):
        """Clean up all sessions"""
        print("Cleaning up sessions...")
        
        # Cleanup common inbox
        try:
            subprocess.run(["screen", "-S", self.common_inbox_session, "-X", "quit"], check=True)
        except subprocess.CalledProcessError:
            pass
        
        # Cleanup agent sessions
        for agent in self.agents:
            sessions = [f"{agent}_inbox", f"{agent}_outbox", f"{agent}_signals"]
            for session in sessions:
                try:
                    subprocess.run(["screen", "-S", session, "-X", "quit"], check=True)
                except subprocess.CalledProcessError:
                    pass
    
    def log_to_common_inbox(self, sender: str, recipient: str, content: str, msg_type: str = "direct"):
        """Log every message to the common inbox"""
        self.message_counter += 1
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if msg_type == "broadcast":
            log_entry = f"[{timestamp}] #{self.message_counter:03d} BROADCAST {sender} -> ALL: {content}"
        else:
            log_entry = f"[{timestamp}] #{self.message_counter:03d} {sender} -> {recipient}: {content}"
        
        try:
            subprocess.run([
                "screen", "-S", self.common_inbox_session, "-X", "stuff",
                f"{log_entry}\n"
            ], check=True)
            print(f"[COMMON INBOX] {log_entry}")
        except subprocess.CalledProcessError:
            print(f"[COMMON INBOX] Failed to log message")

class TransparentAgent:
    """Agent that logs all communications to common inbox"""
    
    def __init__(self, agent_id: str, all_agents: List[str], common_system: CommonInboxSystem):
        self.agent_id = agent_id
        self.all_agents = all_agents
        self.common_system = common_system
        self.temp_dir = tempfile.gettempdir()
        
        # Personal sessions
        self.inbox_session = f"{agent_id}_inbox"
        self.outbox_session = f"{agent_id}_outbox"
        self.signals_session = f"{agent_id}_signals"
        
        # Monitoring
        self.monitoring_active = False
        self.monitor_thread = None
    
    def send_message(self, recipient: str, content: str):
        """Send message and log to common inbox"""
        
        # Send to recipient's personal inbox
        try:
            subprocess.run([
                "screen", "-S", f"{recipient}_inbox", "-X", "stuff",
                f"FROM {self.agent_id}: {content}\n"
            ], check=True)
        except subprocess.CalledProcessError:
            print(f"[{self.agent_id}] Failed to send to {recipient}")
            return
        
        # Log to own outbox
        try:
            subprocess.run([
                "screen", "-S", self.outbox_session, "-X", "stuff",
                f"SENT to {recipient}: {content}\n"
            ], check=True)
        except subprocess.CalledProcessError:
            pass
        
        # LOG TO COMMON INBOX (This is the key!)
        self.common_system.log_to_common_inbox(
            sender=self.agent_id,
            recipient=recipient,
            content=content,
            msg_type="direct"
        )
    
    def broadcast_message(self, content: str):
        """Send broadcast and log to common inbox"""
        
        recipients = [agent for agent in self.all_agents if agent != self.agent_id]
        
        # Send to all recipient inboxes
        for recipient in recipients:
            try:
                subprocess.run([
                    "screen", "-S", f"{recipient}_inbox", "-X", "stuff",
                    f"BROADCAST FROM {self.agent_id}: {content}\n"
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
                f"BROADCAST to {len(recipients)} agents: {content}\n"
            ], check=True)
        except subprocess.CalledProcessError:
            pass
        
        # LOG TO COMMON INBOX (This is the key!)
        self.common_system.log_to_common_inbox(
            sender=self.agent_id,
            recipient="ALL",
            content=content,
            msg_type="broadcast"
        )
    
    def start_monitoring(self):
        """Start monitoring personal inbox and common inbox"""
        self.monitoring_active = True
        self.monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitor_thread.start()
        print(f"[{self.agent_id}] Started monitoring")
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.monitoring_active = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2)
    
    def _monitoring_loop(self):
        """Monitor personal inbox and common inbox"""
        while self.monitoring_active:
            try:
                # Check personal inbox
                self._check_personal_inbox()
                
                # Check common inbox for network awareness
                self._check_common_inbox()
                
                time.sleep(2)
                
            except Exception as e:
                if self.monitoring_active:
                    print(f"[{self.agent_id}] Monitor error: {e}")
                time.sleep(1)
    
    def _check_personal_inbox(self):
        """Check personal inbox for messages addressed to this agent"""
        try:
            inbox_file = os.path.join(self.temp_dir, f"personal_{self.agent_id}")
            subprocess.run([
                "screen", "-S", self.inbox_session, "-X", "hardcopy", inbox_file
            ], check=True)
            
            with open(inbox_file, 'r') as f:
                content = f.read()
            
            os.remove(inbox_file)
            
            # Process new personal messages
            lines = content.split('\n')
            for line in lines:
                if ("FROM " in line or "BROADCAST FROM" in line) and line.strip():
                    if not self._already_processed(line):
                        print(f"[{self.agent_id}] PERSONAL: {line.strip()}")
                        
        except Exception:
            pass
    
    def _check_common_inbox(self):
        """Check common inbox to see ALL network communications"""
        try:
            common_file = os.path.join(self.temp_dir, f"common_{self.agent_id}")
            subprocess.run([
                "screen", "-S", self.common_system.common_inbox_session, "-X", "hardcopy", common_file
            ], check=True)
            
            with open(common_file, 'r') as f:
                content = f.read()
            
            os.remove(common_file)
            
            # Show recent network activity (not involving this agent directly)
            lines = content.split('\n')
            recent_lines = lines[-3:] if len(lines) > 3 else lines
            
            for line in recent_lines:
                if ("] #" in line and 
                    self.agent_id not in line.split("->")[0] and  # Not sender
                    line.strip() and 
                    not self._already_seen(line)):
                    print(f"[{self.agent_id}] NETWORK: {line.strip()}")
                        
        except Exception:
            pass
    
    def _already_processed(self, message: str) -> bool:
        """Simple duplicate detection for personal messages"""
        return False  # Simplified for demo
    
    def _already_seen(self, message: str) -> bool:
        """Simple duplicate detection for network messages"""
        return False  # Simplified for demo
    
    def get_network_snapshot(self) -> Dict:
        """Get current snapshot of all network communications"""
        try:
            common_file = os.path.join(self.temp_dir, f"snapshot_{self.agent_id}")
            subprocess.run([
                "screen", "-S", self.common_system.common_inbox_session, "-X", "hardcopy", common_file
            ], check=True)
            
            with open(common_file, 'r') as f:
                content = f.read()
            
            os.remove(common_file)
            
            lines = [line for line in content.split('\n') if line.strip() and "] #" in line]
            
            return {
                "agent_id": self.agent_id,
                "total_messages": len(lines),
                "recent_activity": lines[-5:] if lines else [],
                "message_types": {
                    "direct": len([l for l in lines if "BROADCAST" not in l]),
                    "broadcast": len([l for l in lines if "BROADCAST" in l])
                }
            }
            
        except Exception:
            return {"agent_id": self.agent_id, "error": "Failed to get snapshot"}

def demonstrate_common_inbox():
    """Demonstrate the common inbox system"""
    
    print("COMMON INBOX SYSTEM DEMONSTRATION")
    print("=" * 40)
    
    agents = ["agent1", "agent2", "agent3"]
    
    # Create system
    common_system = CommonInboxSystem(agents)
    common_system.initialize_sessions()
    
    # Create agents
    agent_objects = {}
    for agent_id in agents:
        agent_objects[agent_id] = TransparentAgent(agent_id, agents, common_system)
    
    try:
        # Start monitoring
        for agent in agent_objects.values():
            agent.start_monitoring()
        
        time.sleep(2)
        
        print("\n" + "="*50)
        print("SENDING MESSAGES...")
        print("="*50)
        
        # Send messages
        agent_objects["agent1"].send_message("agent2", "Hello agent2!")
        time.sleep(1)
        
        agent_objects["agent2"].send_message("agent3", "Task assignment for you")
        time.sleep(1)
        
        agent_objects["agent1"].broadcast_message("Team meeting in 10 minutes!")
        time.sleep(2)
        
        agent_objects["agent3"].send_message("agent1", "Task completed successfully")
        time.sleep(1)
        
        agent_objects["agent2"].broadcast_message("System maintenance tonight")
        time.sleep(2)
        
        print("\n" + "="*50)
        print("NETWORK SNAPSHOTS...")
        print("="*50)
        
        # Get network snapshots from each agent's perspective
        for agent_id, agent in agent_objects.items():
            snapshot = agent.get_network_snapshot()
            print(f"\n{agent_id.upper()} SEES:")
            print(f"  Total messages: {snapshot.get('total_messages', 0)}")
            print(f"  Direct: {snapshot.get('message_types', {}).get('direct', 0)}")
            print(f"  Broadcast: {snapshot.get('message_types', {}).get('broadcast', 0)}")
            print("  Recent activity:")
            for msg in snapshot.get('recent_activity', [])[-3:]:
                print(f"    {msg}")
        
        time.sleep(2)
        
    except KeyboardInterrupt:
        print("\nInterrupted...")
    finally:
        # Cleanup
        for agent in agent_objects.values():
            agent.stop_monitoring()
        common_system.cleanup_sessions()

def show_simplified_architecture():
    """Show the simplified session architecture"""
    
    print("\n\nSIMPLIFIED SESSION ARCHITECTURE")
    print("=" * 35)
    
    agents = ["agent1", "agent2", "agent3"]
    
    print("SHARED SESSIONS:")
    print("  common_inbox   (ALL communications visible to everyone)")
    print()
    
    print("PER-AGENT SESSIONS:")
    for agent in agents:
        print(f"  {agent.upper()}:")
        print(f"    {agent}_inbox    (personal messages)")
        print(f"    {agent}_outbox   (personal sent log)")
        print(f"    {agent}_signals  (polling triggers)")
        print()
    
    print(f"TOTAL SESSIONS for {len(agents)} agents:")
    print(f"  Shared: 1 (common_inbox)")
    print(f"  Per-agent: {len(agents)} × 3 = {len(agents) * 3}")
    print(f"  TOTAL: {1 + len(agents) * 3} sessions")
    print()
    
    print("COMMUNICATION FLOW:")
    print("  1. Agent sends message to recipient's personal inbox")
    print("  2. Message ALSO logged to common_inbox")
    print("  3. ALL agents can monitor common_inbox")
    print("  4. Complete network transparency achieved!")

if __name__ == "__main__":
    demonstrate_common_inbox()
    show_simplified_architecture()
    
    print("\n\nKEY BENEFITS:")
    print("=" * 13)
    print("• Single common_inbox shows ALL network communications")
    print("• Every agent can see what everyone else is doing")
    print("• Simplified architecture with just 1 shared session")
    print("• Full transparency without complexity")
    print("• Easy debugging and network monitoring")
    print("• Agents maintain awareness of entire network state")