/**
 * Enhanced Multi-Agent Communication Client
 * Comprehensive multi-agent system management with 99+ functionalities from 19 Python files
 */

import { logger } from "./logger.js";
import { MULTIAGENT_FUNCTIONALITIES, TOTAL_FUNCTIONALITIES } from "./generated-multiagent.js";
import * as fs from 'fs';
import * as path from 'path';

export interface MultiAgentFunctionality {
  name: string;
  description: string;
  type: "class" | "function" | "constant";
  category: string;
  filename: string;
  class: string | null;
  usage_pattern: string;
  examples: string[];
  alternatives: string[];
  requirements: string[];
  dependencies: string[];
  safety_level: "safe" | "moderate" | "dangerous";
  complexity: "low" | "moderate" | "high";
  methods: any[];
}

export interface NetworkTopology {
  name: string;
  description: string;
  use_cases: string[];
  session_count: number;
  complexity: string;
}

export interface AgentRole {
  name: string;
  permissions: string[];
  description: string;
  communication_level: string;
}

export class MultiAgentClient {
  private functionalityDatabase: Map<string, MultiAgentFunctionality>;
  private categoryIndex: Map<string, MultiAgentFunctionality[]>;
  private typeIndex: Map<string, MultiAgentFunctionality[]>;
  private lastUpdate: Date;
  private multiAgentPath: string;

  constructor() {
    this.functionalityDatabase = new Map();
    this.categoryIndex = new Map();
    this.typeIndex = new Map();
    this.lastUpdate = new Date();
    this.multiAgentPath = '/Users/kayaozkur/Desktop/lepion/multi_agent_communication';
    this.initializeFunctionalityDatabase();
    
    // Set up periodic refresh for dynamic updates
    this.startPeriodicRefresh();
  }

  private initializeFunctionalityDatabase() {
    // Use comprehensive functionality database generated from all Python files
    const functionalities: MultiAgentFunctionality[] = MULTIAGENT_FUNCTIONALITIES as MultiAgentFunctionality[];

    // Clear existing data
    this.functionalityDatabase.clear();
    this.categoryIndex.clear();
    this.typeIndex.clear();

    // Initialize functionality database
    functionalities.forEach(func => {
      this.functionalityDatabase.set(func.name.toLowerCase(), func);
      
      // Build category index
      if (!this.categoryIndex.has(func.category)) {
        this.categoryIndex.set(func.category, []);
      }
      this.categoryIndex.get(func.category)!.push(func);
      
      // Build type index
      if (!this.typeIndex.has(func.type)) {
        this.typeIndex.set(func.type, []);
      }
      this.typeIndex.get(func.type)!.push(func);
    });

    this.lastUpdate = new Date();
    logger.info(`Initialized comprehensive multi-agent database with ${functionalities.length} functionalities (${TOTAL_FUNCTIONALITIES} total) from 19 Python files`);
  }

  private startPeriodicRefresh() {
    // Check for updates every 5 minutes
    setInterval(() => {
      this.checkForUpdates();
    }, 5 * 60 * 1000);
    
    logger.info('Started periodic refresh monitoring for multi-agent system updates');
  }

  private async checkForUpdates() {
    try {
      // Check if any Python files have been modified
      const pythonFiles = fs.readdirSync(this.multiAgentPath)
        .filter(file => file.endsWith('.py'));

      let hasUpdates = false;
      for (const file of pythonFiles) {
        const filePath = path.join(this.multiAgentPath, file);
        if (fs.existsSync(filePath)) {
          const stats = fs.statSync(filePath);
          if (stats.mtime > this.lastUpdate) {
            hasUpdates = true;
            break;
          }
        }
      }

      if (hasUpdates) {
        logger.info('Multi-agent Python files updated, regenerating functionality database...');
        await this.regenerateFunctionalityDatabase();
      }
    } catch (error) {
      logger.error('Error checking for multi-agent updates:', error);
    }
  }

  private async regenerateFunctionalityDatabase() {
    try {
      // Execute the parser script to regenerate functionalities
      const { exec } = await import('child_process');
      const { promisify } = await import('util');
      const execAsync = promisify(exec);
      
      await execAsync('node scripts/parse-multiagent-system.cjs', { 
        cwd: '/Users/kayaozkur/Desktop/lepion/mcp-multiagent-server' 
      });
      
      // Reload the generated functionalities module
      delete require.cache[require.resolve('./generated-multiagent.js')];
      const { MULTIAGENT_FUNCTIONALITIES: newFunctionalities } = await import('./generated-multiagent.js');
      
      // Reinitialize with new data
      this.initializeFunctionalityDatabase();
      
      logger.info('Successfully updated multi-agent functionality database with latest changes');
    } catch (error) {
      logger.error('Error regenerating multi-agent functionality database:', error);
    }
  }

