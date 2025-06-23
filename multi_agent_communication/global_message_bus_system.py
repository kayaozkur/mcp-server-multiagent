#!/usr/bin/env python3
"""
Global Message Bus System
Common inbox/outbox for full transparency of all agent communications
"""

import subprocess
import time
import threading
import json
import os
import tempfile
from typing import List, Dict, Set, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class GlobalMessage:
    """Message in the global message bus"""
    id: str
    sender: str
    recipient: str
    content: str
    timestamp: str
    message_type: str = "direct"  # direct, broadcast, system
    visibility: str = "public"   # public, private, restricted

class GlobalMessageBus:
    """Central message bus that tracks ALL communications"""
    
    def __init__(self, agents: List[str]):
        self.agents = agents
        self.global_inbox_session = "global_inbox"
        self.global_outbox_session = "global_outbox"
        self.global_log_session = "global_log"
        self.temp_dir = tempfile.gettempdir()
        
        # Message tracking
        self.message_counter = 0
        self.all_messages: List[GlobalMessage] = []
        
    def initialize_global_sessions(self):
        """Create the global communication sessions"""
        sessions = [
            self.global_inbox_session,
            self.global_outbox_session, 
            self.global_log_session
        ]
        
        for session in sessions:
            try:
                subprocess.run(["screen", "-dmS", session], check=True)
                subprocess.run([
                    "screen", "-S", session, "-X", "stuff",
                    f"=== {session.upper()} INITIALIZED ===\n"
                ], check=True)
                print(f"Created global session: {session}")
            except subprocess.CalledProcessError:
                print(f"Failed to create session: {session}")
    
    def cleanup_global_sessions(self):
        """Clean up global sessions"""
        sessions = [
            self.global_inbox_session,
            self.global_outbox_session,
            self.global_log_session
        ]
        
        for session in sessions:
            try:
                subprocess.run(["screen", "-S", session, "-X", "quit"], check=True)
            except subprocess.CalledProcessError:
                pass
    
    def log_message_to_global_bus(self, sender: str, recipient: str, content: str, 
                                 message_type: str = "direct"):
        """Log every message to the global message bus"""
        
        self.message_counter += 1
        timestamp = datetime.now().isoformat()
        
        # Create global message record
        global_msg = GlobalMessage(
            id=f"msg_{self.message_counter:06d}",
            sender=sender,
            recipient=recipient,
            content=content,
            timestamp=timestamp,
            message_type=message_type
        )
        
        self.all_messages.append(global_msg)
        
        # Format message for global sessions
        if message_type == "broadcast":
            log_entry = f"[{timestamp}] BROADCAST {sender} -> ALL: {content}"
        else:
            log_entry = f"[{timestamp}] {sender} -> {recipient}: {content}"
        
        # Log to global inbox (all received messages)
        try:
            subprocess.run([
                "screen", "-S", self.global_inbox_session, "-X", "stuff",
                f"{log_entry}\n"
            ], check=True)
        except subprocess.CalledProcessError:
            pass
        
        # Log to global outbox (all sent messages) 
        try:
            subprocess.run([
                "screen", "-S", self.global_outbox_session, "-X", "stuff",
                f"{log_entry}\n"
            ], check=True)
        except subprocess.CalledProcessError:
            pass
        
        # Log to global log with metadata
        try:
            metadata = f"ID:{global_msg.id} TYPE:{message_type} SENDER:{sender} RECIPIENT:{recipient}"
            subprocess.run([
                "screen", "-S", self.global_log_session, "-X", "stuff",
                f"[{timestamp}] {metadata} CONTENT:{content}\n"
            ], check=True)
        except subprocess.CalledProcessError:
            pass
        
        print(f"[GLOBAL BUS] Logged: {sender} -> {recipient}")

