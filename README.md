# @lepion/mcp-server-multiagent

[![npm version](https://img.shields.io/npm/v/@lepion/mcp-server-multiagent.svg)](https://www.npmjs.com/package/@lepion/mcp-server-multiagent)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D18-brightgreen)](https://nodejs.org/)

A Model Context Protocol (MCP) server that provides intelligent multi-agent communication system management. This server enables AI assistants like Claude to coordinate complex multi-agent workflows, manage distributed agent networks, and orchestrate collaborative AI systems.

---

## 🌟 Overview

The Multi-Agent MCP Server provides access to 99+ functionalities from a comprehensive multi-agent system, enabling sophisticated agent coordination patterns including screen-based communication, various network topologies, and distributed intelligence capabilities.

## Features

### Core Capabilities
- 🤖 **Multi-Agent Coordination**: Manage networks of AI agents with different roles and permissions
- 📡 **Communication Patterns**: Support for broadcast, multicast, and point-to-point messaging
- 🔗 **Network Topologies**: Linear, ring, star, mesh, and hierarchical agent configurations
- 🖥️ **Screen Session Management**: Unix screen-based agent isolation and communication
- 📊 **Monitoring & Analytics**: Real-time agent network monitoring and performance metrics
- 🛡️ **Role-Based Access Control**: Fine-grained permissions for different agent types
- 🔄 **Dynamic Configuration**: Runtime topology changes and agent role modifications
- 📦 **Message Queue Management**: Inbox systems for asynchronous agent communication

### Intelligent Features
- 🧠 **Workflow Generation**: Automatically generate multi-agent workflow examples
- 🎯 **Smart Search**: Find functionalities by keywords, use cases, or patterns
- 📈 **Complexity Analysis**: Assess computational requirements for agent networks
- 🔍 **Functionality Discovery**: Browse 99+ capabilities across 19 categories
- 💡 **Session Estimation**: Calculate required screen sessions for agent deployments
- 🏗️ **Architecture Patterns**: Pre-built patterns for common multi-agent scenarios

## Installation

```bash
# Install from npm
npm install -g @lepion/mcp-server-multiagent

# Or clone the repository for development
git clone https://github.com/lepion/mcp-server-multiagent.git
cd mcp-server-multiagent

# Install dependencies
npm install

# Build the TypeScript code
npm run build

# Parse and generate functionality database
npm run parse-agents
```

## Configuration

### Claude Desktop Integration

Add the server to your Claude Desktop configuration file (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "multiagent": {
      "command": "node",
      "args": ["/path/to/mcp-server-multiagent/dist/index.js"],
      "env": {
        "LOG_LEVEL": "info"
      }
    }
  }
}
```

### Environment Variables

```env
# Optional: Log level (debug, info, warn, error)
LOG_LEVEL=info

# Optional: Path to multi-agent system (defaults to standard location)
MULTIAGENT_PATH=/path/to/multi_agent_communication
```

## Available Tools

### 1. `multiagent_get_functionality_info`
Get detailed information about a specific multi-agent functionality.

**Parameters:**
- `functionality` (string, required): Name of the functionality (e.g., 'MultiAgentNetworkManager', 'send_message')
- `include_examples` (boolean, optional): Include usage examples and code snippets (default: true)

**Example:**
```json
{
  "functionality": "MultiAgentNetworkManager",
  "include_examples": true
}
```

### 2. `multiagent_search_functionalities`
Search for functionalities by keywords, use cases, or patterns.

**Parameters:**
- `query` (string, required): Search query
- `category` (string, optional): Filter by category
- `max_results` (number, optional): Maximum results to return (default: 10)

**Categories:** agents, broadcasting, communication, configuration, dependencies, hierarchy, inbox, messaging, monitoring, permissions, roles, rules, screen, topology, triggers

### 3. `multiagent_get_functionalities_by_category`
Get all functionalities in a specific category.

**Parameters:**
- `category` (string, required): One of the available categories

### 4. `multiagent_get_functionalities_by_type`
Get functionalities by implementation type.

**Parameters:**
- `type` (string, required): Implementation type (class, function, constant)

### 5. `multiagent_get_functionalities_by_complexity`
Get functionalities filtered by complexity level.

**Parameters:**
- `complexity` (string, required): Complexity level (low, moderate, high)

### 6. `multiagent_get_functionalities_by_file`
Get all functionalities from a specific Python file.

**Parameters:**
- `filename` (string, required): Python filename (e.g., 'multi_agent_screen_network.py')

### 7. `multiagent_get_network_topologies`
Get available network communication topologies and their characteristics.

### 8. `multiagent_get_agent_roles`
Get available agent roles and their permissions.

### 9. `multiagent_estimate_session_count`
Estimate required screen sessions for a multi-agent setup.

**Parameters:**
- `agent_count` (number, required): Number of agents
- `topology` (string, required): Network topology type

### 10. `multiagent_generate_workflow_example`
Generate complete workflow example with setup, execution, and cleanup.

**Parameters:**
- `agent_count` (number, required): Number of agents
- `topology` (string, required): Communication topology
- `use_case` (string, required): Specific use case description

### 11. `multiagent_get_database_stats`
Get comprehensive statistics about the multi-agent functionality database.

## Examples

### Example 1: Basic Agent Network Setup

```javascript
// Search for network management capabilities
{
  "tool": "multiagent_search_functionalities",
  "arguments": {
    "query": "network manager",
    "category": "agents"
  }
}

// Get detailed information about the network manager
{
  "tool": "multiagent_get_functionality_info",
  "arguments": {
    "functionality": "MultiAgentNetworkManager"
  }
}

// Generate a workflow example
{
  "tool": "multiagent_generate_workflow_example",
  "arguments": {
    "agent_count": 5,
    "topology": "star",
    "use_case": "Distributed task processing with central coordinator"
  }
}
```

### Example 2: Communication Pattern Discovery

```javascript
// Find broadcast communication patterns
{
  "tool": "multiagent_search_functionalities",
  "arguments": {
    "query": "broadcast",
    "category": "communication"
  }
}

// Get all messaging functionalities
{
  "tool": "multiagent_get_functionalities_by_category",
  "arguments": {
    "category": "messaging"
  }
}
```

### Example 3: Complex Multi-Agent Orchestration

```javascript
// Estimate session requirements
{
  "tool": "multiagent_estimate_session_count",
  "arguments": {
    "agent_count": 10,
    "topology": "hierarchical"
  }
}

// Get high-complexity functionalities
{
  "tool": "multiagent_get_functionalities_by_complexity",
  "arguments": {
    "complexity": "high"
  }
}
```

## Use Cases

### 1. Distributed Intelligence Networks
Create networks of specialized AI agents that collaborate on complex tasks:
- Research agents gathering information
- Analysis agents processing data
- Synthesis agents creating reports
- Coordination agents managing workflows

### 2. Autonomous System Coordination
Manage autonomous systems with different capabilities:
- Sensor agents collecting environmental data
- Decision agents processing information
- Action agents executing commands
- Monitor agents ensuring system health

### 3. Multi-Modal AI Pipelines
Orchestrate pipelines with agents handling different modalities:
- Vision agents processing images
- Language agents handling text
- Audio agents managing sound
- Integration agents combining outputs

### 4. Collaborative Problem Solving
Deploy agent teams for complex problem-solving:
- Explorer agents searching solution spaces
- Evaluator agents testing solutions
- Optimizer agents improving results
- Reporter agents documenting findings

## Architecture Overview

### System Components

```
┌─────────────────────────────────────────────────────────┐
│                   MCP Server Layer                       │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │   Tools     │  │   Client     │  │   Database    │  │
│  │  Handlers   │  │  Interface   │  │   99+ Funcs   │  │
│  └─────────────┘  └──────────────┘  └───────────────┘  │
└─────────────────────────────────────────────────────────┘
                            │
┌─────────────────────────────────────────────────────────┐
│                Multi-Agent System Layer                  │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │   Screen    │  │   Network    │  │  Message      │  │
│  │  Sessions   │  │  Topologies  │  │   Queues      │  │
│  └─────────────┘  └──────────────┘  └───────────────┘  │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │    Agent    │  │    Role      │  │  Monitoring   │  │
│  │   Managers  │  │   Control    │  │   System      │  │
│  └─────────────┘  └──────────────┘  └───────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Communication Flow

1. **MCP Client** (e.g., Claude) sends requests to the MCP Server
2. **Tool Handlers** process requests and interact with the Multi-Agent Client
3. **Multi-Agent Client** manages the functionality database and coordinates operations
4. **Generated Database** contains 99+ functionalities parsed from 19 Python files
5. **Response Formation** structures data for optimal AI understanding

### Key Design Principles

- **Modularity**: Each agent operates independently with well-defined interfaces
- **Scalability**: Support for networks from 2 to 100+ agents
- **Flexibility**: Runtime configuration changes without system restart
- **Reliability**: Built-in error handling and recovery mechanisms
- **Security**: Role-based access control and secure communication channels

## Development

### Building from Source

```bash
# Clone the repository
git clone https://github.com/lepion/mcp-server-multiagent.git
cd mcp-server-multiagent

# Install dependencies
npm install

# Build TypeScript
npm run build

# Parse multi-agent system (updates functionality database)
npm run parse-agents

# Run in development mode
npm run dev
```

### Running Tests

```bash
# Run Jest tests
npm test

# Run linting
npm run lint

# Format code
npm run format
```

### Project Structure

```
mcp-server-multiagent/
├── src/
│   ├── index.ts              # Main server entry point
│   ├── tools.ts              # Tool handler implementations
│   ├── multiagent-client.ts  # Multi-agent system client
│   ├── logger.ts             # Logging utilities
│   └── generated-multiagent.ts # Generated functionality database
├── scripts/
│   └── parse-multiagent-system.cjs # Parser for Python files
├── dist/                     # Compiled JavaScript
├── package.json             # Project configuration
└── tsconfig.json           # TypeScript configuration
```

## Troubleshooting

### Common Issues

1. **"Functionality not found" error**
   - Check spelling of functionality name
   - Use search tool to find similar functionalities
   - Browse by category to discover available options

2. **"Failed to parse agents" error**
   - Ensure Python files are in the correct location
   - Check file permissions
   - Run `npm run parse-agents` manually

3. **Performance issues with large agent networks**
   - Use appropriate topology for your use case
   - Consider complexity ratings when selecting functionalities
   - Monitor resource usage with built-in tools

4. **Screen session errors**
   - Ensure GNU Screen is installed on your system
   - Check user permissions for screen operations
   - Verify session count estimates before deployment

### Debug Mode

Enable detailed logging:

```bash
export LOG_LEVEL=debug
npm start
```

### Getting Help

- Check the [documentation](https://github.com/lepion/mcp-server-multiagent/docs)
- Browse examples in the `/examples` directory
- Search functionalities using the built-in tools
- Open an issue on GitHub for bugs or feature requests

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built on the [Model Context Protocol](https://modelcontextprotocol.io)
- Inspired by distributed systems research and multi-agent architectures
- Special thanks to the MCP community for feedback and contributions

---

**Note**: This server requires access to the multi-agent communication system Python files. Ensure the path is correctly configured in your environment.