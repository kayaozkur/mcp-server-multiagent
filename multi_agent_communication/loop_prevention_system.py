#!/usr/bin/env python3
"""
Loop Prevention and Message State Management
Shows how to prevent infinite ping-pong loops between agents
"""

import json
import time
import hashlib
from datetime import datetime, timedelta
from typing import Set, Dict, Optional
from dataclasses import dataclass

@dataclass
class MessageState:
    """Track message processing state to prevent loops"""
    message_id: str
    content_hash: str
    sender: str
    recipient: str
    timestamp: datetime
    processed: bool = False
    responded: bool = False
    response_count: int = 0
    
class LoopPreventionManager:
    """Prevents infinite loops and ping-pong conversations"""
    
    def __init__(self, agent_id: str, max_responses: int = 1, 
                 message_ttl_minutes: int = 30):
        self.agent_id = agent_id
        self.max_responses = max_responses
        self.message_ttl = timedelta(minutes=message_ttl_minutes)
        
        # Track processed messages
        self.processed_messages: Dict[str, MessageState] = {}
        self.content_hashes: Set[str] = set()
        self.conversation_threads: Dict[str, int] = {}  # thread_id -> message_count
        
    def should_process_message(self, message_content: str, sender: str) -> bool:
        """Determine if a message should be processed or ignored"""
        
        # Create content hash to detect duplicates
        content_hash = hashlib.md5(message_content.encode()).hexdigest()
        
        # Check for exact duplicate content
        if content_hash in self.content_hashes:
            print(f"[{self.agent_id}] IGNORED: Duplicate content from {sender}")
            return False
        
        # Check for ping-pong patterns
        thread_id = f"{sender}-{self.agent_id}"
        current_count = self.conversation_threads.get(thread_id, 0)
        
        if current_count >= self.max_responses:
            print(f"[{self.agent_id}] IGNORED: Max responses reached with {sender}")
            return False
        
        # Check for echo patterns (agent responding to own message)
        if sender == self.agent_id:
            print(f"[{self.agent_id}] IGNORED: Own message echo")
            return False
        
        return True
    
    def record_processed_message(self, message_content: str, sender: str, 
                                message_id: str = None) -> MessageState:
        """Record that a message has been processed"""
        
        if not message_id:
            message_id = f"{sender}-{int(time.time())}"
        
        content_hash = hashlib.md5(message_content.encode()).hexdigest()
        
        message_state = MessageState(
            message_id=message_id,
            content_hash=content_hash,
            sender=sender,
            recipient=self.agent_id,
            timestamp=datetime.now(),
            processed=True
        )
        
        self.processed_messages[message_id] = message_state
        self.content_hashes.add(content_hash)
        
        # Update conversation thread count
        thread_id = f"{sender}-{self.agent_id}"
        self.conversation_threads[thread_id] = self.conversation_threads.get(thread_id, 0) + 1
        
        return message_state
    
    def should_respond(self, message_state: MessageState) -> bool:
        """Determine if agent should respond to a message"""
        
        # Check if already responded
        if message_state.responded:
            return False
        
        # Check response limits
        thread_id = f"{message_state.sender}-{self.agent_id}"
        if self.conversation_threads.get(thread_id, 0) >= self.max_responses:
            return False
        
        # Check for automatic response triggers that should be ignored
        auto_responses = ["ACK", "OK", "RECEIVED", "CONFIRMED"]
        if any(trigger in message_state.content_hash for trigger in auto_responses):
            return False
        
        return True
    
    def record_response_sent(self, original_message_id: str, response_content: str):
        """Record that a response was sent"""
        
        if original_message_id in self.processed_messages:
            self.processed_messages[original_message_id].responded = True
            self.processed_messages[original_message_id].response_count += 1
    
    def cleanup_old_messages(self):
        """Remove old message states to prevent memory bloat"""
        
        current_time = datetime.now()
        expired_messages = []
        
        for msg_id, msg_state in self.processed_messages.items():
            if current_time - msg_state.timestamp > self.message_ttl:
                expired_messages.append(msg_id)
        
        for msg_id in expired_messages:
            msg_state = self.processed_messages.pop(msg_id)
            self.content_hashes.discard(msg_state.content_hash)
        
        print(f"[{self.agent_id}] Cleaned up {len(expired_messages)} expired messages")

