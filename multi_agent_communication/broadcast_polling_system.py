#!/usr/bin/env python3
"""
Broadcast Polling System
Implements immediate polling triggers when broadcast messages are sent
"""

import subprocess
import time
import threading
import json
import os
from typing import List, Dict, Set, Callable
from dataclasses import dataclass
from datetime import datetime
import tempfile

@dataclass
class BroadcastMessage:
    """Represents a broadcast message that triggers immediate polling"""
    id: str
    sender: str
    content: str
    timestamp: str
    priority: str = "normal"  # normal, urgent, critical
    requires_acknowledgment: bool = False
    recipients: List[str] = None

class BroadcastPollManager:
    """Manages polling triggers for broadcast messages"""
    
    def __init__(self, agent_id: str, all_agents: List[str]):
        self.agent_id = agent_id
        self.all_agents = all_agents
        self.polling_active = False
        self.normal_poll_interval = 5.0  # Normal polling every 5 seconds
        self.urgent_poll_interval = 0.5  # Urgent polling every 0.5 seconds
        self.current_poll_interval = self.normal_poll_interval
        
        # Polling control
        self.poll_thread = None
        self.poll_triggers: Set[str] = set()  # Pending poll triggers
        self.broadcast_handlers: Dict[str, Callable] = {}
        
        # Signal mechanisms
        self.signal_session = f"{agent_id}_signals"
        self.temp_dir = tempfile.gettempdir()
        
    def start_polling(self):
        """Start the adaptive polling system"""
        self.polling_active = True
        self._create_signal_session()
        
        self.poll_thread = threading.Thread(target=self._adaptive_polling_loop, daemon=True)
        self.poll_thread.start()
        print(f"[{self.agent_id}] Adaptive polling started")
    
    def stop_polling(self):
        """Stop the polling system"""
        self.polling_active = False
        if self.poll_thread:
            self.poll_thread.join(timeout=2)
        self._cleanup_signal_session()
        print(f"[{self.agent_id}] Polling stopped")
    
    def _create_signal_session(self):
        """Create a dedicated session for polling signals"""
        try:
            subprocess.run(["screen", "-dmS", self.signal_session], check=True)
            subprocess.run([
                "screen", "-S", self.signal_session, "-X", "stuff",
                f"echo 'Signal session for {self.agent_id} initialized'\n"
            ], check=True)
        except subprocess.CalledProcessError:
            pass
    
    def _cleanup_signal_session(self):
        """Clean up the signal session"""
        try:
            subprocess.run(["screen", "-S", self.signal_session, "-X", "quit"], check=True)
        except subprocess.CalledProcessError:
            pass
    
    def trigger_immediate_poll(self, reason: str = "broadcast"):
        """Trigger immediate polling for this agent"""
        try:
            # Send signal to own signal session
            subprocess.run([
                "screen", "-S", self.signal_session, "-X", "stuff",
                f"POLL_TRIGGER:{reason}:{datetime.now().isoformat()}\n"
            ], check=True)
            
            print(f"[{self.agent_id}] Poll trigger sent: {reason}")
        except subprocess.CalledProcessError:
            print(f"[{self.agent_id}] Failed to send poll trigger")
    
    def _adaptive_polling_loop(self):
        """Main polling loop with adaptive intervals"""
        while self.polling_active:
            try:
                # Check for poll triggers first
                self._check_poll_triggers()
                
                # Perform inbox polling
                self._poll_inbox()
                
                # Sleep for current interval
                time.sleep(self.current_poll_interval)
                
            except Exception as e:
                print(f"[{self.agent_id}] Polling error: {e}")
                time.sleep(1)
    
    def _check_poll_triggers(self):
        """Check for immediate poll triggers"""
        try:
            # Capture signal session
            signal_file = os.path.join(self.temp_dir, f"signals_{self.agent_id}")
            subprocess.run([
                "screen", "-S", self.signal_session, "-X", "hardcopy", signal_file
            ], check=True)
            
            with open(signal_file, 'r') as f:
                content = f.read()
            
            os.remove(signal_file)
            
            # Look for poll triggers
            lines = content.split('\n')
            for line in lines:
                if "POLL_TRIGGER:" in line:
                    parts = line.split("POLL_TRIGGER:")[1].split(":")
                    if parts:
                        reason = parts[0]
                        print(f"[{self.agent_id}] Processing poll trigger: {reason}")
                        
                        # Adjust polling speed based on reason
                        if reason in ["broadcast", "urgent"]:
                            self._switch_to_urgent_polling()
                        
                        # Clear the trigger by restarting session
                        self._clear_signal_session()
                        
        except Exception as e:
            pass  # Signal checking is best-effort
    
    def _switch_to_urgent_polling(self):
        """Switch to urgent polling mode temporarily"""
        self.current_poll_interval = self.urgent_poll_interval
        print(f"[{self.agent_id}] Switched to urgent polling (0.5s)")
        
        # Set timer to return to normal polling
        def reset_polling():
            time.sleep(10)  # Stay in urgent mode for 10 seconds
            self.current_poll_interval = self.normal_poll_interval
            print(f"[{self.agent_id}] Returned to normal polling (5s)")
        
        threading.Thread(target=reset_polling, daemon=True).start()
    
    def _clear_signal_session(self):
        """Clear the signal session content"""
        try:
            subprocess.run([
                "screen", "-S", self.signal_session, "-X", "stuff", "clear\n"
            ], check=True)
        except subprocess.CalledProcessError:
            pass
    
    def _poll_inbox(self):
        """Poll the agent's inbox for new messages"""
        try:
            inbox_file = os.path.join(self.temp_dir, f"inbox_{self.agent_id}")
            subprocess.run([
                "screen", "-S", f"{self.agent_id}_inbox", "-X", "hardcopy", inbox_file
            ], check=True)
            
            with open(inbox_file, 'r') as f:
                content = f.read()
            
            os.remove(inbox_file)
            
            # Process new messages
            self._process_inbox_content(content)
            
        except Exception as e:
            pass  # Inbox polling is best-effort
    
    def _process_inbox_content(self, content: str):
        """Process inbox content and handle broadcasts"""
        lines = content.split('\n')
        for line in lines:
            if "BROADCAST:" in line:
                print(f"[{self.agent_id}] Received broadcast: {line}")
                # Handle broadcast message
                self._handle_broadcast_message(line)
            elif "MSG from" in line:
                print(f"[{self.agent_id}] Received message: {line}")
    
    def _handle_broadcast_message(self, message: str):
        """Handle a broadcast message"""
        # Extract sender and content
        if "MSG from" in message and "BROADCAST:" in message:
            try:
                parts = message.split("MSG from ")[1].split(": BROADCAST: ")
                sender = parts[0]
                content = parts[1] if len(parts) > 1 else ""
                
                # Call registered handlers
                for handler_name, handler in self.broadcast_handlers.items():
                    try:
                        handler(sender, content)
                    except Exception as e:
                        print(f"[{self.agent_id}] Handler error: {e}")
                        
            except Exception as e:
                print(f"[{self.agent_id}] Failed to parse broadcast: {e}")
    
    def register_broadcast_handler(self, name: str, handler: Callable[[str, str], None]):
        """Register a handler for broadcast messages"""
        self.broadcast_handlers[name] = handler

