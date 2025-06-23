#!/usr/bin/env python3
"""
Hierarchical Broadcast Concept
Shows the key concept without screen complexity
"""

from enum import Enum
from typing import Dict, List
from dataclasses import dataclass

class Rank(Enum):
    USER = 1        # 👑 Highest priority - trumps everything
    LEADER = 2      # ⭐ Executive level
    MANAGER = 3     # 🔶 Management level  
    WORKER = 4      # 🔸 Worker level

@dataclass
class Agent:
    id: str
    rank: Rank

class HierarchicalBroadcastRules:
    """Defines who can see whose broadcasts in the common inbox"""
    
    def __init__(self):
        # Visibility matrix: Who can see broadcasts from whom
        self.visibility_rules = {
            Rank.USER: [Rank.USER, Rank.LEADER, Rank.MANAGER, Rank.WORKER],  # User sees everything
            Rank.LEADER: [Rank.LEADER, Rank.MANAGER, Rank.WORKER],          # Leader sees subordinates  
            Rank.MANAGER: [Rank.MANAGER, Rank.WORKER],                      # Manager sees workers + peers
            Rank.WORKER: [Rank.WORKER]                                      # Workers see only peer level
        }
        
        # Priority ordering for common inbox (lower = appears higher)
        self.priority_order = {
            Rank.USER: 1,     # Always appears at top
            Rank.LEADER: 2,   
            Rank.MANAGER: 3,
            Rank.WORKER: 4    # Appears at bottom
        }
    
    def can_see_broadcast(self, viewer_rank: Rank, broadcaster_rank: Rank) -> bool:
        """Can viewer see broadcaster's messages in common inbox?"""
        return broadcaster_rank in self.visibility_rules.get(viewer_rank, [])
    
    def get_broadcast_priority(self, broadcaster_rank: Rank) -> int:
        """Get display priority in common inbox"""
        return self.priority_order.get(broadcaster_rank, 999)