class SmartAgentNode:
    """Agent with loop prevention and intelligent response logic"""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.loop_prevention = LoopPreventionManager(agent_id, max_responses=2)
        self.response_patterns = {
            "greeting": ["hello", "hi", "hey"],
            "question": ["?", "what", "how", "why", "when", "where"],
            "command": ["do", "execute", "run", "start", "stop"],
            "acknowledgment": ["ack", "ok", "received", "got it"]
        }
    
    def process_incoming_message(self, message_content: str, sender: str) -> Optional[str]:
        """Process incoming message with loop prevention"""
        
        # First check: Should we process this message at all?
        if not self.loop_prevention.should_process_message(message_content, sender):
            return None
        
        # Record the message as processed
        message_state = self.loop_prevention.record_processed_message(
            message_content, sender
        )
        
        # Determine message type and appropriate response
        response = self._generate_intelligent_response(message_content, sender)
        
        # Check if we should actually send the response
        if response and self.loop_prevention.should_respond(message_state):
            self.loop_prevention.record_response_sent(message_state.message_id, response)
            return response
        
        return None
    
    def _generate_intelligent_response(self, message_content: str, sender: str) -> Optional[str]:
        """Generate contextually appropriate response"""
        
        content_lower = message_content.lower()
        
        # Don't respond to acknowledgments
        if any(ack in content_lower for ack in self.response_patterns["acknowledgment"]):
            return None
        
        # Respond to greetings (but only once per sender)
        if any(greeting in content_lower for greeting in self.response_patterns["greeting"]):
            thread_id = f"{sender}-{self.agent_id}"
            if self.loop_prevention.conversation_threads.get(thread_id, 0) == 0:
                return f"Hello {sender}! How can I help you?"
            else:
                return None  # Don't keep saying hello
        
        # Respond to questions
        if any(q in content_lower for q in self.response_patterns["question"]):
            return f"I understand your question. Let me process that..."
        
        # Respond to commands
        if any(cmd in content_lower for cmd in self.response_patterns["command"]):
            return f"Command received. Processing..."
        
        # Default response for other messages
        return f"Message acknowledged."

def demonstrate_loop_prevention():
    """Show how loop prevention works"""
    
    print("LOOP PREVENTION DEMONSTRATION")
    print("=" * 40)
    
    # Create two agents
    agent1 = SmartAgentNode("agent1")
    agent2 = SmartAgentNode("agent2")
    
    print("\nSimulating conversation between agent1 and agent2:")
    print("-" * 50)
    
    # Simulate message exchange
    messages = [
        ("agent1", "agent2", "Hello agent2!"),
        ("agent2", "agent1", "Hello agent1! How can I help you?"),
        ("agent1", "agent2", "Hello agent2!"),  # Duplicate - should be ignored
        ("agent2", "agent1", "What's the weather like?"),
        ("agent1", "agent2", "I understand your question. Let me process that..."),
        ("agent2", "agent1", "What's the weather like?"),  # Duplicate - should be ignored
        ("agent1", "agent2", "ACK"),  # Should not generate response
        ("agent2", "agent1", "ACK"),  # Should not generate response
    ]
    
    for sender, recipient, message in messages:
        print(f"\n{sender} -> {recipient}: '{message}'")
        
        if recipient == "agent1":
            response = agent1.process_incoming_message(message, sender)
        else:
            response = agent2.process_incoming_message(message, sender)
        
        if response:
            print(f"  {recipient} responds: '{response}'")
        else:
            print(f"  {recipient}: [No response - loop prevention]")

def show_problematic_scenarios():
    """Show scenarios that would cause loops without prevention"""
    
    print("\n\nPROBLEMATIC SCENARIOS WITHOUT LOOP PREVENTION")
    print("=" * 50)
    
    scenarios = [
        {
            "name": "Ping-Pong Loop",
            "description": "Agents keep greeting each other infinitely",
            "messages": [
                "agent1 -> agent2: Hello!",
                "agent2 -> agent1: Hello back!",
                "agent1 -> agent2: Hello!",
                "agent2 -> agent1: Hello back!",
                "... INFINITE LOOP ..."
            ]
        },
        {
            "name": "Echo Chamber",
            "description": "Agents repeat the same information",
            "messages": [
                "agent1 -> agent2: The meeting is at 3pm",
                "agent2 -> agent3: The meeting is at 3pm",
                "agent3 -> agent1: The meeting is at 3pm",
                "agent1 -> agent2: The meeting is at 3pm",
                "... INFINITE LOOP ..."
            ]
        },
        {
            "name": "Question Loop",
            "description": "Agents keep asking the same question",
            "messages": [
                "agent1 -> agent2: What's the status?",
                "agent2 -> agent1: I don't know, what's the status?", 
                "agent1 -> agent2: What's the status?",
                "... INFINITE LOOP ..."
            ]
        }
    ]
    
    for scenario in scenarios:
        print(f"\n{scenario['name']}:")
        print(f"Description: {scenario['description']}")
        print("Message flow:")
        for message in scenario['messages']:
            print(f"  {message}")

if __name__ == "__main__":
    demonstrate_loop_prevention()
    show_problematic_scenarios()
    
    print("\n\nKEY PREVENTION MECHANISMS:")
    print("=" * 35)
    print("1. Content Hash Deduplication - Ignore exact duplicates")
    print("2. Response Limits - Max responses per conversation thread")
    print("3. Echo Detection - Don't respond to own messages")
    print("4. Acknowledgment Filtering - Don't respond to ACK/OK messages")
    print("5. Message TTL - Clean up old conversation state")
    print("6. Intelligent Response Logic - Context-aware responses")