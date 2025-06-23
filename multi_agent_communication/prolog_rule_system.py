#!/usr/bin/env python3
"""
Prolog-Style Rule-Based System for Dynamic Multi-Agent Configuration
Uses rules to automatically determine topology, polling, and interactions
"""

from typing import Dict, List, Set, Tuple, Any, Optional
from dataclasses import dataclass
from enum import Enum
import re

class Fact:
    """Base class for facts in the knowledge base"""
    pass

@dataclass
class AgentFact(Fact):
    """Facts about agents"""
    agent_id: str
    role: str
    activity_level: str  # high, medium, low
    domain_expertise: Set[str]
    team: str = None
    reports_to: str = None

@dataclass
class TeamFact(Fact):
    """Facts about teams"""
    team_id: str
    team_type: str  # development, design, qa, management
    size: int
    coordination_need: str  # high, medium, low

@dataclass
class ProjectFact(Fact):
    """Facts about project characteristics"""
    project_type: str  # startup, enterprise, research
    phase: str  # planning, development, testing, deployment
    urgency: str  # critical, normal, low
    team_distribution: str  # collocated, distributed, hybrid

@dataclass
class WorkflowFact(Fact):
    """Facts about workflow patterns"""
    workflow_type: str  # sequential, parallel, iterative
    dependencies: List[Tuple[str, str]]  # (prerequisite, dependent)
    bottlenecks: List[str]

class Rule:
    """Prolog-style rule: IF conditions THEN conclusions"""
    
    def __init__(self, name: str, conditions: List[str], conclusions: List[str], priority: int = 1):
        self.name = name
        self.conditions = conditions
        self.conclusions = conclusions
        self.priority = priority
    
    def evaluate(self, knowledge_base: 'KnowledgeBase') -> List[str]:
        """Evaluate rule against knowledge base"""
        if all(knowledge_base.query(condition) for condition in self.conditions):
            return self.conclusions
        return []

class KnowledgeBase:
    """Prolog-style knowledge base with facts and rules"""
    
    def __init__(self):
        self.facts: List[Fact] = []
        self.rules: List[Rule] = []
        self.derived_facts: Set[str] = set()
        
    def add_fact(self, fact: Fact):
        """Add a fact to the knowledge base"""
        self.facts.append(fact)
    
    def add_rule(self, rule: Rule):
        """Add a rule to the knowledge base"""
        self.rules.append(rule)
    
    def query(self, query_str: str) -> bool:
        """Query the knowledge base (simplified pattern matching)"""
        
        # Check derived facts first
        if query_str in self.derived_facts:
            return True
        
        # Pattern matching for different fact types
        for fact in self.facts:
            if self._matches_pattern(query_str, fact):
                return True
        
        return False
    
    def _matches_pattern(self, pattern: str, fact: Fact) -> bool:
        """Match a query pattern against a fact"""
        
        if isinstance(fact, AgentFact):
            # agent(ID, role, activity_level)
            if pattern.startswith("agent("):
                parts = self._parse_pattern(pattern)
                return (self._match_value(parts[0], fact.agent_id) and
                       self._match_value(parts[1], fact.role) and
                       self._match_value(parts[2], fact.activity_level))
            
            # has_expertise(agent, domain)
            elif pattern.startswith("has_expertise("):
                parts = self._parse_pattern(pattern)
                return (self._match_value(parts[0], fact.agent_id) and
                       parts[1] in fact.domain_expertise)
            
            # reports_to(agent, supervisor)
            elif pattern.startswith("reports_to("):
                parts = self._parse_pattern(pattern)
                return (self._match_value(parts[0], fact.agent_id) and
                       self._match_value(parts[1], fact.reports_to))
            
            # in_team(agent, team)
            elif pattern.startswith("in_team("):
                parts = self._parse_pattern(pattern)
                return (self._match_value(parts[0], fact.agent_id) and
                       self._match_value(parts[1], fact.team))
        
        elif isinstance(fact, TeamFact):
            # team(ID, type, size, coordination_need)
            if pattern.startswith("team("):
                parts = self._parse_pattern(pattern)
                return (self._match_value(parts[0], fact.team_id) and
                       self._match_value(parts[1], fact.team_type) and
                       self._match_value(parts[2], str(fact.size)) and
                       self._match_value(parts[3], fact.coordination_need))
        
        elif isinstance(fact, ProjectFact):
            # project(type, phase, urgency, distribution)
            if pattern.startswith("project("):
                parts = self._parse_pattern(pattern)
                return (self._match_value(parts[0], fact.project_type) and
                       self._match_value(parts[1], fact.phase) and
                       self._match_value(parts[2], fact.urgency) and
                       self._match_value(parts[3], fact.team_distribution))
        
        elif isinstance(fact, WorkflowFact):
            # workflow(type)
            if pattern.startswith("workflow("):
                parts = self._parse_pattern(pattern)
                return self._match_value(parts[0], fact.workflow_type)
        
        return False
    
    def _parse_pattern(self, pattern: str) -> List[str]:
        """Parse pattern like 'agent(X, developer, high)' into parts"""
        content = pattern[pattern.find('(')+1:pattern.rfind(')')]
        return [part.strip() for part in content.split(',')]
    
    def _match_value(self, pattern_value: str, actual_value: str) -> bool:
        """Match pattern value against actual value (supports variables)"""
        if pattern_value.startswith('_') or pattern_value.isupper():
            return True  # Variable matches anything
        return pattern_value == actual_value
    
    def infer(self):
        """Apply all rules to derive new facts"""
        changed = True
        iterations = 0
        max_iterations = 10
        
        while changed and iterations < max_iterations:
            changed = False
            iterations += 1
            
            # Sort rules by priority (higher priority first)
            sorted_rules = sorted(self.rules, key=lambda r: r.priority, reverse=True)
            
            for rule in sorted_rules:
                conclusions = rule.evaluate(self)
                for conclusion in conclusions:
                    if conclusion not in self.derived_facts:
                        self.derived_facts.add(conclusion)
                        changed = True
                        print(f"Derived: {conclusion} (from rule: {rule.name})")

