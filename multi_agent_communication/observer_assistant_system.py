#!/usr/bin/env python3
"""
Observer/Assistant Agent System
Different participation levels: Active, Observer, Assistant, Silent
"""

from enum import Enum
from typing import Dict, List, Set
from dataclasses import dataclass

class ParticipationLevel(Enum):
    ACTIVE = "active"           # Full participation - can send/receive/broadcast
    OBSERVER = "observer"       # Can see all, cannot send broadcasts, limited replies
    ASSISTANT = "assistant"     # Can see specific topics, can respond when needed
    SILENT = "silent"          # Can see all, cannot send anything
    SUPPORT = "support"        # Can see context, can provide help when requested

class AgentRole(Enum):
    # Core roles
    USER = "user"
    MANAGER = "manager"
    DEVELOPER = "developer"
    
    # Support roles  
    DESIGNER = "designer"
    QA_TESTER = "qa_tester"
    DEVOPS = "devops"
    ANALYST = "analyst"
    ASSISTANT = "assistant"

@dataclass
class Agent:
    id: str
    role: AgentRole
    participation_level: ParticipationLevel
    can_observe_topics: Set[str]        # Topics they can observe
    can_participate_topics: Set[str]    # Topics they can actively participate in
    assists_agents: List[str]           # Agents they provide support to
    reports_to: str = None
    