  async getFunctionalityInfo(name: string, includeExamples: boolean = true): Promise<MultiAgentFunctionality | null> {
    const targetName = name.toLowerCase();
    const func = this.functionalityDatabase.get(targetName);
    
    if (!func) {
      logger.warn(`Multi-agent functionality not found: ${name}`);
      return null;
    }

    const result = { ...func };
    if (!includeExamples) {
      result.examples = [];
    }

    return result;
  }

  async searchFunctionalities(query: string, category: string = "all", maxResults: number = 10): Promise<MultiAgentFunctionality[]> {
    const results: MultiAgentFunctionality[] = [];
    const queryLower = query.toLowerCase();

    for (const [name, func] of this.functionalityDatabase) {
      if (results.length >= maxResults) break;
      
      const matchesCategory = category === "all" || func.category === category;
      const matchesQuery = 
        name.includes(queryLower) ||
        func.description.toLowerCase().includes(queryLower) ||
        func.examples.some(ex => ex.toLowerCase().includes(queryLower)) ||
        func.usage_pattern.toLowerCase().includes(queryLower) ||
        func.filename.toLowerCase().includes(queryLower);

      if (matchesCategory && matchesQuery) {
        results.push(func);
      }
    }

    // Sort by relevance (exact matches first, then partial matches)
    results.sort((a, b) => {
      const aExact = a.name.toLowerCase() === queryLower;
      const bExact = b.name.toLowerCase() === queryLower;
      if (aExact && !bExact) return -1;
      if (!aExact && bExact) return 1;
      return 0;
    });

    logger.info(`Multi-agent search query "${query}" returned ${results.length} results`);
    return results;
  }

  async getFunctionalitiesByCategory(category: string): Promise<MultiAgentFunctionality[]> {
    const functionalities = this.categoryIndex.get(category) || [];
    return functionalities.sort((a, b) => a.name.localeCompare(b.name));
  }

  async getFunctionalitiesByType(type: string): Promise<MultiAgentFunctionality[]> {
    const functionalities = this.typeIndex.get(type) || [];
    return functionalities.sort((a, b) => a.name.localeCompare(b.name));
  }

  async getFunctionalitiesByComplexity(complexity: string): Promise<MultiAgentFunctionality[]> {
    const functionalities: MultiAgentFunctionality[] = [];
    
    for (const [name, func] of this.functionalityDatabase) {
      if (func.complexity === complexity) {
        functionalities.push(func);
      }
    }
    
    return functionalities.sort((a, b) => a.name.localeCompare(b.name));
  }

  async getFunctionalitiesByFile(filename: string): Promise<MultiAgentFunctionality[]> {
    const functionalities: MultiAgentFunctionality[] = [];
    
    for (const [name, func] of this.functionalityDatabase) {
      if (func.filename === filename) {
        functionalities.push(func);
      }
    }
    
    return functionalities.sort((a, b) => a.name.localeCompare(b.name));
  }

  getStats(): { 
    totalFunctionalities: number; 
    categories: string[]; 
    types: string[];
    complexityLevels: Record<string, number>;
    safetyLevels: Record<string, number>;
    fileCount: number;
    lastUpdate: Date;
  } {
    const categories = [...this.categoryIndex.keys()].sort();
    const types = [...this.typeIndex.keys()].sort();
    
    const complexityLevels = Array.from(this.functionalityDatabase.values()).reduce((acc, func) => {
      acc[func.complexity] = (acc[func.complexity] || 0) + 1;
      return acc;
    }, {} as Record<string, number>);
    
    const safetyLevels = Array.from(this.functionalityDatabase.values()).reduce((acc, func) => {
      acc[func.safety_level] = (acc[func.safety_level] || 0) + 1;
      return acc;
    }, {} as Record<string, number>);
    
    const uniqueFiles = new Set(Array.from(this.functionalityDatabase.values()).map(f => f.filename));

    return {
      totalFunctionalities: this.functionalityDatabase.size,
      categories,
      types,
      complexityLevels,
      safetyLevels,
      fileCount: uniqueFiles.size,
      lastUpdate: this.lastUpdate
    };
  }

  // Network topology management
  async getNetworkTopologies(): Promise<NetworkTopology[]> {
    return [
      {
        name: "Linear Chain",
        description: "Sequential communication: A1 → A2 → A3 → A4",
        use_cases: ["Pipeline processing", "Sequential workflows", "Data transformation chains"],
        session_count: 3, // N agents * 3 sessions per agent
        complexity: "low"
      },
      {
        name: "Ring Topology", 
        description: "Circular communication: A1 → A2 → A3 → A4 → A1",
        use_cases: ["Token passing", "Consensus protocols", "Circular workflows"],
        session_count: 3,
        complexity: "moderate"
      },
      {
        name: "Star Topology",
        description: "Central hub broadcasts to all: Central ↔ All others",
        use_cases: ["Centralized coordination", "Command distribution", "Status collection"],
        session_count: 3,
        complexity: "low"
      },
      {
        name: "Full Mesh",
        description: "Every agent communicates with every other: N*(N-1) channels",
        use_cases: ["Collaborative decision making", "Distributed consensus", "Peer-to-peer"],
        session_count: 3,
        complexity: "high"
      },
      {
        name: "Hierarchical",
        description: "Multi-level structure: Leader → Managers → Workers",
        use_cases: ["Organizational structures", "Command chains", "Delegated authority"],
        session_count: 4, // Additional level for hierarchy
        complexity: "high"
      }
    ];
  }