class BroadcastSystem:
    """System for managing broadcasts and polling triggers"""
    
    def __init__(self, agents: List[str]):
        self.agents = agents
        self.poll_managers: Dict[str, BroadcastPollManager] = {}
        
        # Create poll managers for each agent
        for agent in agents:
            self.poll_managers[agent] = BroadcastPollManager(agent, agents)
    
    def start_system(self):
        """Start the broadcast system for all agents"""
        print("Starting broadcast system...")
        
        # Create screen sessions
        for agent in self.agents:
            try:
                subprocess.run(["screen", "-dmS", f"{agent}_inbox"], check=True)
                subprocess.run(["screen", "-dmS", f"{agent}_outbox"], check=True)
            except subprocess.CalledProcessError:
                pass
        
        # Start polling for all agents
        for agent, manager in self.poll_managers.items():
            manager.start_polling()
            
            # Register default broadcast handler
            def make_handler(agent_id):
                def handler(sender, content):
                    print(f"[{agent_id}] BROADCAST RECEIVED from {sender}: {content}")
                    # Could trigger acknowledgment, logging, etc.
                return handler
            
            manager.register_broadcast_handler("default", make_handler(agent))
        
        print("Broadcast system started!")
    
    def stop_system(self):
        """Stop the broadcast system"""
        print("Stopping broadcast system...")
        
        for manager in self.poll_managers.values():
            manager.stop_polling()
        
        # Clean up sessions
        for agent in self.agents:
            try:
                subprocess.run(["screen", "-S", f"{agent}_inbox", "-X", "quit"], check=True)
                subprocess.run(["screen", "-S", f"{agent}_outbox", "-X", "quit"], check=True)
            except subprocess.CalledProcessError:
                pass
        
        print("Broadcast system stopped!")
    
    def send_broadcast(self, sender: str, message: str, priority: str = "normal"):
        """Send a broadcast message and trigger immediate polling"""
        if sender not in self.agents:
            print(f"Unknown sender: {sender}")
            return
        
        print(f"\n[BROADCAST] {sender} -> ALL: {message}")
        
        recipients = [agent for agent in self.agents if agent != sender]
        
        # Send message to all recipient inboxes
        for recipient in recipients:
            try:
                subprocess.run([
                    "screen", "-S", f"{recipient}_inbox", "-X", "stuff",
                    f"MSG from {sender}: BROADCAST: {message}\n"
                ], check=True)
                
                print(f"  -> Delivered to {recipient}")
                
            except subprocess.CalledProcessError:
                print(f"  -> Failed to deliver to {recipient}")
        
        # Log in sender's outbox
        try:
            subprocess.run([
                "screen", "-S", f"{sender}_outbox", "-X", "stuff",
                f"BROADCAST SENT to {len(recipients)} agents: {message}\n"
            ], check=True)
        except subprocess.CalledProcessError:
            pass
        
        # Trigger immediate polling for all recipients
        for recipient in recipients:
            if recipient in self.poll_managers:
                self.poll_managers[recipient].trigger_immediate_poll("broadcast")
        
        print(f"[BROADCAST] Poll triggers sent to {len(recipients)} agents")