class ObserverAssistantSystem:
    """System managing different participation levels and observer patterns"""
    
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.topic_channels: Dict[str, Set[str]] = {}  # topic -> participating agents
        self.assistance_requests: List[Dict] = []
        
        # Participation rules
        self.participation_rules = {
            ParticipationLevel.ACTIVE: {
                "can_broadcast": True,
                "can_send_direct": True,
                "can_respond": True,
                "can_observe_all": True,
                "can_request_help": True
            },
            ParticipationLevel.OBSERVER: {
                "can_broadcast": False,
                "can_send_direct": False,
                "can_respond": True,  # Limited responses only
                "can_observe_all": True,
                "can_request_help": False
            },
            ParticipationLevel.ASSISTANT: {
                "can_broadcast": False,
                "can_send_direct": True,  # To assisted agents only
                "can_respond": True,
                "can_observe_all": False,  # Only relevant topics
                "can_request_help": False
            },
            ParticipationLevel.SILENT: {
                "can_broadcast": False,
                "can_send_direct": False,
                "can_respond": False,
                "can_observe_all": True,
                "can_request_help": False
            },
            ParticipationLevel.SUPPORT: {
                "can_broadcast": False,
                "can_send_direct": True,  # When providing support
                "can_respond": True,
                "can_observe_all": False,  # Context-aware
                "can_request_help": False
            }
        }
    
    def add_agent(self, agent_id: str, role: AgentRole, participation_level: ParticipationLevel,
                  can_observe_topics: Set[str] = None, can_participate_topics: Set[str] = None,
                  assists_agents: List[str] = None, reports_to: str = None):
        """Add an agent with specific participation rules"""
        
        self.agents[agent_id] = Agent(
            id=agent_id,
            role=role,
            participation_level=participation_level,
            can_observe_topics=can_observe_topics or set(),
            can_participate_topics=can_participate_topics or set(),
            assists_agents=assists_agents or [],
            reports_to=reports_to
        )
    
    def setup_example_ecosystem(self):
        """Set up an example software development ecosystem"""
        
        # Active participants
        self.add_agent("user", AgentRole.USER, ParticipationLevel.ACTIVE,
                      can_observe_topics={"all"}, can_participate_topics={"all"})
        
        self.add_agent("product_manager", AgentRole.MANAGER, ParticipationLevel.ACTIVE,
                      can_observe_topics={"development", "design", "testing", "deployment"},
                      can_participate_topics={"development", "design", "testing", "deployment"})
        
        self.add_agent("backend_dev", AgentRole.DEVELOPER, ParticipationLevel.ACTIVE,
                      can_observe_topics={"development", "testing", "deployment"},
                      can_participate_topics={"development", "testing"})
        
        self.add_agent("frontend_dev", AgentRole.DEVELOPER, ParticipationLevel.ACTIVE,
                      can_observe_topics={"development", "design", "testing"},
                      can_participate_topics={"development", "design", "testing"})
        
        # Observer agents
        self.add_agent("graphic_designer", AgentRole.DESIGNER, ParticipationLevel.OBSERVER,
                      can_observe_topics={"development", "design"},
                      assists_agents=["frontend_dev"])
        
        self.add_agent("senior_analyst", AgentRole.ANALYST, ParticipationLevel.OBSERVER,
                      can_observe_topics={"development", "testing", "deployment"})
        
        # Assistant agents
        self.add_agent("ui_designer", AgentRole.DESIGNER, ParticipationLevel.ASSISTANT,
                      can_observe_topics={"design", "development"},
                      can_participate_topics={"design"},
                      assists_agents=["frontend_dev", "graphic_designer"])
        
        self.add_agent("qa_assistant", AgentRole.QA_TESTER, ParticipationLevel.ASSISTANT,
                      can_observe_topics={"testing", "development"},
                      can_participate_topics={"testing"},
                      assists_agents=["backend_dev", "frontend_dev"])
        
        # Support agents
        self.add_agent("devops_support", AgentRole.DEVOPS, ParticipationLevel.SUPPORT,
                      can_observe_topics={"deployment", "development"},
                      can_participate_topics={"deployment"},
                      assists_agents=["backend_dev", "frontend_dev"])
        
        # Silent observers
        self.add_agent("intern", AgentRole.ASSISTANT, ParticipationLevel.SILENT,
                      can_observe_topics={"development", "design", "testing"})
    
    def can_agent_participate(self, agent_id: str, action: str, topic: str = None, 
                             target_agent: str = None) -> tuple[bool, str]:
        """Check if agent can perform an action"""
        
        if agent_id not in self.agents:
            return False, f"Agent {agent_id} not found"
        
        agent = self.agents[agent_id]
        rules = self.participation_rules[agent.participation_level]
        
        # Check basic permission
        if action == "broadcast" and not rules["can_broadcast"]:
            return False, f"{agent_id} ({agent.participation_level.value}) cannot broadcast"
        
        if action == "send_direct" and not rules["can_send_direct"]:
            return False, f"{agent_id} ({agent.participation_level.value}) cannot send direct messages"
        
        if action == "respond" and not rules["can_respond"]:
            return False, f"{agent_id} ({agent.participation_level.value}) cannot respond"
        
        # Check topic-specific permissions
        if topic and action in ["broadcast", "send_direct", "respond"]:
            if topic not in agent.can_participate_topics and "all" not in agent.can_participate_topics:
                return False, f"{agent_id} cannot participate in {topic} topic"
        
        # Check assistance relationships
        if action == "send_direct" and agent.participation_level == ParticipationLevel.ASSISTANT:
            if target_agent and target_agent not in agent.assists_agents:
                return False, f"{agent_id} can only send direct messages to assisted agents"
        
        return True, "Allowed"
    
    def can_agent_observe(self, agent_id: str, topic: str, sender: str) -> tuple[bool, str]:
        """Check if agent can observe a message/topic"""
        
        if agent_id not in self.agents:
            return False, f"Agent {agent_id} not found"
        
        agent = self.agents[agent_id]
        rules = self.participation_rules[agent.participation_level]
        
        # Can observe all topics
        if rules["can_observe_all"] or "all" in agent.can_observe_topics:
            return True, "Can observe all"
        
        # Check specific topic permissions
        if topic in agent.can_observe_topics:
            return True, f"Can observe {topic} topic"
        
        # Assistant agents can observe messages from/to assisted agents
        if agent.participation_level == ParticipationLevel.ASSISTANT:
            if sender in agent.assists_agents:
                return True, f"Observing assisted agent {sender}"
        
        return False, f"{agent_id} cannot observe {topic} topic"
    
    def send_message(self, sender: str, recipient: str, content: str, topic: str = "general"):
        """Send message with participation level checking"""
        
        can_send, reason = self.can_agent_participate(sender, "send_direct", topic, recipient)
        
        if not can_send:
            print(f"❌ BLOCKED: {reason}")
            return False
        
        # Check if recipient can observe
        can_observe, obs_reason = self.can_agent_observe(recipient, topic, sender)
        
        if not can_observe:
            print(f"❌ BLOCKED: Recipient {recipient} cannot observe {topic} - {obs_reason}")
            return False
        
        # Send the message
        sender_agent = self.agents[sender]
        recipient_agent = self.agents[recipient]
        
        print(f"📧 DIRECT: {sender} ({sender_agent.role.value}) -> {recipient} ({recipient_agent.role.value})")
        print(f"   Topic: {topic} | Content: {content}")
        
        # Log to common inbox with participation info
        self._log_to_common_inbox(sender, recipient, content, topic, "direct")
        
        return True
    
    def broadcast_message(self, sender: str, content: str, topic: str = "general"):
        """Send broadcast with participation checking"""
        
        can_broadcast, reason = self.can_agent_participate(sender, "broadcast", topic)
        
        if not can_broadcast:
            print(f"❌ BLOCKED: {reason}")
            return False
        
        sender_agent = self.agents[sender]
        
        # Determine who can observe this broadcast
        observers = []
        for agent_id, agent in self.agents.items():
            if agent_id != sender:
                can_observe, _ = self.can_agent_observe(agent_id, topic, sender)
                if can_observe:
                    observers.append(agent_id)
        
        print(f"📢 BROADCAST: {sender} ({sender_agent.role.value}) -> {len(observers)} observers")
        print(f"   Topic: {topic} | Content: {content}")
        print(f"   Observers: {', '.join(observers)}")
        
        # Log to common inbox
        self._log_to_common_inbox(sender, "ALL", content, topic, "broadcast")
        
        return True
    
    def request_assistance(self, requester: str, topic: str, content: str):
        """Request assistance from support agents"""
        
        # Find available assistants for this topic
        available_assistants = []
        for agent_id, agent in self.agents.items():
            if (agent.participation_level in [ParticipationLevel.ASSISTANT, ParticipationLevel.SUPPORT] and
                (topic in agent.can_observe_topics or requester in agent.assists_agents)):
                available_assistants.append(agent_id)
        
        print(f"🆘 ASSISTANCE REQUEST: {requester} needs help with {topic}")
        print(f"   Content: {content}")
        print(f"   Available assistants: {', '.join(available_assistants)}")
        
        # Log assistance request
        self.assistance_requests.append({
            "requester": requester,
            "topic": topic,
            "content": content,
            "available_assistants": available_assistants
        })
        
        return available_assistants
    
    def _log_to_common_inbox(self, sender: str, recipient: str, content: str, topic: str, msg_type: str):
        """Log message to common inbox with participation context"""
        
        sender_agent = self.agents[sender]
        participation_icon = {
            ParticipationLevel.ACTIVE: "🟢",
            ParticipationLevel.OBSERVER: "👁️",
            ParticipationLevel.ASSISTANT: "🤝",
            ParticipationLevel.SILENT: "🔇",
            ParticipationLevel.SUPPORT: "🛠️"
        }.get(sender_agent.participation_level, "❓")
        
        log_entry = f"[{topic}] {participation_icon} {sender} -> {recipient}: {content}"
        print(f"📝 COMMON INBOX: {log_entry}")
    
    def show_ecosystem_overview(self):
        """Show the complete ecosystem overview"""
        
        print("AGENT ECOSYSTEM OVERVIEW")
        print("=" * 30)
        
        # Group agents by participation level
        by_participation = {}
        for agent in self.agents.values():
            level = agent.participation_level
            if level not in by_participation:
                by_participation[level] = []
            by_participation[level].append(agent)
        
        for level in ParticipationLevel:
            if level in by_participation:
                icon = {
                    ParticipationLevel.ACTIVE: "🟢",
                    ParticipationLevel.OBSERVER: "👁️",
                    ParticipationLevel.ASSISTANT: "🤝",
                    ParticipationLevel.SILENT: "🔇",
                    ParticipationLevel.SUPPORT: "🛠️"
                }[level]
                
                print(f"\n{icon} {level.value.upper()} AGENTS:")
                
                for agent in by_participation[level]:
                    print(f"  {agent.id} ({agent.role.value})")
                    if agent.can_observe_topics:
                        print(f"    Observes: {', '.join(agent.can_observe_topics)}")
                    if agent.can_participate_topics:
                        print(f"    Participates: {', '.join(agent.can_participate_topics)}")
                    if agent.assists_agents:
                        print(f"    Assists: {', '.join(agent.assists_agents)}")

