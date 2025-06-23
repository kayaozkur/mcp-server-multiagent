#!/usr/bin/env python3
"""
Multi-Agent Screen Communication Network
Enables bidirectional, non-linear communication between multiple agents using screen sessions
"""

import subprocess
import time
import os
import json
import threading
import tempfile
from typing import Dict, List, Optional, Callable, Any
from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class Message:
    """Represents a message in the communication network"""
    id: str
    sender: str
    recipient: str
    content: str
    timestamp: str
    message_type: str = "text"
    metadata: Dict[str, Any] = None
    
    def to_json(self) -> str:
        return json.dumps({
            'id': self.id,
            'sender': self.sender,
            'recipient': self.recipient,
            'content': self.content,
            'timestamp': self.timestamp,
            'message_type': self.message_type,
            'metadata': self.metadata or {}
        })
    
    @classmethod
    def from_json(cls, json_str: str) -> 'Message':
        data = json.loads(json_str)
        return cls(**data)

class AgentCommunicationNode:
    """Individual agent node in the communication network"""
    
    def __init__(self, agent_id: str, network_manager: 'MultiAgentNetworkManager'):
        self.agent_id = agent_id
        self.network_manager = network_manager
        self.inbox_session = f"{agent_id}_inbox"
        self.outbox_session = f"{agent_id}_outbox"
        self.message_handlers: Dict[str, Callable] = {}
        self.running = False
        self.listener_thread = None
        self.temp_dir = tempfile.gettempdir()
        
    def start(self):
        """Start the agent communication node"""
        self._create_sessions()
        self.running = True
        self.listener_thread = threading.Thread(target=self._message_listener, daemon=True)
        self.listener_thread.start()
        print(f"Agent {self.agent_id} communication node started")
    
    def stop(self):
        """Stop the agent communication node"""
        self.running = False
        if self.listener_thread:
            self.listener_thread.join(timeout=2)
        self._cleanup_sessions()
        print(f"Agent {self.agent_id} communication node stopped")
    
    def _create_sessions(self):
        """Create inbox and outbox screen sessions"""
        for session in [self.inbox_session, self.outbox_session]:
            try:
                subprocess.run(["screen", "-dmS", session], check=True)
                # Initialize with a marker
                subprocess.run([
                    "screen", "-S", session, "-X", "stuff", 
                    f"echo 'Session {session} initialized'\n"
                ], check=True)
            except subprocess.CalledProcessError:
                pass
    
    def _cleanup_sessions(self):
        """Clean up screen sessions"""
        for session in [self.inbox_session, self.outbox_session]:
            try:
                subprocess.run(["screen", "-S", session, "-X", "quit"], check=True)
            except subprocess.CalledProcessError:
                pass
    
    def send_message(self, recipient: str, content: str, message_type: str = "text", metadata: Dict = None):
        """Send a message to another agent"""
        message = Message(
            id=str(uuid.uuid4()),
            sender=self.agent_id,
            recipient=recipient,
            content=content,
            timestamp=datetime.now().isoformat(),
            message_type=message_type,
            metadata=metadata
        )
        
        # Send to recipient's inbox
        recipient_inbox = f"{recipient}_inbox"
        try:
            # Write message as JSON to the recipient's inbox session
            subprocess.run([
                "screen", "-S", recipient_inbox, "-X", "stuff",
                f"echo 'MSG:{message.to_json()}'\n"
            ], check=True)
            
            # Log in our outbox
            subprocess.run([
                "screen", "-S", self.outbox_session, "-X", "stuff",
                f"echo 'SENT:{message.to_json()}'\n"
            ], check=True)
            
            return True
        except subprocess.CalledProcessError:
            return False
    
    def broadcast_message(self, content: str, message_type: str = "broadcast", metadata: Dict = None):
        """Send a message to all other agents in the network"""
        other_agents = [agent_id for agent_id in self.network_manager.agents.keys() 
                       if agent_id != self.agent_id]
        
        for recipient in other_agents:
            self.send_message(recipient, content, message_type, metadata)
    
    def _message_listener(self):
        """Background thread to listen for incoming messages"""
        while self.running:
            try:
                # Capture inbox content
                output_file = os.path.join(self.temp_dir, f"inbox_{self.agent_id}_output")
                subprocess.run([
                    "screen", "-S", self.inbox_session, "-X", "hardcopy", output_file
                ], check=True)
                
                # Read and parse messages
                with open(output_file, 'r') as f:
                    content = f.read()
                
                os.remove(output_file)
                
                # Parse messages from content
                self._process_inbox_content(content)
                
            except Exception as e:
                if self.running:  # Only log if we're supposed to be running
                    print(f"Error in message listener for {self.agent_id}: {e}")
            
            time.sleep(1)  # Check for messages every second
    
    def _process_inbox_content(self, content: str):
        """Process messages from inbox content"""
        lines = content.split('\n')
        for line in lines:
            if line.startswith('MSG:'):
                try:
                    json_str = line[4:]  # Remove 'MSG:' prefix
                    message = Message.from_json(json_str)
                    self._handle_message(message)
                except (json.JSONDecodeError, Exception) as e:
                    print(f"Error parsing message in {self.agent_id}: {e}")
    
    def _handle_message(self, message: Message):
        """Handle an incoming message"""
        handler = self.message_handlers.get(message.message_type)
        if handler:
            try:
                handler(message)
            except Exception as e:
                print(f"Error handling message in {self.agent_id}: {e}")
        else:
            # Default handler
            print(f"[{self.agent_id}] Received from {message.sender}: {message.content}")
    
    def register_message_handler(self, message_type: str, handler: Callable[[Message], None]):
        """Register a handler for a specific message type"""
        self.message_handlers[message_type] = handler
    
    def get_conversation_history(self) -> List[str]:
        """Get the conversation history from both inbox and outbox"""
        history = []
        
        for session in [self.inbox_session, self.outbox_session]:
            try:
                output_file = os.path.join(self.temp_dir, f"history_{session}_output")
                subprocess.run([
                    "screen", "-S", session, "-X", "hardcopy", output_file
                ], check=True)
                
                with open(output_file, 'r') as f:
                    content = f.read()
                
                os.remove(output_file)
                history.append(f"=== {session} ===")
                history.append(content)
                
            except Exception:
                pass
        
        return history

