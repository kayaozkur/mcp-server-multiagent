#!/usr/bin/env python3
"""
Configuration Variables - All the parameters that can be easily set
"""

from enum import Enum
from typing import Dict, List, Set
from dataclasses import dataclass

# =============================================================================
# CORE SYSTEM CONFIGURATION
# =============================================================================

@dataclass
class SystemConfig:
    """Core system configuration parameters"""
    
    # Session Management
    session_prefix: str = ""                    # Prefix for all screen sessions
    auto_cleanup: bool = True                   # Automatically cleanup sessions on exit
    session_timeout_minutes: int = 30           # Session TTL
    
    # Common Inbox
    enable_common_inbox: bool = True            # Enable global visibility
    common_inbox_name: str = "common_inbox"    # Name of shared session
    
    # Message Management
    message_ttl_minutes: int = 30               # Message time-to-live
    max_message_length: int = 1000              # Maximum message length
    enable_message_ids: bool = True             # Use unique message IDs
    
    # Performance
    temp_directory: str = "/tmp"                # Directory for temp files
    max_concurrent_captures: int = 10           # Max parallel hardcopy operations

# =============================================================================
# POLLING CONFIGURATION
# =============================================================================

@dataclass
class PollingConfig:
    """Polling system configuration"""
    
    # Polling Intervals (seconds)
    normal_poll_interval: float = 5.0          # Normal polling frequency
    urgent_poll_interval: float = 0.5          # Urgent polling frequency
    signal_check_interval: float = 1.0         # How often to check signals
    
    # Polling Behavior
    enable_adaptive_polling: bool = True        # Use adaptive polling speeds
    urgent_mode_duration: int = 10              # Seconds to stay in urgent mode
    max_poll_failures: int = 3                  # Max consecutive poll failures
    
    # Trigger System
    enable_poll_triggers: bool = True           # Use signal-based triggers
    broadcast_triggers_urgent: bool = True      # Broadcasts trigger urgent polling

# =============================================================================
# HIERARCHY CONFIGURATION
# =============================================================================

class Rank(Enum):
    USER = 1        # Highest priority
    LEADER = 2      # Executive level
    MANAGER = 3     # Management level
    WORKER = 4      # Worker level

@dataclass
class HierarchyConfig:
    """Hierarchical communication configuration"""
    
    # Hierarchy Settings
    enable_hierarchy: bool = True               # Use hierarchical permissions
    strict_hierarchy: bool = False              # Enforce strict top-down only
    
    # Visibility Rules (who can see broadcasts from whom)
    visibility_matrix: Dict[Rank, List[Rank]] = None
    
    # Priority Settings
    enable_priority_ordering: bool = True       # Order by sender rank
    user_broadcasts_trump_all: bool = True      # User messages always priority
    
    # Icons for display
    rank_icons: Dict[Rank, str] = None
    
    def __post_init__(self):
        if self.visibility_matrix is None:
            self.visibility_matrix = {
                Rank.USER: [Rank.USER, Rank.LEADER, Rank.MANAGER, Rank.WORKER],
                Rank.LEADER: [Rank.LEADER, Rank.MANAGER, Rank.WORKER],
                Rank.MANAGER: [Rank.MANAGER, Rank.WORKER],
                Rank.WORKER: [Rank.WORKER]
            }
        
        if self.rank_icons is None:
            self.rank_icons = {
                Rank.USER: "👑",
                Rank.LEADER: "⭐", 
                Rank.MANAGER: "🔶",
                Rank.WORKER: "🔸"
            }

# =============================================================================
# PARTICIPATION CONFIGURATION
# =============================================================================

class ParticipationLevel(Enum):
    ACTIVE = "active"           # Full participation
    OBSERVER = "observer"       # Can see all, limited interaction
    ASSISTANT = "assistant"     # Can help specific agents
    SILENT = "silent"          # Can observe, cannot communicate
    SUPPORT = "support"        # Provides help when requested

@dataclass
class ParticipationConfig:
    """Agent participation level configuration"""
    
    # Participation Rules
    participation_rules: Dict[ParticipationLevel, Dict[str, bool]] = None
    
    # Observer Settings
    observers_can_respond: bool = True          # Observers can send limited responses
    observers_see_all_topics: bool = True      # Observers see all communication
    
    # Assistant Settings
    assistants_can_broadcast: bool = False     # Assistants cannot broadcast
    assistants_topic_limited: bool = True      # Assistants limited to specific topics
    
    # Support Settings
    support_on_demand_only: bool = True        # Support agents only act when requested
    support_sees_context: bool = True          # Support agents see relevant context
    
    # Icons for participation levels
    participation_icons: Dict[ParticipationLevel, str] = None
    
    def __post_init__(self):
        if self.participation_rules is None:
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
                    "can_respond": self.observers_can_respond,
                    "can_observe_all": self.observers_see_all_topics,
                    "can_request_help": False
                },
                ParticipationLevel.ASSISTANT: {
                    "can_broadcast": self.assistants_can_broadcast,
                    "can_send_direct": True,
                    "can_respond": True,
                    "can_observe_all": not self.assistants_topic_limited,
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
                    "can_send_direct": True,
                    "can_respond": True,
                    "can_observe_all": self.support_sees_context,
                    "can_request_help": False
                }
            }
        
        if self.participation_icons is None:
            self.participation_icons = {
                ParticipationLevel.ACTIVE: "🟢",
                ParticipationLevel.OBSERVER: "👁️",
                ParticipationLevel.ASSISTANT: "🤝",
                ParticipationLevel.SILENT: "🔇",
                ParticipationLevel.SUPPORT: "🛠️"
            }