def demonstrate_broadcast_system():
    """Demonstrate the broadcast polling system"""
    
    print("BROADCAST POLLING SYSTEM DEMONSTRATION")
    print("=" * 42)
    
    agents = ["agent1", "agent2", "agent3", "agent4"]
    broadcast_system = BroadcastSystem(agents)
    
    try:
        # Start the system
        broadcast_system.start_system()
        time.sleep(2)  # Let polling stabilize
        
        print("\n" + "="*50)
        print("SENDING BROADCASTS...")
        print("="*50)
        
        # Send some broadcasts
        broadcast_system.send_broadcast("agent1", "Emergency meeting at 3 PM!", "urgent")
        time.sleep(3)
        
        broadcast_system.send_broadcast("agent2", "System maintenance scheduled for tonight", "normal")
        time.sleep(3)
        
        broadcast_system.send_broadcast("agent3", "CRITICAL: Security breach detected!", "critical")
        time.sleep(3)
        
        print("\nLetting system process broadcasts...")
        time.sleep(5)
        
    except KeyboardInterrupt:
        print("\nInterrupted...")
    finally:
        broadcast_system.stop_system()

if __name__ == "__main__":
    demonstrate_broadcast_system()
    
    print("\n\nKEY FEATURES:")
    print("=" * 15)
    print("• Immediate poll triggers for broadcast recipients")
    print("• Adaptive polling intervals (normal 5s, urgent 0.5s)")
    print("• Dedicated signal sessions for polling control")
    print("• Automatic return to normal polling after urgent period")
    print("• Broadcast handlers for custom message processing")
    print("• Priority-based polling speed adjustments")