class MultiAgentNetworkManager:
    """Manages a network of communicating agents"""
    
    def __init__(self):
        self.agents: Dict[str, AgentCommunicationNode] = {}
        self.user_node: Optional[AgentCommunicationNode] = None
        self.network_monitor_running = False
        self.monitor_thread = None
    
    def add_agent(self, agent_id: str) -> AgentCommunicationNode:
        """Add an agent to the network"""
        if agent_id in self.agents:
            raise ValueError(f"Agent {agent_id} already exists")
        
        node = AgentCommunicationNode(agent_id, self)
        self.agents[agent_id] = node
        return node
    
    def add_user(self, user_id: str = "user") -> AgentCommunicationNode:
        """Add a user node to the network"""
        self.user_node = AgentCommunicationNode(user_id, self)
        return self.user_node
    
    def start_network(self):
        """Start all agents in the network"""
        if self.user_node:
            self.user_node.start()
        
        for agent in self.agents.values():
            agent.start()
        
        self._start_network_monitor()
        print(f"Network started with {len(self.agents)} agents" + 
              (" and 1 user" if self.user_node else ""))
    
    def stop_network(self):
        """Stop all agents in the network"""
        self.network_monitor_running = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2)
        
        if self.user_node:
            self.user_node.stop()
        
        for agent in self.agents.values():
            agent.stop()
        
        print("Network stopped")
    
    def _start_network_monitor(self):
        """Start network monitoring thread"""
        self.network_monitor_running = True
        self.monitor_thread = threading.Thread(target=self._network_monitor, daemon=True)
        self.monitor_thread.start()
    
    def _network_monitor(self):
        """Monitor network health and statistics"""
        while self.network_monitor_running:
            # Could implement network health checks, message statistics, etc.
            time.sleep(10)
    
    def get_network_status(self) -> Dict[str, Any]:
        """Get status of all nodes in the network"""
        status = {
            'agents': {},
            'user': None,
            'total_agents': len(self.agents),
            'network_running': self.network_monitor_running
        }
        
        for agent_id, agent in self.agents.items():
            status['agents'][agent_id] = {
                'running': agent.running,
                'inbox_session': agent.inbox_session,
                'outbox_session': agent.outbox_session
            }
        
        if self.user_node:
            status['user'] = {
                'id': self.user_node.agent_id,
                'running': self.user_node.running
            }
        
        return status
    
    def broadcast_to_all(self, sender_id: str, message: str):
        """Broadcast a message from one node to all others"""
        if sender_id in self.agents:
            self.agents[sender_id].broadcast_message(message)
        elif self.user_node and sender_id == self.user_node.agent_id:
            self.user_node.broadcast_message(message)

