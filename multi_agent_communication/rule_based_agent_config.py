#!/usr/bin/env python3
"""
Simplified Rule-Based System for Dynamic Agent Configuration
Auto-determines topology, polling, and interactions based on context
"""

from typing import Dict, List, Set, Any, Optional
from dataclasses import dataclass
from enum import Enum

# =============================================================================
# KNOWLEDGE BASE FACTS
# =============================================================================

@dataclass
class AgentFact:
    agent_id: str
    role: str
    activity_level: str  # high, medium, low
    expertise: Set[str]
    team: str = None

@dataclass
class ProjectFact:
    project_type: str  # startup, enterprise, research
    phase: str  # planning, development, testing, deployment
    urgency: str  # critical, urgent, normal, low
    team_size: int
    distribution: str  # collocated, distributed, hybrid

# =============================================================================
# RULE-BASED CONFIGURATION ENGINE
# =============================================================================

class RuleBasedConfigSystem:
    """Rule-based system that generates agent configurations"""
    
    def __init__(self):
        self.agents: List[AgentFact] = []
        self.project: Optional[ProjectFact] = None
        self.derived_config = {}
        
    def add_agent(self, agent_id: str, role: str, activity_level: str, expertise: Set[str], team: str = None):
        """Add an agent to the knowledge base"""
        self.agents.append(AgentFact(agent_id, role, activity_level, expertise, team))
    
    def set_project_context(self, project_type: str, phase: str, urgency: str, team_size: int, distribution: str):
        """Set project context"""
        self.project = ProjectFact(project_type, phase, urgency, team_size, distribution)
    
    def generate_configuration(self) -> Dict[str, Any]:
        """Apply rules to generate configuration"""
        
        if not self.project:
            raise ValueError("Project context must be set")
        
        print("RULE-BASED CONFIGURATION GENERATION")
        print("=" * 42)
        
        # Apply rules in order of priority
        self._apply_topology_rules()
        self._apply_polling_rules()
        self._apply_participation_rules()
        self._apply_broadcast_rules()
        
        return self.derived_config
    
    def _apply_topology_rules(self):
        """Rules for determining communication topology"""
        
        print("\nApplying TOPOLOGY rules...")
        
        # Rule 1: Small startup teams use MESH for flexibility
        if (self.project.project_type == "startup" and 
            self.project.team_size <= 6):
            self.derived_config["topology"] = "mesh"
            self.derived_config["topology_reason"] = "Small startup team needs maximum flexibility"
            print("  ✓ Rule: startup_small_team → mesh topology")
        
        # Rule 2: Large enterprise teams use HIERARCHICAL for structure
        elif (self.project.project_type == "enterprise" and 
              self.project.team_size > 10):
            self.derived_config["topology"] = "hierarchical"
            self.derived_config["topology_reason"] = "Large enterprise team needs clear structure"
            print("  ✓ Rule: enterprise_large_team → hierarchical topology")
        
        # Rule 3: Development phase with high coordination needs STAR
        elif (self.project.phase == "development" and 
              self._has_role("tech_lead") and
              self.project.urgency in ["critical", "urgent"]):
            self.derived_config["topology"] = "star"
            self.derived_config["star_center"] = self._find_agent_by_role("tech_lead")
            self.derived_config["topology_reason"] = "Critical development needs central coordination"
            print("  ✓ Rule: critical_development → star topology with tech lead center")
        
        # Rule 4: Testing phase uses LINEAR for systematic testing
        elif self.project.phase == "testing":
            self.derived_config["topology"] = "linear" 
            self.derived_config["topology_reason"] = "Testing phase needs systematic handoffs"
            print("  ✓ Rule: testing_phase → linear topology")
        
        # Rule 5: Planning phase uses MESH for brainstorming
        elif self.project.phase == "planning":
            self.derived_config["topology"] = "mesh"
            self.derived_config["topology_reason"] = "Planning needs open collaboration"
            print("  ✓ Rule: planning_phase → mesh topology")
        
        # Default: Medium mesh for balanced communication
        else:
            self.derived_config["topology"] = "mesh"
            self.derived_config["topology_reason"] = "Default balanced communication"
            print("  ✓ Rule: default → mesh topology")
    
    def _apply_polling_rules(self):
        """Rules for determining polling frequencies"""
        
        print("\nApplying POLLING rules...")
        
        # Rule 1: Critical projects need fast polling
        if self.project.urgency == "critical":
            self.derived_config["normal_poll_interval"] = 1.0
            self.derived_config["urgent_poll_interval"] = 0.2
            self.derived_config["polling_reason"] = "Critical urgency requires immediate response"
            print("  ✓ Rule: critical_urgency → fast polling (1.0s/0.2s)")
        
        # Rule 2: Distributed teams need more frequent polling
        elif self.project.distribution == "distributed":
            self.derived_config["normal_poll_interval"] = 2.0
            self.derived_config["urgent_poll_interval"] = 0.5
            self.derived_config["polling_reason"] = "Distributed teams need frequent sync"
            print("  ✓ Rule: distributed_team → frequent polling (2.0s/0.5s)")
        
        # Rule 3: High activity agents need responsive polling
        elif self._has_high_activity_agents():
            self.derived_config["normal_poll_interval"] = 3.0
            self.derived_config["urgent_poll_interval"] = 0.5
            self.derived_config["polling_reason"] = "High activity agents need responsiveness"
            print("  ✓ Rule: high_activity_agents → responsive polling (3.0s/0.5s)")
        
        # Rule 4: Research projects can use slower polling
        elif self.project.project_type == "research":
            self.derived_config["normal_poll_interval"] = 10.0
            self.derived_config["urgent_poll_interval"] = 2.0
            self.derived_config["polling_reason"] = "Research projects allow thoughtful pace"
            print("  ✓ Rule: research_project → slow polling (10.0s/2.0s)")
        
        # Default: Standard polling
        else:
            self.derived_config["normal_poll_interval"] = 5.0
            self.derived_config["urgent_poll_interval"] = 1.0
            self.derived_config["polling_reason"] = "Standard balanced polling"
            print("  ✓ Rule: default → standard polling (5.0s/1.0s)")
    
    def _apply_participation_rules(self):
        """Rules for determining agent participation levels"""
        
        print("\nApplying PARTICIPATION rules...")
        
        participation_levels = {}
        
        for agent in self.agents:
            
            # Rule 1: Managers are always ACTIVE
            if "manager" in agent.role or "lead" in agent.role:
                participation_levels[agent.agent_id] = "active"
                print(f"  ✓ Rule: {agent.agent_id} (manager/lead) → active participation")
            
            # Rule 2: Interns and junior roles are OBSERVERS
            elif "intern" in agent.role or "junior" in agent.role:
                participation_levels[agent.agent_id] = "observer"
                print(f"  ✓ Rule: {agent.agent_id} (intern/junior) → observer participation")
            
            # Rule 3: Designers assist frontend developers
            elif agent.role == "designer" and self._has_role("frontend_developer"):
                participation_levels[agent.agent_id] = "assistant"
                self.derived_config.setdefault("assistance_relationships", []).append(
                    (agent.agent_id, self._find_agent_by_role("frontend_developer"))
                )
                print(f"  ✓ Rule: {agent.agent_id} (designer) → assistant to frontend_developer")
            
            # Rule 4: DevOps provides SUPPORT during deployment
            elif "devops" in agent.role and self.project.phase == "deployment":
                participation_levels[agent.agent_id] = "support"
                print(f"  ✓ Rule: {agent.agent_id} (devops + deployment) → support participation")
            
            # Rule 5: QA engineers become ACTIVE during testing
            elif "qa" in agent.role and self.project.phase == "testing":
                participation_levels[agent.agent_id] = "active"
                print(f"  ✓ Rule: {agent.agent_id} (qa + testing) → active participation")
            
            # Rule 6: Low activity agents are SILENT in critical projects
            elif agent.activity_level == "low" and self.project.urgency == "critical":
                participation_levels[agent.agent_id] = "silent"
                print(f"  ✓ Rule: {agent.agent_id} (low activity + critical) → silent participation")
            
            # Default: ACTIVE participation
            else:
                participation_levels[agent.agent_id] = "active"
                print(f"  ✓ Rule: {agent.agent_id} (default) → active participation")
        
        self.derived_config["participation_levels"] = participation_levels
        self.derived_config["participation_reason"] = "Role and context-based participation"
    
    def _apply_broadcast_rules(self):
        """Rules for broadcast behavior"""
        
        print("\nApplying BROADCAST rules...")
        
        # Rule 1: Critical projects enable emergency broadcasts
        if self.project.urgency == "critical":
            self.derived_config["emergency_broadcasts"] = True
            self.derived_config["broadcast_priority"] = "critical"
            self.derived_config["broadcast_reason"] = "Critical projects need emergency communication"
            print("  ✓ Rule: critical_urgency → emergency broadcasts enabled")
        
        # Rule 2: Testing phase gives QA broadcast priority
        elif self.project.phase == "testing" and self._has_role("qa"):
            self.derived_config["qa_broadcast_priority"] = True
            self.derived_config["broadcast_focus"] = "testing"
            self.derived_config["broadcast_reason"] = "Testing phase prioritizes QA communication"
            print("  ✓ Rule: testing_phase + qa → QA broadcast priority")
        
        # Rule 3: Deployment phase gives DevOps broadcast priority
        elif self.project.phase == "deployment" and self._has_role("devops"):
            self.derived_config["devops_broadcast_priority"] = True
            self.derived_config["broadcast_focus"] = "deployment"
            self.derived_config["broadcast_reason"] = "Deployment phase prioritizes DevOps communication"
            print("  ✓ Rule: deployment_phase + devops → DevOps broadcast priority")
        
        # Rule 4: Distributed teams enable frequent broadcasts
        elif self.project.distribution == "distributed":
            self.derived_config["frequent_broadcasts"] = True
            self.derived_config["broadcast_reason"] = "Distributed teams need frequent updates"
            print("  ✓ Rule: distributed_team → frequent broadcasts")
        
        # Default: Standard broadcasts
        else:
            self.derived_config["broadcast_priority"] = "normal"
            self.derived_config["broadcast_reason"] = "Standard broadcast configuration"
            print("  ✓ Rule: default → standard broadcasts")
    
    # Helper methods
    def _has_role(self, role: str) -> bool:
        """Check if any agent has the specified role"""
        return any(role in agent.role for agent in self.agents)
    
    def _find_agent_by_role(self, role: str) -> Optional[str]:
        """Find first agent with specified role"""
        for agent in self.agents:
            if role in agent.role:
                return agent.agent_id
        return None
    
    def _has_high_activity_agents(self) -> bool:
        """Check if there are high activity agents"""
        return any(agent.activity_level == "high" for agent in self.agents)
    
    def show_knowledge_base(self):
        """Display current knowledge base"""
        print("\nKNOWLEDGE BASE:")
        print("-" * 15)
        
        print(f"Project: {self.project.project_type} | {self.project.phase} | {self.project.urgency}")
        print(f"Team: {self.project.team_size} agents | {self.project.distribution}")
        
        print("\nAgents:")
        for agent in self.agents:
            print(f"  {agent.agent_id}: {agent.role} ({agent.activity_level}) - {', '.join(agent.expertise)}")