class TransparentAgent:
    """Agent that participates in global message bus"""
    
    def __init__(self, agent_id: str, all_agents: List[str], global_bus: GlobalMessageBus):
        self.agent_id = agent_id
        self.all_agents = all_agents
        self.global_bus = global_bus
        self.temp_dir = tempfile.gettempdir()
        
        # Agent's personal sessions
        self.inbox_session = f"{agent_id}_inbox"
        self.outbox_session = f"{agent_id}_outbox"
        self.signals_session = f"{agent_id}_signals"
        
        # Monitoring
        self.monitoring_active = False
        self.monitor_thread = None
    
    def initialize_agent_sessions(self):
        """Create agent's personal sessions"""
        sessions = [self.inbox_session, self.outbox_session, self.signals_session]
        
        for session in sessions:
            try:
                subprocess.run(["screen", "-dmS", session], check=True)
                subprocess.run([
                    "screen", "-S", session, "-X", "stuff",
                    f"=== {session.upper()} INITIALIZED ===\n"
                ], check=True)
            except subprocess.CalledProcessError:
                pass
    
    def cleanup_agent_sessions(self):
        """Clean up agent sessions"""
        sessions = [self.inbox_session, self.outbox_session, self.signals_session]
        
        for session in sessions:
            try:
                subprocess.run(["screen", "-S", session, "-X", "quit"], check=True)
            except subprocess.CalledProcessError:
                pass
    
    def send_message(self, recipient: str, content: str):
        """Send message with global bus logging"""
        
        # Send to recipient's personal inbox
        try:
            subprocess.run([
                "screen", "-S", f"{recipient}_inbox", "-X", "stuff",
                f"MSG from {self.agent_id}: {content}\n"
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
        
        # LOG TO GLOBAL MESSAGE BUS
        self.global_bus.log_message_to_global_bus(
            sender=self.agent_id,
            recipient=recipient,
            content=content,
            message_type="direct"
        )
        
        print(f"[{self.agent_id}] Sent to {recipient}: {content}")
    
    def broadcast_message(self, content: str):
        """Send broadcast with global bus logging"""
        
        recipients = [agent for agent in self.all_agents if agent != self.agent_id]
        
        # Send to all recipient inboxes
        for recipient in recipients:
            try:
                subprocess.run([
                    "screen", "-S", f"{recipient}_inbox", "-X", "stuff",
                    f"BROADCAST from {self.agent_id}: {content}\n"
                ], check=True)
                
                # Trigger immediate polling
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
        
        # LOG TO GLOBAL MESSAGE BUS
        self.global_bus.log_message_to_global_bus(
            sender=self.agent_id,
            recipient="ALL",
            content=content,
            message_type="broadcast"
        )
        
        print(f"[{self.agent_id}] Broadcast sent: {content}")
    
    def start_monitoring(self):
        """Start monitoring personal inbox and global bus"""
        self.monitoring_active = True
        self.monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        self.monitor_thread.start()
        print(f"[{self.agent_id}] Started monitoring")
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.monitoring_active = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2)
        print(f"[{self.agent_id}] Stopped monitoring")
    
    def _monitoring_loop(self):
        """Monitor personal inbox and global message bus"""
        while self.monitoring_active:
            try:
                # Monitor personal inbox
                self._check_personal_inbox()
                
                # Monitor global message bus 
                self._check_global_activity()
                
                time.sleep(2)  # Check every 2 seconds
                
            except Exception as e:
                if self.monitoring_active:
                    print(f"[{self.agent_id}] Monitoring error: {e}")
                time.sleep(1)
    
    def _check_personal_inbox(self):
        """Check personal inbox for new messages"""
        try:
            inbox_file = os.path.join(self.temp_dir, f"inbox_{self.agent_id}")
            subprocess.run([
                "screen", "-S", self.inbox_session, "-X", "hardcopy", inbox_file
            ], check=True)
            
            with open(inbox_file, 'r') as f:
                content = f.read()
            
            os.remove(inbox_file)
            
            # Process new messages
            lines = content.split('\n')
            for line in lines:
                if "MSG from" in line or "BROADCAST from" in line:
                    if line.strip() and not self._already_processed(line):
                        print(f"[{self.agent_id}] RECEIVED: {line.strip()}")
                        
        except Exception:
            pass
    
    def _check_global_activity(self):
        """Check global message bus for network activity"""
        try:
            global_file = os.path.join(self.temp_dir, f"global_{self.agent_id}")
            subprocess.run([
                "screen", "-S", self.global_bus.global_inbox_session, "-X", "hardcopy", global_file
            ], check=True)
            
            with open(global_file, 'r') as f:
                content = f.read()
            
            os.remove(global_file)
            
            # Look for recent activity (last few lines)
            lines = content.split('\n')
            recent_lines = lines[-5:] if len(lines) > 5 else lines
            
            for line in recent_lines:
                if "] " in line and (self.agent_id not in line or "BROADCAST" in line):
                    # This is network activity not involving this agent directly
                    if line.strip() and not self._already_seen_global(line):
                        print(f"[{self.agent_id}] NETWORK ACTIVITY: {line.strip()}")
                        
        except Exception:
            pass
    
    def _already_processed(self, message: str) -> bool:
        """Check if we've already processed this personal message"""
        # Simple duplicate detection based on message content
        # In real implementation, would use more sophisticated tracking
        return False
    
    def _already_seen_global(self, message: str) -> bool:
        """Check if we've already seen this global activity"""
        # Simple duplicate detection for global messages
        return False
    
    def get_global_communication_summary(self) -> Dict:
        """Get summary of all network communications"""
        try:
            # Capture global log
            log_file = os.path.join(self.temp_dir, f"global_log_{self.agent_id}")
            subprocess.run([
                "screen", "-S", self.global_bus.global_log_session, "-X", "hardcopy", log_file
            ], check=True)
            
            with open(log_file, 'r') as f:
                content = f.read()
            
            os.remove(log_file)
            
            # Parse log content
            lines = content.split('\n')
            messages = [line for line in lines if "ID:msg_" in line]
            
            return {
                "agent_id": self.agent_id,
                "total_network_messages": len(messages),
                "recent_messages": messages[-10:] if messages else [],
                "agents_active": list(set([
                    line.split("SENDER:")[1].split(" ")[0] 
                    for line in messages 
                    if "SENDER:" in line
                ]))
            }
            
        except Exception:
            return {"agent_id": self.agent_id, "error": "Failed to get summary"}

def demonstrate_global_message_bus():
    """Demonstrate the global message bus system"""
    
    print("GLOBAL MESSAGE BUS SYSTEM")
    print("=" * 30)
    
    agents = ["agent1", "agent2", "agent3", "agent4"]
    
    # Create global message bus
    global_bus = GlobalMessageBus(agents)
    global_bus.initialize_global_sessions()
    
    # Create transparent agents
    transparent_agents = {}
    for agent_id in agents:
        agent = TransparentAgent(agent_id, agents, global_bus)
        agent.initialize_agent_sessions()
        transparent_agents[agent_id] = agent
    
    try:
        # Start monitoring for all agents
        for agent in transparent_agents.values():
            agent.start_monitoring()
        
        time.sleep(2)  # Let monitoring stabilize
        
        print("\n" + "="*50)
        print("SENDING MESSAGES WITH GLOBAL TRACKING...")
        print("="*50)
        
        # Send various messages
        transparent_agents["agent1"].send_message("agent2", "Hello agent2, how are you?")
        time.sleep(1)
        
        transparent_agents["agent2"].send_message("agent3", "Agent3, please start processing")
        time.sleep(1)
        
        transparent_agents["agent1"].broadcast_message("Team meeting in 5 minutes!")
        time.sleep(2)
        
        transparent_agents["agent3"].send_message("agent1", "Processing complete")
        time.sleep(1)
        
        transparent_agents["agent4"].broadcast_message("System status: All normal")
        time.sleep(2)
        
        print("\n" + "="*50)
        print("GLOBAL COMMUNICATION SUMMARIES...")
        print("="*50)
        
        # Get communication summaries
        for agent_id, agent in transparent_agents.items():
            summary = agent.get_global_communication_summary()
            print(f"\n{agent_id.upper()} PERSPECTIVE:")
            print(f"  Total network messages seen: {summary.get('total_network_messages', 0)}")
            print(f"  Active agents: {', '.join(summary.get('agents_active', []))}")
            if summary.get('recent_messages'):
                print("  Recent activity:")
                for msg in summary['recent_messages'][-3:]:
                    print(f"    {msg}")
        
        print("\nLetting system process messages...")
        time.sleep(3)
        
    except KeyboardInterrupt:
        print("\nInterrupted...")
    finally:
        # Cleanup
        for agent in transparent_agents.values():
            agent.stop_monitoring()
            agent.cleanup_agent_sessions()
        
        global_bus.cleanup_global_sessions()

def show_session_architecture():
    """Show the complete session architecture with global bus"""
    
    print("\n\nCOMPLETE SESSION ARCHITECTURE")
    print("=" * 35)
    
    agents = ["agent1", "agent2", "agent3"]
    
    print("GLOBAL SESSIONS (shared by all):")
    print("  global_inbox   (all received messages)")
    print("  global_outbox  (all sent messages)")
    print("  global_log     (detailed message metadata)")
    print()
    
    print("PER-AGENT SESSIONS:")
    for agent in agents:
        print(f"  {agent.upper()}:")
        print(f"    {agent}_inbox    (personal messages)")
        print(f"    {agent}_outbox   (personal sent log)")
        print(f"    {agent}_signals  (polling triggers)")
        print()
    
    print(f"TOTAL SESSIONS for {len(agents)} agents:")
    print(f"  Global sessions: 3")
    print(f"  Per-agent sessions: {len(agents)} × 3 = {len(agents) * 3}")
    print(f"  TOTAL: {3 + len(agents) * 3} sessions")
    print()
    
    print("MESSAGE FLOW:")
    print("  1. Agent sends message")
    print("  2. Message goes to recipient's personal inbox")
    print("  3. Message logged to global_inbox")
    print("  4. Message logged to global_outbox") 
    print("  5. Detailed metadata logged to global_log")
    print("  6. ALL agents can observe network activity")

if __name__ == "__main__":
    demonstrate_global_message_bus()
    show_session_architecture()
    
    print("\n\nKEY BENEFITS:")
    print("=" * 13)
    print("• Complete transparency - all agents see all communications")
    print("• Global message bus tracks every message sent/received")
    print("• Agents can monitor network activity in real-time")
    print("• Debugging and auditing capabilities built-in")
    print("• Network-wide communication patterns visible")
    print("• Central logging for compliance and analysis")