def demonstrate_observer_assistant_system():
    """Demonstrate the observer/assistant system"""
    
    print("OBSERVER/ASSISTANT AGENT ECOSYSTEM")
    print("=" * 40)
    
    system = ObserverAssistantSystem()
    system.setup_example_ecosystem()
    system.show_ecosystem_overview()
    
    print("\n" + "="*60)
    print("COMMUNICATION SCENARIOS")
    print("="*60)
    
    # Scenario 1: Active development discussion
    print("\n1. DEVELOPMENT DISCUSSION:")
    system.broadcast_message("backend_dev", "New API endpoint ready for frontend integration", "development")
    system.send_message("frontend_dev", "backend_dev", "Great! I'll integrate it today", "development")
    
    # Scenario 2: Observer trying to participate (should be blocked)
    print("\n2. OBSERVER ATTEMPTING BROADCAST (BLOCKED):")
    system.broadcast_message("graphic_designer", "I have design suggestions", "development")
    
    # Scenario 3: Assistant providing help
    print("\n3. ASSISTANT PROVIDING SUPPORT:")
    system.send_message("ui_designer", "frontend_dev", "I've updated the component designs", "design")
    
    # Scenario 4: Support request
    print("\n4. ASSISTANCE REQUEST:")
    system.request_assistance("frontend_dev", "deployment", "Need help with production deployment")
    
    # Scenario 5: Support agent responding
    print("\n5. SUPPORT AGENT HELPING:")
    system.send_message("devops_support", "frontend_dev", "I can help with the deployment", "deployment")
    
    # Scenario 6: Silent agent trying to communicate (should be blocked)
    print("\n6. SILENT AGENT ATTEMPTING COMMUNICATION (BLOCKED):")
    system.send_message("intern", "backend_dev", "I have a question", "development")

if __name__ == "__main__":
    demonstrate_observer_assistant_system()
    
    print("\n\nPARTICIPATION LEVELS:")
    print("=" * 22)
    print("🟢 ACTIVE:    Full participation - can broadcast, send, respond")
    print("👁️ OBSERVER:  Can see all, limited responses, no broadcasts")
    print("🤝 ASSISTANT: Can help specific agents, topic-limited participation")
    print("🔇 SILENT:    Can observe all, cannot communicate")
    print("🛠️ SUPPORT:   Context-aware, provides help when requested")
    print()
    print("REAL-WORLD EXAMPLES:")
    print("• Graphic designer observes frontend discussions")
    print("• QA assistant helps developers with testing")
    print("• DevOps support provides deployment assistance")
    print("• Analyst observes all but doesn't participate")
    print("• Intern silently learns from all conversations")