def demonstrate_rule_based_scenarios():
    """Demonstrate different rule-based scenarios"""
    
    scenarios = [
        {
            "name": "Critical Startup Development",
            "project": ("startup", "development", "critical", 4, "distributed"),
            "agents": [
                ("tech_lead", "tech_lead", "high", {"architecture", "leadership"}),
                ("frontend_dev", "frontend_developer", "high", {"react", "typescript"}),
                ("backend_dev", "backend_developer", "high", {"nodejs", "database"}),
                ("designer", "designer", "medium", {"ui", "ux"})
            ]
        },
        {
            "name": "Enterprise Testing Phase",
            "project": ("enterprise", "testing", "normal", 8, "collocated"),
            "agents": [
                ("qa_manager", "qa_manager", "medium", {"testing", "management"}),
                ("qa_engineer1", "qa_engineer", "high", {"automation", "selenium"}),
                ("qa_engineer2", "qa_engineer", "medium", {"manual_testing"}),
                ("devops", "devops_engineer", "low", {"deployment", "monitoring"}),
                ("dev1", "backend_developer", "medium", {"api", "testing"}),
                ("dev2", "frontend_developer", "medium", {"react", "testing"}),
                ("intern", "qa_intern", "low", {"learning", "manual_testing"}),
                ("architect", "senior_architect", "medium", {"architecture", "review"})
            ]
        },
        {
            "name": "Research Planning Phase",
            "project": ("research", "planning", "low", 6, "hybrid"),
            "agents": [
                ("researcher1", "senior_researcher", "medium", {"ai", "nlp"}),
                ("researcher2", "researcher", "high", {"machine_learning"}),
                ("data_scientist", "data_scientist", "high", {"analysis", "visualization"}),
                ("intern1", "research_intern", "low", {"learning", "analysis"}),
                ("intern2", "research_intern", "low", {"learning", "documentation"}),
                ("advisor", "research_advisor", "low", {"guidance", "review"})
            ]
        }
    ]
    
    for scenario in scenarios:
        print(f"\n{'='*60}")
        print(f"SCENARIO: {scenario['name']}")
        print(f"{'='*60}")
        
        # Create system and add facts
        system = RuleBasedConfigSystem()
        
        # Set project context
        project_data = scenario['project']
        system.set_project_context(*project_data)
        
        # Add agents
        for agent_data in scenario['agents']:
            system.add_agent(*agent_data)
        
        # Show knowledge base
        system.show_knowledge_base()
        
        # Generate configuration
        config = system.generate_configuration()
        
        print(f"\nGENERATED CONFIGURATION:")
        print(f"-" * 25)
        print(f"Topology: {config['topology']} ({config['topology_reason']})")
        if 'star_center' in config:
            print(f"Star Center: {config['star_center']}")
        
        print(f"Polling: {config['normal_poll_interval']}s/{config['urgent_poll_interval']}s ({config['polling_reason']})")
        
        print(f"Participation Levels:")
        for agent_id, level in config['participation_levels'].items():
            print(f"  {agent_id}: {level}")
        
        if 'assistance_relationships' in config:
            print(f"Assistance: {config['assistance_relationships']}")
        
        print(f"Broadcasts: {config.get('broadcast_priority', 'normal')} ({config['broadcast_reason']})")

if __name__ == "__main__":
    demonstrate_rule_based_scenarios()
    
    print(f"\n\n{'='*60}")
    print("RULE-BASED SYSTEM BENEFITS")
    print(f"{'='*60}")
    print("✓ Context-aware configuration generation")
    print("✓ Automatic topology selection based on team/project")
    print("✓ Dynamic polling frequencies based on urgency")
    print("✓ Role-based participation level assignment")
    print("✓ Phase-specific broadcast priorities")
    print("✓ Extensible rule base for new scenarios")
    print("✓ Explainable reasoning for all decisions")
    print("✓ No manual configuration required")