# =============================================================================
# TOPOLOGY CONFIGURATION
# =============================================================================

class TopologyType(Enum):
    LINEAR = "linear"           # A1 -> A2 -> A3 -> A4
    RING = "ring"              # A1 -> A2 -> A3 -> A4 -> A1
    STAR = "star"              # Center <-> All others
    MESH = "mesh"              # Everyone <-> Everyone
    HIERARCHICAL = "hierarchical"  # Leader -> Manager -> Worker
    CUSTOM = "custom"          # User-defined topology

@dataclass
class TopologyConfig:
    """Communication topology configuration"""
    
    # Topology Settings
    topology_type: TopologyType = TopologyType.MESH
    dynamic_topology: bool = False              # Allow runtime topology changes
    
    # Star Topology
    star_center_agent: str = "agent1"          # Which agent is center in star
    star_bidirectional: bool = True            # Star allows responses back to center
    
    # Linear/Ring Topology
    linear_order: List[str] = None             # Order of agents in linear chain
    ring_direction: str = "clockwise"          # Direction for ring topology
    
    # Mesh Topology
    mesh_full_connectivity: bool = True        # All agents connect to all others
    mesh_exclude_pairs: List[tuple] = None     # Agent pairs to exclude from mesh
    
    # Hierarchical Topology
    hierarchy_layers: Dict[str, List[str]] = None  # Layer name -> agents in layer
    cross_layer_communication: bool = False    # Allow communication across layers
    
    # Custom Topology
    custom_connections: Dict[str, List[str]] = None  # agent -> list of agents they can send to

# =============================================================================
# LOOP PREVENTION CONFIGURATION
# =============================================================================

@dataclass
class LoopPreventionConfig:
    """Loop prevention system configuration"""
    
    # Response Limits
    max_responses_per_thread: int = 2          # Max responses in conversation thread
    max_total_responses: int = 10              # Max total responses per agent
    
    # Deduplication
    enable_content_hashing: bool = True        # Use content hashes for dedup
    hash_algorithm: str = "md5"                # Hash algorithm to use
    ignore_case_in_hash: bool = True           # Case-insensitive hashing
    
    # Echo Prevention
    prevent_self_echo: bool = True             # Agents can't respond to themselves
    prevent_immediate_echo: bool = True        # Prevent A->B->A immediate loops
    
    # Auto-Response Filtering
    auto_response_keywords: List[str] = None   # Keywords that don't trigger responses
    enable_ack_filtering: bool = True          # Filter acknowledgment messages
    
    # Timing Controls
    min_response_delay_seconds: float = 0.1    # Minimum time between responses
    response_cooldown_seconds: float = 5.0     # Cooldown after rapid responses
    
    def __post_init__(self):
        if self.auto_response_keywords is None:
            self.auto_response_keywords = ["ACK", "OK", "RECEIVED", "CONFIRMED", "ROGER"]

# =============================================================================
# TOPIC CONFIGURATION
# =============================================================================

@dataclass
class TopicConfig:
    """Topic-based communication configuration"""
    
    # Topic Settings
    enable_topics: bool = True                 # Use topic-based communication
    default_topic: str = "general"            # Default topic for messages
    
    # Predefined Topics
    standard_topics: Set[str] = None           # Standard topics available
    allow_custom_topics: bool = True           # Allow creation of new topics
    
    # Topic Permissions
    topic_visibility: Dict[str, List[str]] = None      # topic -> agents who can see
    topic_participation: Dict[str, List[str]] = None   # topic -> agents who can participate
    
    # Topic Behavior
    topic_isolation: bool = False              # Topics are completely isolated
    cross_topic_references: bool = True        # Allow references between topics
    
    def __post_init__(self):
        if self.standard_topics is None:
            self.standard_topics = {
                "general", "development", "design", "testing", 
                "deployment", "planning", "support", "emergency"
            }

# =============================================================================
# MASTER CONFIGURATION CLASS
# =============================================================================