def create_example_network():
    """Create an example network with different configurations"""
    
    def create_2_agent_network():
        """2 agents + user network"""
        network = MultiAgentNetworkManager()
        
        # Add user
        user = network.add_user()
        
        # Add agents
        agent1 = network.add_agent("agent1")
        agent2 = network.add_agent("agent2")
        
        # Set up message handlers
        def agent1_handler(message: Message):
            print(f"[AGENT1] Got message from {message.sender}: {message.content}")
            if message.sender != "agent1":
                agent1.send_message(message.sender, f"Agent1 acknowledges: {message.content}")
        
        def agent2_handler(message: Message):
            print(f"[AGENT2] Got message from {message.sender}: {message.content}")
            if message.sender != "agent2":
                agent2.send_message(message.sender, f"Agent2 processed: {message.content}")
        
        agent1.register_message_handler("text", agent1_handler)
        agent2.register_message_handler("text", agent2_handler)
        
        return network, user, [agent1, agent2]
    
    def create_4_agent_mesh_network():
        """4 agents in full mesh communication"""
        network = MultiAgentNetworkManager()
        
        # Add user
        user = network.add_user()
        
        # Add 4 agents
        agents = []
        for i in range(1, 5):
            agent = network.add_agent(f"agent{i}")
            agents.append(agent)
            
            # Each agent responds to messages from others
            def make_handler(agent_id):
                def handler(message: Message):
                    print(f"[{agent_id.upper()}] Received from {message.sender}: {message.content}")
                    # Respond to sender
                    if message.sender != agent_id:
                        agent = network.agents[agent_id]
                        agent.send_message(message.sender, 
                                         f"{agent_id} processed your message: '{message.content[:20]}...'")
                return handler
            
            agent.register_message_handler("text", make_handler(f"agent{i}"))
        
        return network, user, agents
    
    return create_2_agent_network, create_4_agent_mesh_network

if __name__ == "__main__":
    # Example usage
    print("Multi-Agent Screen Communication Network")
    print("=" * 50)
    
    # Create a 2-agent network
    create_2_agent, create_4_agent = create_example_network()
    network, user, agents = create_2_agent()
    
    try:
        # Start the network
        network.start_network()
        time.sleep(2)
        
        # Send some test messages
        print("\nSending test messages...")
        user.send_message("agent1", "Hello from user!")
        time.sleep(1)
        
        agents[0].send_message("agent2", "Hello from agent1!")
        time.sleep(1)
        
        agents[1].send_message("agent1", "Hello back from agent2!")
        time.sleep(2)
        
        # Show network status
        print("\nNetwork Status:")
        print(json.dumps(network.get_network_status(), indent=2))
        
        # Keep running for a bit to see communication
        print("\nNetwork running... Press Ctrl+C to stop")
        time.sleep(10)
        
    except KeyboardInterrupt:
        print("\nStopping network...")
    finally:
        network.stop_network()