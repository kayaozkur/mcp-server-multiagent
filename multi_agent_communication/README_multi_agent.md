# Multi-Agent Screen Communication Network

A sophisticated system for enabling bidirectional, non-linear communication between multiple AI agents using GNU Screen sessions as communication channels.

## Architecture Overview

### Core Components

1. **AgentCommunicationNode** - Individual agent with inbox/outbox screen sessions
2. **MultiAgentNetworkManager** - Orchestrates the entire network
3. **Message** - Structured communication protocol
4. **CommunicationPatterns** - Advanced topology implementations

### Communication Flow

```
Agent A ←→ Agent B
   ↕         ↕
Agent D ←→ Agent C
   ↕         ↕
  User ←→ All Agents
```

## Supported Network Topologies

### 1. Linear Communication (2 Agents + User)
```
User ←→ Agent1 ←→ Agent2
```
- Simple bidirectional communication
- Sequential message passing
- User can interact with both agents

### 2. Triangle Communication (3 Agents + User)
```
    User
   ↙ ↓ ↘
Agent1 ←→ Agent2
   ↘     ↙
   Agent3
```
- Each agent communicates with every other agent
- Non-linear, mesh-like topology
- User broadcasts to all

### 3. Full Mesh (4+ Agents)
```
Agent1 ←→ Agent2
  ↕  ╲   ╱  ↕
  ↕   ╲ ╱   ↕
Agent4 ←→ Agent3
```
- Every agent communicates with every other agent
- N*(N-1) communication channels
- Highly redundant and robust

## Advanced Communication Patterns

### Ring Topology
Agents communicate in a circular pattern:
```python
# A1 → A2 → A3 → A4 → A1
CommunicationPatterns.ring_topology(network, "message")
```

### Star Topology
One central agent broadcasts to all others:
```python
# A1 → (A2, A3, A4)
CommunicationPatterns.star_topology_broadcast(network, "agent1", "broadcast")
```

### Hierarchical
Leader-lieutenant-worker structure:
```python
# Leader → Lieutenants → Workers
CommunicationPatterns.hierarchical_communication(network)
```

### Consensus Protocol
Agents vote and reach agreement:
```python
# Proposal → Voting → Consensus
CommunicationPatterns.consensus_protocol(network, "proposal")
```

## Key Features

### Bidirectional Communication
- **Inbox Sessions**: Each agent has a dedicated inbox screen session
- **Outbox Sessions**: Separate outbox for sent message logging
- **Message Listeners**: Background threads monitor incoming messages
- **Response Handlers**: Agents can respond to specific message types

### Non-Linear Topologies
- **Mesh Networks**: Every agent talks to every other agent
- **Dynamic Routing**: Messages can take multiple paths
- **Broadcast Capabilities**: One-to-many communication
- **Selective Communication**: Targeted agent-to-agent messaging

### Scalability Patterns

#### 2 Agents + User
```python
network = MultiAgentNetworkManager()
user = network.add_user()
agent1 = network.add_agent("agent1")
agent2 = network.add_agent("agent2")

# Bidirectional communication
agent1.send_message("agent2", "Hello!")
agent2.send_message("agent1", "Hello back!")
user.broadcast_message("Hello everyone!")
```

#### 4 Agents Full Mesh
```python
# Each agent communicates with 3 others
# Total communication channels: 4 * 3 = 12 directional channels
# Bidirectional pairs: 6 unique pairs

for sender in agents:
    for receiver in agents:
        if sender != receiver:
            sender.send_message(receiver.agent_id, "mesh message")
```

## Advanced Agent Behaviors

### Negotiating Agents
Agents that can make offers, counter-offers, and reach agreements:
```python
agent1.send_message("agent2", "OFFER:100")
# agent2 responds with "COUNTER:110"
# agent1 responds with "ACCEPT"
```

### Collaborative Agents
Agents that work together on distributed tasks:
```python
agent1.send_message("agent2", "TASK_REQUEST:Process data subset A")
agent2.send_message("agent1", "TASK_ACCEPTED:Process data subset A")
# Later: agent2.send_message("agent1", "RESULT:Processed 1000 records")
```

### Competitive Agents
Agents that compete for resources through bidding:
```python
agent1.send_message("agent2", "BID:resource1,50")
agent2.send_message("agent1", "COUNTER_BID:resource1,60")
```

## Technical Implementation

### Screen Session Management
- Each agent gets 2 screen sessions: `{agent_id}_inbox` and `{agent_id}_outbox`
- Messages are injected using `screen -X stuff`
- Content is captured using `screen -X hardcopy`
- Automatic session cleanup on shutdown

### Message Protocol
```json
{
  "id": "uuid",
  "sender": "agent1",
  "recipient": "agent2", 
  "content": "message content",
  "timestamp": "2024-01-01T12:00:00",
  "message_type": "text",
  "metadata": {}
}
```

### Threading Model
- **Main Thread**: Network management and coordination
- **Listener Threads**: One per agent for monitoring incoming messages
- **Handler Threads**: Process messages based on type and content

## Usage Examples

### Basic 2-Agent Setup
```python
from multi_agent_screen_network import *

network = MultiAgentNetworkManager()
user = network.add_user()
agent1 = network.add_agent("agent1")
agent2 = network.add_agent("agent2")

network.start_network()

# Bidirectional communication
agent1.send_message("agent2", "Hello from agent1!")
agent2.send_message("agent1", "Hello back from agent2!")
user.broadcast_message("Hello everyone from user!")

network.stop_network()
```

### 4-Agent Mesh Network
```python
network = MultiAgentNetworkManager()
agents = [network.add_agent(f"agent{i}") for i in range(1, 5)]

network.start_network()

# Full mesh communication
CommunicationPatterns.mesh_discussion(network, "Topic: AI Safety")

network.stop_network()
```

## Benefits

1. **Scalability**: Easily add more agents to the network
2. **Flexibility**: Support for various communication topologies
3. **Persistence**: Screen sessions maintain state across connections
4. **Debugging**: Easy to monitor communication via screen sessions
5. **Isolation**: Each agent operates in its own communication space
6. **Extensibility**: Custom message types and handlers

## Use Cases

- **Multi-Agent AI Systems**: Coordinate multiple AI agents on complex tasks
- **Distributed Computing**: Manage communication between distributed processes
- **Workflow Orchestration**: Coordinate complex multi-step processes
- **Real-time Collaboration**: Enable real-time communication between agents
- **Consensus Systems**: Implement voting and agreement protocols
- **Competitive Simulations**: Model competitive multi-agent environments

This system transforms simple screen sessions into a sophisticated multi-agent communication platform, enabling complex, non-linear interactions between multiple autonomous agents.