@dataclass
class MasterConfig:
    """Master configuration containing all system settings"""
    
    # Core Components
    system: SystemConfig = None
    polling: PollingConfig = None
    hierarchy: HierarchyConfig = None
    participation: ParticipationConfig = None
    topology: TopologyConfig = None
    loop_prevention: LoopPreventionConfig = None
    topics: TopicConfig = None
    
    # Agent Settings
    agent_list: List[str] = None               # List of agent IDs
    enable_user_agent: bool = True             # Include special user agent
    user_agent_id: str = "user"               # ID for user agent
    
    # Feature Toggles
    enable_broadcasts: bool = True             # Allow broadcast messages
    enable_direct_messages: bool = True        # Allow direct messages
    enable_assistance_requests: bool = True    # Allow help requests
    enable_network_monitoring: bool = True     # Allow network observation
    
    # Debugging & Logging
    debug_mode: bool = False                   # Enable debug output
    log_all_messages: bool = True              # Log all communications
    log_session_operations: bool = False       # Log screen session ops
    verbose_permissions: bool = False          # Verbose permission checking
    
    def __post_init__(self):
        # Initialize sub-configs with defaults if not provided
        if self.system is None:
            self.system = SystemConfig()
        if self.polling is None:
            self.polling = PollingConfig()
        if self.hierarchy is None:
            self.hierarchy = HierarchyConfig()
        if self.participation is None:
            self.participation = ParticipationConfig()
        if self.topology is None:
            self.topology = TopologyConfig()
        if self.loop_prevention is None:
            self.loop_prevention = LoopPreventionConfig()
        if self.topics is None:
            self.topics = TopicConfig()
        
        # Default agent list
        if self.agent_list is None:
            self.agent_list = ["agent1", "agent2", "agent3", "agent4"]
    
    def get_total_sessions_needed(self) -> int:
        """Calculate total sessions needed for current configuration"""
        agent_count = len(self.agent_list)
        if self.enable_user_agent:
            agent_count += 1
        
        # Personal sessions: 3 per agent (inbox, outbox, signals)
        personal_sessions = agent_count * 3
        
        # Shared sessions
        shared_sessions = 1 if self.system.enable_common_inbox else 0
        
        return personal_sessions + shared_sessions
    
    def validate_configuration(self) -> List[str]:
        """Validate configuration and return list of issues"""
        issues = []
        
        # Check agent list
        if not self.agent_list:
            issues.append("Agent list cannot be empty")
        
        if len(set(self.agent_list)) != len(self.agent_list):
            issues.append("Agent IDs must be unique")
        
        # Check topology configuration
        if self.topology.topology_type == TopologyType.STAR:
            if self.topology.star_center_agent not in self.agent_list:
                issues.append(f"Star center agent '{self.topology.star_center_agent}' not in agent list")
        
        # Check hierarchy configuration
        if self.hierarchy.enable_hierarchy and self.topology.topology_type == TopologyType.HIERARCHICAL:
            if not self.hierarchy.visibility_matrix:
                issues.append("Hierarchical topology requires visibility matrix")
        
        # Check polling configuration
        if self.polling.normal_poll_interval <= 0:
            issues.append("Normal poll interval must be positive")
        
        if self.polling.urgent_poll_interval >= self.polling.normal_poll_interval:
            issues.append("Urgent poll interval should be less than normal interval")
        
        return issues

def create_default_config() -> MasterConfig:
    """Create a default configuration for quick setup"""
    return MasterConfig()

def create_simple_config(agents: List[str]) -> MasterConfig:
    """Create a simple configuration with basic settings"""
    return MasterConfig(
        agent_list=agents,
        topology=TopologyConfig(topology_type=TopologyType.MESH),
        hierarchy=HierarchyConfig(enable_hierarchy=False),
        participation=ParticipationConfig(),
        debug_mode=False
    )

def create_hierarchical_config(agents: List[str], user_agent: str = "user") -> MasterConfig:
    """Create a hierarchical configuration"""
    return MasterConfig(
        agent_list=agents,
        user_agent_id=user_agent,
        topology=TopologyConfig(topology_type=TopologyType.HIERARCHICAL),
        hierarchy=HierarchyConfig(enable_hierarchy=True),
        participation=ParticipationConfig(),
        enable_broadcasts=True
    )

if __name__ == "__main__":
    # Example: Create and validate a configuration
    config = create_default_config()
    issues = config.validate_configuration()
    
    print("DEFAULT CONFIGURATION")
    print("=" * 25)
    print(f"Agents: {config.agent_list}")
    print(f"Total sessions needed: {config.get_total_sessions_needed()}")
    print(f"Topology: {config.topology.topology_type.value}")
    print(f"Hierarchy enabled: {config.hierarchy.enable_hierarchy}")
    print(f"Common inbox: {config.system.enable_common_inbox}")
    
    if issues:
        print(f"\nConfiguration issues: {issues}")
    else:
        print("\n✓ Configuration is valid")
    
    print("\nCONFIGURABLE PARAMETERS:")
    print("=" * 25)
    print("• System: Session management, common inbox, message TTL")
    print("• Polling: Intervals, adaptive polling, triggers")
    print("• Hierarchy: Ranks, visibility rules, priorities")
    print("• Participation: Active, observer, assistant, silent, support")
    print("• Topology: Linear, ring, star, mesh, hierarchical, custom")
    print("• Loop Prevention: Response limits, deduplication, echo prevention")
    print("• Topics: Topic-based communication, permissions")
    print("• Features: Broadcasts, direct messages, assistance, monitoring")