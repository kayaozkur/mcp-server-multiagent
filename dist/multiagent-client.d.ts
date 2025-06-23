/**
 * Enhanced Multi-Agent Communication Client
 * Comprehensive multi-agent system management with 99+ functionalities from 19 Python files
 */
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
export declare class MultiAgentClient {
    private functionalityDatabase;
    private categoryIndex;
    private typeIndex;
    private lastUpdate;
    private multiAgentPath;
    constructor();
    private initializeFunctionalityDatabase;
    private startPeriodicRefresh;
    private checkForUpdates;
    private regenerateFunctionalityDatabase;
    getFunctionalityInfo(name: string, includeExamples?: boolean): Promise<MultiAgentFunctionality | null>;
    searchFunctionalities(query: string, category?: string, maxResults?: number): Promise<MultiAgentFunctionality[]>;
    getFunctionalitiesByCategory(category: string): Promise<MultiAgentFunctionality[]>;
    getFunctionalitiesByType(type: string): Promise<MultiAgentFunctionality[]>;
    getFunctionalitiesByComplexity(complexity: string): Promise<MultiAgentFunctionality[]>;
    getFunctionalitiesByFile(filename: string): Promise<MultiAgentFunctionality[]>;
    getStats(): {
        totalFunctionalities: number;
        categories: string[];
        types: string[];
        complexityLevels: Record<string, number>;
        safetyLevels: Record<string, number>;
        fileCount: number;
        lastUpdate: Date;
    };
    getNetworkTopologies(): Promise<NetworkTopology[]>;
    getAgentRoles(): Promise<AgentRole[]>;
    estimateSessionCount(agentCount: number, topology: string): Promise<{
        total_sessions: number;
        per_agent_sessions: number;
        shared_sessions: number;
        calculation: string;
    }>;
    generateWorkflowExample(agentCount: number, topology: string, useCase: string): Promise<{
        workflow_code: string;
        setup_steps: string[];
        execution_flow: string[];
        cleanup_steps: string[];
    }>;
}
//# sourceMappingURL=multiagent-client.d.ts.map