def demonstrate_hierarchical_visibility():
    """Show exactly who sees what in the common inbox"""
    
    print("HIERARCHICAL BROADCAST VISIBILITY")
    print("=" * 40)
    
    # Setup agents
    agents = {
        "user": Agent("user", Rank.USER),
        "ceo": Agent("ceo", Rank.LEADER), 
        "manager1": Agent("manager1", Rank.MANAGER),
        "manager2": Agent("manager2", Rank.MANAGER),
        "worker1": Agent("worker1", Rank.WORKER),
        "worker2": Agent("worker2", Rank.WORKER),
        "worker3": Agent("worker3", Rank.WORKER)
    }
    
    rules = HierarchicalBroadcastRules()
    
    # Show visibility matrix
    print("\nVISIBILITY MATRIX:")
    print("-" * 20)
    print("Viewer → Can see broadcasts from:")
    
    for viewer_rank in Rank:
        visible_ranks = rules.visibility_rules[viewer_rank]
        rank_names = [rank.name for rank in visible_ranks]
        icon = {Rank.USER: "👑", Rank.LEADER: "⭐", Rank.MANAGER: "🔶", Rank.WORKER: "🔸"}[viewer_rank]
        print(f"{icon} {viewer_rank.name:<7} → {', '.join(rank_names)}")
    
    print("\n" + "="*60)
    print("BROADCAST SCENARIOS:")
    print("="*60)
    
    # Scenario examples
    scenarios = [
        {
            "broadcaster": "worker1",
            "message": "Need help with task X",
            "description": "Worker broadcast - limited scope"
        },
        {
            "broadcaster": "manager1", 
            "message": "Team meeting at 3 PM",
            "description": "Manager broadcast - trickles down"
        },
        {
            "broadcaster": "ceo",
            "message": "Quarterly results excellent!",
            "description": "Leader broadcast - company-wide"
        },
        {
            "broadcaster": "user",
            "message": "URGENT: System maintenance now!",
            "description": "User broadcast - trumps everything"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        broadcaster = agents[scenario["broadcaster"]]
        broadcaster_rank = broadcaster.rank
        
        print(f"\n{i}. {scenario['description'].upper()}")
        print(f"   {broadcaster.id} ({broadcaster_rank.name}): \"{scenario['message']}\"")
        print("   Who sees this in common inbox:")
        
        for viewer_id, viewer in agents.items():
            can_see = rules.can_see_broadcast(viewer.rank, broadcaster_rank)
            icon = {Rank.USER: "👑", Rank.LEADER: "⭐", Rank.MANAGER: "🔶", Rank.WORKER: "🔸"}[viewer.rank]
            status = "✓ VISIBLE" if can_see else "✗ HIDDEN"
            print(f"     {icon} {viewer_id:<10} ({viewer.rank.name:<7}) → {status}")

def show_common_inbox_filtering():
    """Show how common inbox appears to different ranks"""
    
    print("\n\n" + "="*60)
    print("COMMON INBOX VIEW BY RANK")
    print("="*60)
    
    # Simulated common inbox messages (in chronological order)
    messages = [
        {"sender": "worker1", "rank": Rank.WORKER, "content": "Need help with task X", "priority": 4},
        {"sender": "manager1", "rank": Rank.MANAGER, "content": "Team meeting at 3 PM", "priority": 3},
        {"sender": "worker2", "rank": Rank.WORKER, "content": "Completed assignment A", "priority": 4},
        {"sender": "ceo", "rank": Rank.LEADER, "content": "Quarterly results excellent!", "priority": 2},
        {"sender": "user", "rank": Rank.USER, "content": "URGENT: System maintenance!", "priority": 1}
    ]
    
    rules = HierarchicalBroadcastRules()
    
    # Show filtered view for each rank
    for viewer_rank in Rank:
        icon = {Rank.USER: "👑", Rank.LEADER: "⭐", Rank.MANAGER: "🔶", Rank.WORKER: "🔸"}[viewer_rank]
        print(f"\n{icon} {viewer_rank.name} VIEW OF COMMON INBOX:")
        print("-" * 30)
        
        # Filter messages this rank can see
        visible_messages = []
        for msg in messages:
            if rules.can_see_broadcast(viewer_rank, msg["rank"]):
                visible_messages.append(msg)
        
        # Sort by priority (user messages first)
        visible_messages.sort(key=lambda x: x["priority"])
        
        if visible_messages:
            for i, msg in enumerate(visible_messages, 1):
                sender_icon = {Rank.USER: "👑", Rank.LEADER: "⭐", Rank.MANAGER: "🔶", Rank.WORKER: "🔸"}[msg["rank"]]
                print(f"  {i}. {sender_icon} {msg['sender']}: {msg['content']}")
        else:
            print("  (No messages visible)")

def show_session_architecture():
    """Show the complete session architecture"""
    
    print("\n\n" + "="*60)
    print("SESSION ARCHITECTURE WITH HIERARCHY")
    print("="*60)
    
    agents = ["user", "ceo", "manager1", "manager2", "worker1", "worker2", "worker3"]
    
    print("SHARED SESSION:")
    print("  common_inbox   (ALL communications, filtered by rank)")
    print()
    
    print("PER-AGENT SESSIONS:")
    for agent in agents:
        print(f"  {agent.upper()}:")
        print(f"    {agent}_inbox      (personal messages)")
        print(f"    {agent}_outbox     (personal sent log)")
        print(f"    {agent}_signals    (polling triggers)")
        print()
    
    print(f"TOTAL SESSIONS for {len(agents)} agents:")
    print(f"  Shared: 1 (common_inbox)")
    print(f"  Per-agent: {len(agents)} × 3 = {len(agents) * 3}")
    print(f"  TOTAL: {1 + len(agents) * 3} sessions")
    print()
    
    print("HIERARCHY FEATURES:")
    print("  • Common inbox shows ALL communications")
    print("  • Each agent sees filtered view based on rank")
    print("  • User broadcasts trump everything (highest priority)")
    print("  • Manager broadcasts trickle down to workers")
    print("  • Worker broadcasts stay at worker level")
    print("  • Direct messages still use personal inboxes")

if __name__ == "__main__":
    demonstrate_hierarchical_visibility()
    show_common_inbox_filtering()
    show_session_architecture()
    
    print("\n\nKEY INSIGHTS:")
    print("=" * 15)
    print("👑 USER: Sees everything, highest priority in common inbox")
    print("⭐ LEADER: Sees leader/manager/worker, high priority")
    print("🔶 MANAGER: Sees manager/worker, medium priority")
    print("🔸 WORKER: Sees only worker level, lowest priority")
    print()
    print("BENEFITS:")
    print("• Appropriate information flows based on hierarchy")
    print("• Important messages (user/leader) get priority")
    print("• Workers aren't overwhelmed by executive communications")  
    print("• Managers coordinate their teams effectively")
    print("• Full transparency with intelligent filtering")