#!/usr/bin/env node

/**
 * MCP Multi-Agent Communication Server
 * Intelligent multi-agent system management and coordination
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ErrorCode,
  ListToolsRequestSchema,
  McpError,
} from "@modelcontextprotocol/sdk/types.js";
import { logger } from "./logger.js";
import { MultiAgentClient } from "./multiagent-client.js";
import { toolHandlers } from "./tools.js";

const server = new Server(
  {
    name: "multiagent-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Initialize Multi-Agent client
const multiAgentClient = new MultiAgentClient();

// List available tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "multiagent_get_functionality_info",
        description: "Get comprehensive information about multi-agent system functionalities from 99+ components",
        inputSchema: {
          type: "object",
          properties: {
            functionality: {
              type: "string",
              description: "Multi-agent functionality name (e.g., 'MultiAgentNetworkManager', 'send_message', 'ring_topology')",
            },
            include_examples: {
              type: "boolean",
              description: "Include usage examples and code snippets",
              default: true,
            }
          },
          required: ["functionality"],
        },
      },
      {
        name: "multiagent_search_functionalities",
        description: "Search for multi-agent functionalities by keywords, use cases, or patterns",
        inputSchema: {
          type: "object",
          properties: {
            query: {
              type: "string",
              description: "Search query (e.g., 'broadcast communication', 'topology management', 'screen sessions')",
            },
            category: {
              type: "string",
              description: "Functionality category filter",
              enum: ["agents", "broadcasting", "communication", "configuration", "dependencies", "hierarchy", "inbox", "messaging", "monitoring", "permissions", "roles", "rules", "screen", "topology", "triggers", "all"],
              default: "all",
            },
            max_results: {
              type: "number",
              description: "Maximum number of results to return",
              default: 10,
            }
          },
          required: ["query"],
        },
      },
      {
        name: "multiagent_get_functionalities_by_category",
        description: "Get all functionalities in a specific category",
        inputSchema: {
          type: "object",
          properties: {
            category: {
              type: "string",
              description: "Functionality category",
              enum: ["agents", "broadcasting", "communication", "configuration", "dependencies", "hierarchy", "inbox", "messaging", "monitoring", "permissions", "roles", "rules", "screen", "topology", "triggers"],
            }
          },
          required: ["category"],
        },
      },
      {
        name: "multiagent_get_functionalities_by_type",
        description: "Get all functionalities by implementation type",
        inputSchema: {
          type: "object",
          properties: {
            type: {
              type: "string",
              description: "Implementation type",
              enum: ["class", "function", "constant"],
            }
          },
          required: ["type"],
        },
      },
      {
        name: "multiagent_get_functionalities_by_complexity",
        description: "Get functionalities by complexity level",
        inputSchema: {
          type: "object",
          properties: {
            complexity: {
              type: "string",
              description: "Complexity level",
              enum: ["low", "moderate", "high"],
            }
          },
          required: ["complexity"],
        },
      },
      {
        name: "multiagent_get_functionalities_by_file",
        description: "Get all functionalities from a specific Python file",
        inputSchema: {
          type: "object",
          properties: {
            filename: {
              type: "string",
              description: "Python filename (e.g., 'multi_agent_screen_network.py', 'communication_patterns.py')",
            }
          },
          required: ["filename"],
        },
      },
      {
        name: "multiagent_get_network_topologies",
        description: "Get available network communication topologies and their characteristics",
        inputSchema: {
          type: "object",
          properties: {},
        },
      },
      {
        name: "multiagent_get_agent_roles",
        description: "Get available agent roles and their permissions",
        inputSchema: {
          type: "object",
          properties: {},
        },
      },
      {
        name: "multiagent_estimate_session_count",
        description: "Estimate required screen sessions for a multi-agent setup",
        inputSchema: {
          type: "object",
          properties: {
            agent_count: {
              type: "number",
              description: "Number of agents in the network",
              minimum: 1,
            },
            topology: {
              type: "string",
              description: "Network topology type",
              enum: ["linear", "ring", "star", "mesh", "hierarchical"],
            }
          },
          required: ["agent_count", "topology"],
        },
      },
      {
        name: "multiagent_generate_workflow_example",
        description: "Generate complete workflow example with setup, execution, and cleanup",
        inputSchema: {
          type: "object",
          properties: {
            agent_count: {
              type: "number",
              description: "Number of agents in the workflow",
              minimum: 2,
            },
            topology: {
              type: "string",
              description: "Communication topology",
              enum: ["linear", "ring", "star", "mesh", "hierarchical"],
            },
            use_case: {
              type: "string",
              description: "Specific use case or task description",
            }
          },
          required: ["agent_count", "topology", "use_case"],
        },
      },
      {
        name: "multiagent_get_database_stats",
        description: "Get comprehensive statistics about the multi-agent functionality database",
        inputSchema: {
          type: "object",
          properties: {},
        },
      }
    ],
  };
});

// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    logger.info(`Executing multi-agent tool: ${name}`, { args });

    let result: any;
    switch (name) {
      case "multiagent_get_functionality_info":
        result = await toolHandlers.getFunctionalityInfo(multiAgentClient, args);
        break;
      case "multiagent_search_functionalities":
        result = await toolHandlers.searchFunctionalities(multiAgentClient, args);
        break;
      case "multiagent_get_functionalities_by_category":
        result = await toolHandlers.getFunctionalitiesByCategory(multiAgentClient, args);
        break;
      case "multiagent_get_functionalities_by_type":
        result = await toolHandlers.getFunctionalitiesByType(multiAgentClient, args);
        break;
      case "multiagent_get_functionalities_by_complexity":
        result = await toolHandlers.getFunctionalitiesByComplexity(multiAgentClient, args);
        break;
      case "multiagent_get_functionalities_by_file":
        result = await toolHandlers.getFunctionalitiesByFile(multiAgentClient, args);
        break;
      case "multiagent_get_network_topologies":
        result = await toolHandlers.getNetworkTopologies(multiAgentClient, args);
        break;
      case "multiagent_get_agent_roles":
        result = await toolHandlers.getAgentRoles(multiAgentClient, args);
        break;
      case "multiagent_estimate_session_count":
        result = await toolHandlers.estimateSessionCount(multiAgentClient, args);
        break;
      case "multiagent_generate_workflow_example":
        result = await toolHandlers.generateWorkflowExample(multiAgentClient, args);
        break;
      case "multiagent_get_database_stats":
        result = await toolHandlers.getDatabaseStats(multiAgentClient, args);
        break;
      default:
        throw new McpError(ErrorCode.MethodNotFound, `Unknown multi-agent tool: ${name}`);
    }

    return {
      content: [
        {
          type: "text",
          text: JSON.stringify(result, null, 2),
        },
      ],
    };
  } catch (error) {
    logger.error(`Error executing multi-agent tool ${name}:`, error);
    throw new McpError(
      ErrorCode.InternalError,
      `Multi-agent tool execution failed: ${error instanceof Error ? error.message : String(error)}`
    );
  }
});

// Start server
async function main() {
  try {
    const transport = new StdioServerTransport();
    await server.connect(transport);
    logger.info("Multi-Agent MCP Server started successfully");
  } catch (error) {
    logger.error("Failed to start multi-agent server:", error);
    process.exit(1);
  }
}

main();