  // Agent role management
  async getAgentRoles(): Promise<AgentRole[]> {
    return [
      {
        name: "ACTIVE",
        permissions: ["SEND", "RECEIVE", "BROADCAST", "OBSERVE"],
        description: "Full participation in network communication",
        communication_level: "full"
      },
      {
        name: "OBSERVER", 
        permissions: ["RECEIVE", "OBSERVE"],
        description: "Can observe all communications, limited responses",
        communication_level: "read-only"
      },
      {
        name: "ASSISTANT",
        permissions: ["SEND", "RECEIVE", "OBSERVE"],
        description: "Can help specific agents on specific topics",
        communication_level: "selective"
      },
      {
        name: "SILENT",
        permissions: ["OBSERVE"],
        description: "Can observe all communications, cannot send",
        communication_level: "monitor-only"
      },
      {
        name: "SUPPORT",
        permissions: ["SEND", "RECEIVE", "OBSERVE"],
        description: "Context-aware support, provides help when requested",
        communication_level: "on-demand"
      }
    ];
  }

  // System management utilities
  async estimateSessionCount(agentCount: number, topology: string): Promise<{
    total_sessions: number;
    per_agent_sessions: number;
    shared_sessions: number;
    calculation: string;
  }> {
    const perAgentSessions = 3; // inbox, outbox, signals
    const sharedSessions = 1; // common_inbox
    const totalSessions = (agentCount * perAgentSessions) + sharedSessions;
    
    let calculation = `${agentCount} agents × ${perAgentSessions} sessions + ${sharedSessions} shared = ${totalSessions}`;
    
    if (topology === "hierarchical") {
      calculation += " + hierarchy overhead";
    }
    
    return {
      total_sessions: totalSessions,
      per_agent_sessions: perAgentSessions,
      shared_sessions: sharedSessions,
      calculation
    };
  }

  async generateWorkflowExample(
    agentCount: number,
    topology: string,
    useCase: string
  ): Promise<{
    workflow_code: string;
    setup_steps: string[];
    execution_flow: string[];
    cleanup_steps: string[];
  }> {
    const setupSteps = [
      "from multi_agent_screen_network import *",
      "network = MultiAgentNetworkManager()",
      "user = network.add_user()"
    ];
    
    for (let i = 1; i <= agentCount; i++) {
      setupSteps.push(`agent${i} = network.add_agent("agent${i}")`);
    }
    
    setupSteps.push("network.start_network()");
    
    let executionFlow: string[] = [];
    let workflowCode = "";
    
    switch (topology) {
      case "linear":
        executionFlow = [
          "User initiates workflow",
          "Agent1 processes and passes to Agent2",
          "Agent2 processes and passes to Agent3",
          "Final result returned to user"
        ];
        workflowCode = `# Linear chain workflow
agent1.send_message("agent2", "Process: ${useCase}")
agent2.send_message("agent3", "Processed step 1")
agent3.send_message("user", "Final result: ${useCase} complete")`;
        break;
        
      case "star":
        executionFlow = [
          "Central agent receives task from user",
          "Central agent broadcasts subtasks",
          "Worker agents process in parallel",
          "Results collected by central agent"
        ];
        workflowCode = `# Star topology workflow
user.send_message("agent1", "Coordinate: ${useCase}")
agent1.broadcast_message("Subtask assignment")
# Workers process in parallel
agent1.send_message("user", "All subtasks complete")`;
        break;
        
      case "mesh":
        executionFlow = [
          "All agents participate in discussion",
          "Consensus building through mesh communication",
          "Decision reached collaboratively",
          "Result implemented by all agents"
        ];
        workflowCode = `# Mesh topology workflow
CommunicationPatterns.mesh_discussion(network, "Topic: ${useCase}")
# All agents contribute to solution
user.broadcast_message("Implement agreed solution")`;
        break;
        
      default:
        executionFlow = ["Custom workflow execution"];
        workflowCode = `# Custom ${topology} workflow for ${useCase}`;
    }
    
    const cleanupSteps = [
      "network.stop_network()",
      "ScreenAgentManager.cleanup_all_sessions()"
    ];
    
    return {
      workflow_code: workflowCode,
      setup_steps: setupSteps,
      execution_flow: executionFlow,
      cleanup_steps: cleanupSteps
    };
  }
}