class AgentConfigurationSystem:
    """Rule-based system for dynamic agent configuration"""
    
    def __init__(self):
        self.kb = KnowledgeBase()
        self._setup_rules()
    
    def _setup_rules(self):
        """Define the rule base for agent configuration"""
        
        # TOPOLOGY RULES
        self.kb.add_rule(Rule(
            name="startup_mesh_topology",
            conditions=[
                "project(startup, _, _, _)",
                "team(_, _, SIZE, _)",
                # SIZE <= 6 would need custom logic
            ],
            conclusions=["topology(mesh)", "reason(small_team_needs_flexibility)"],
            priority=10
        ))
        
        self.kb.add_rule(Rule(
            name="enterprise_hierarchical_topology", 
            conditions=[
                "project(enterprise, _, _, _)",
                "team(_, _, SIZE, _)",
                # SIZE > 10 would need custom logic
            ],
            conclusions=["topology(hierarchical)", "reason(large_team_needs_structure)"],
            priority=9
        ))
        
        self.kb.add_rule(Rule(
            name="development_phase_star_topology",
            conditions=[
                "project(_, development, _, _)",
                "workflow(sequential)"
            ],
            conclusions=["topology(star)", "star_center(tech_lead)", "reason(central_coordination_needed)"],
            priority=8
        ))
        
        # POLLING FREQUENCY RULES
        self.kb.add_rule(Rule(
            name="critical_project_fast_polling",
            conditions=[
                "project(_, _, critical, _)"
            ],
            conclusions=["poll_interval(0.5)", "urgent_mode(enabled)", "reason(critical_timeline)"],
            priority=10
        ))
        
        self.kb.add_rule(Rule(
            name="high_activity_agents_fast_polling",
            conditions=[
                "agent(_, _, high)"
            ],
            conclusions=["agent_poll_interval(1.0)", "reason(high_activity_needs_responsiveness)"],
            priority=8
        ))
        
        self.kb.add_rule(Rule(
            name="distributed_team_frequent_polling",
            conditions=[
                "project(_, _, _, distributed)"
            ],
            conclusions=["poll_interval(1.0)", "broadcast_priority(high)", "reason(async_coordination)"],
            priority=7
        ))
        
        # PARTICIPATION LEVEL RULES
        self.kb.add_rule(Rule(
            name="manager_active_participation",
            conditions=[
                "agent(_, manager, _)"
            ],
            conclusions=["participation_level(active)", "can_broadcast(true)", "reason(leadership_role)"],
            priority=9
        ))
        
        self.kb.add_rule(Rule(
            name="intern_observer_participation",
            conditions=[
                "agent(_, intern, _)"
            ],
            conclusions=["participation_level(observer)", "can_broadcast(false)", "reason(learning_role)"],
            priority=8
        ))
        
        self.kb.add_rule(Rule(
            name="designer_assistant_to_frontend",
            conditions=[
                "agent(DESIGNER, designer, _)",
                "agent(FRONTEND, frontend_developer, _)"
            ],
            conclusions=["assists(DESIGNER, FRONTEND)", "participation_level(assistant)", "reason(ui_collaboration)"],
            priority=7
        ))
        
        # BROADCAST RULES
        self.kb.add_rule(Rule(
            name="testing_phase_qa_broadcasts",
            conditions=[
                "project(_, testing, _, _)",
                "agent(_, qa_engineer, _)"
            ],
            conclusions=["broadcast_priority(high)", "topic_focus(testing)", "reason(quality_focus)"],
            priority=8
        ))
        
        self.kb.add_rule(Rule(
            name="deployment_phase_devops_priority",
            conditions=[
                "project(_, deployment, _, _)",
                "agent(_, devops, _)"
            ],
            conclusions=["broadcast_priority(critical)", "immediate_polling(true)", "reason(deployment_critical)"],
            priority=10
        ))
        
        # TEAM COORDINATION RULES
        self.kb.add_rule(Rule(
            name="high_coordination_need_mesh",
            conditions=[
                "team(_, _, _, high)"
            ],
            conclusions=["team_topology(mesh)", "frequent_broadcasts(enabled)", "reason(tight_coordination)"],
            priority=8
        ))
        
        self.kb.add_rule(Rule(
            name="low_coordination_hierarchical",
            conditions=[
                "team(_, _, _, low)"
            ],
            conclusions=["team_topology(hierarchical)", "broadcast_limit(managers_only)", "reason(minimal_overhead)"],
            priority=6
        ))
        
        # WORKFLOW-BASED RULES
        self.kb.add_rule(Rule(
            name="sequential_workflow_linear_topology",
            conditions=[
                "workflow(sequential)"
            ],
            conclusions=["topology(linear)", "handoff_notifications(enabled)", "reason(sequential_dependencies)"],
            priority=7
        ))
        
        self.kb.add_rule(Rule(
            name="parallel_workflow_mesh_topology",
            conditions=[
                "workflow(parallel)"
            ],
            conclusions=["topology(mesh)", "concurrent_broadcasts(enabled)", "reason(parallel_coordination)"],
            priority=7
        ))
    
    def add_agent(self, agent_id: str, role: str, activity_level: str, 
                  domain_expertise: Set[str], team: str = None, reports_to: str = None):
        """Add an agent to the knowledge base"""
        self.kb.add_fact(AgentFact(
            agent_id=agent_id,
            role=role,
            activity_level=activity_level,
            domain_expertise=domain_expertise,
            team=team,
            reports_to=reports_to
        ))
    
    def add_team(self, team_id: str, team_type: str, size: int, coordination_need: str):
        """Add a team to the knowledge base"""
        self.kb.add_fact(TeamFact(
            team_id=team_id,
            team_type=team_type,
            size=size,
            coordination_need=coordination_need
        ))
    
    def add_project_context(self, project_type: str, phase: str, urgency: str, team_distribution: str):
        """Add project context to the knowledge base"""
        self.kb.add_fact(ProjectFact(
            project_type=project_type,
            phase=phase,
            urgency=urgency,
            team_distribution=team_distribution
        ))
    
    def add_workflow(self, workflow_type: str, dependencies: List[Tuple[str, str]] = None):
        """Add workflow information to the knowledge base"""
        self.kb.add_fact(WorkflowFact(
            workflow_type=workflow_type,
            dependencies=dependencies or []
        ))
    
    def generate_configuration(self) -> Dict[str, Any]:
        """Generate configuration based on rules and facts"""
        
        print("RULE-BASED CONFIGURATION GENERATION")
        print("=" * 40)
        
        # Apply inference engine
        print("\nApplying rules...")
        self.kb.infer()
        
        # Extract configuration from derived facts
        config = {
            "topology": self._extract_value("topology"),
            "polling": self._extract_polling_config(),
            "participation": self._extract_participation_config(),
            "broadcasts": self._extract_broadcast_config(),
            "reasoning": self._extract_reasoning()
        }
        
        return config
    
    def _extract_value(self, fact_type: str) -> Optional[str]:
        """Extract a single value from derived facts"""
        for fact in self.kb.derived_facts:
            if fact.startswith(f"{fact_type}("):
                value = fact[fact.find('(')+1:fact.rfind(')')]
                return value
        return None
    
    def _extract_polling_config(self) -> Dict[str, Any]:
        """Extract polling configuration from derived facts"""
        config = {
            "normal_interval": 5.0,  # default
            "urgent_interval": 0.5,  # default
            "urgent_mode": False,
            "immediate_polling": False
        }
        
        for fact in self.kb.derived_facts:
            if fact.startswith("poll_interval("):
                interval = float(fact[fact.find('(')+1:fact.rfind(')')])
                config["normal_interval"] = interval
            elif fact.startswith("urgent_mode(enabled)"):
                config["urgent_mode"] = True
            elif fact.startswith("immediate_polling(true)"):
                config["immediate_polling"] = True
        
        return config
    
    def _extract_participation_config(self) -> Dict[str, Any]:
        """Extract participation configuration from derived facts"""
        config = {
            "default_level": "active",
            "agent_levels": {},
            "assistance_relationships": []
        }
        
        for fact in self.kb.derived_facts:
            if fact.startswith("participation_level("):
                level = fact[fact.find('(')+1:fact.rfind(')')]
                config["default_level"] = level
            elif fact.startswith("assists("):
                # Parse assists(agent1, agent2)
                content = fact[fact.find('(')+1:fact.rfind(')')]
                parts = [p.strip() for p in content.split(',')]
                config["assistance_relationships"].append((parts[0], parts[1]))
        
        return config
    
    def _extract_broadcast_config(self) -> Dict[str, Any]:
        """Extract broadcast configuration from derived facts"""
        config = {
            "priority": "normal",
            "enabled": True,
            "topic_focus": None
        }
        
        for fact in self.kb.derived_facts:
            if fact.startswith("broadcast_priority("):
                priority = fact[fact.find('(')+1:fact.rfind(')')]
                config["priority"] = priority
            elif fact.startswith("topic_focus("):
                topic = fact[fact.find('(')+1:fact.rfind(')')]
                config["topic_focus"] = topic
        
        return config
    
    def _extract_reasoning(self) -> List[str]:
        """Extract reasoning from derived facts"""
        reasons = []
        for fact in self.kb.derived_facts:
            if fact.startswith("reason("):
                reason = fact[fact.find('(')+1:fact.rfind(')')]
                reasons.append(reason)
        return reasons

def demonstrate_rule_based_system():
    """Demonstrate the rule-based configuration system"""
    
    system = AgentConfigurationSystem()
    
    # Scenario 1: Startup in development phase
    print("SCENARIO 1: Startup Development Team")
    print("-" * 35)
    
    # Add project context
    system.add_project_context("startup", "development", "critical", "distributed")
    system.add_workflow("parallel")
    
    # Add team
    system.add_team("dev_team", "development", 5, "high")
    
    # Add agents
    system.add_agent("tech_lead", "manager", "high", {"development", "architecture"}, "dev_team")
    system.add_agent("frontend_dev", "frontend_developer", "high", {"react", "ui"}, "dev_team", "tech_lead")
    system.add_agent("backend_dev", "backend_developer", "high", {"api", "database"}, "dev_team", "tech_lead")
    system.add_agent("designer", "designer", "medium", {"ui", "ux"}, "dev_team")
    system.add_agent("intern", "intern", "low", {"learning"}, "dev_team", "tech_lead")
    
    config1 = system.generate_configuration()
    
    print(f"\nGenerated Configuration:")
    print(f"  Topology: {config1['topology']}")
    print(f"  Polling: {config1['polling']}")
    print(f"  Participation: {config1['participation']}")
    print(f"  Broadcasts: {config1['broadcasts']}")
    print(f"  Reasoning: {', '.join(config1['reasoning'])}")
    
    # Scenario 2: Enterprise in testing phase
    print(f"\n\nSCENARIO 2: Enterprise Testing Phase")
    print("-" * 35)
    
    system2 = AgentConfigurationSystem()
    
    # Add different context
    system2.add_project_context("enterprise", "testing", "normal", "collocated")
    system2.add_workflow("sequential")
    
    # Add larger team
    system2.add_team("qa_team", "qa", 12, "medium")
    
    # Add agents
    system2.add_agent("qa_manager", "manager", "medium", {"testing", "quality"}, "qa_team")
    system2.add_agent("qa_engineer1", "qa_engineer", "high", {"automation", "testing"}, "qa_team", "qa_manager")
    system2.add_agent("qa_engineer2", "qa_engineer", "medium", {"manual_testing"}, "qa_team", "qa_manager")
    system2.add_agent("devops", "devops", "low", {"deployment", "infrastructure"}, "qa_team")
    
    config2 = system2.generate_configuration()
    
    print(f"\nGenerated Configuration:")
    print(f"  Topology: {config2['topology']}")
    print(f"  Polling: {config2['polling']}")
    print(f"  Participation: {config2['participation']}")
    print(f"  Broadcasts: {config2['broadcasts']}")
    print(f"  Reasoning: {', '.join(config2['reasoning'])}")

if __name__ == "__main__":
    demonstrate_rule_based_system()
    
    print("\n\nRULE-BASED SYSTEM FEATURES:")
    print("=" * 30)
    print("• Prolog-style facts and rules")
    print("• Automatic inference engine")
    print("• Context-aware configuration")
    print("• Dynamic topology selection")
    print("• Intelligent polling frequencies")
    print("• Role-based participation levels")
    print("• Workflow-driven coordination")
    print("• Reasoning explanation")
    print("• Extensible rule base")