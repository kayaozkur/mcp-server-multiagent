/**
 * Tool handlers for Multi-Agent MCP Server
 */
import { MultiAgentClient } from "./multiagent-client.js";
interface ValidationError {
    field: string;
    message: string;
}
export declare const toolHandlers: {
    getFunctionalityInfo(client: MultiAgentClient, args: any): Promise<{
        error: string;
        errors: ValidationError[];
        suggestions?: undefined;
        success?: undefined;
        functionality_info?: undefined;
        database_size?: undefined;
        source?: undefined;
    } | {
        error: string;
        suggestions: string[];
        errors?: undefined;
        success?: undefined;
        functionality_info?: undefined;
        database_size?: undefined;
        source?: undefined;
    } | {
        success: boolean;
        functionality_info: import("./multiagent-client.js").MultiAgentFunctionality;
        database_size: string;
        source: string;
        error?: undefined;
        errors?: undefined;
        suggestions?: undefined;
    } | {
        error: string;
        errors?: undefined;
        suggestions?: undefined;
        success?: undefined;
        functionality_info?: undefined;
        database_size?: undefined;
        source?: undefined;
    }>;
    searchFunctionalities(client: MultiAgentClient, args: any): Promise<{
        error: string;
        errors: ValidationError[];
        success?: undefined;
        query?: undefined;
        category?: undefined;
        results_count?: undefined;
        functionalities?: undefined;
        search_tips?: undefined;
    } | {
        success: boolean;
        query: any;
        category: any;
        results_count: number;
        functionalities: import("./multiagent-client.js").MultiAgentFunctionality[];
        search_tips: string[];
        error?: undefined;
        errors?: undefined;
    } | {
        error: string;
        errors?: undefined;
        success?: undefined;
        query?: undefined;
        category?: undefined;
        results_count?: undefined;
        functionalities?: undefined;
        search_tips?: undefined;
    }>;
    getFunctionalitiesByCategory(client: MultiAgentClient, args: any): Promise<{
        error: string;
        errors: ValidationError[];
        success?: undefined;
        category?: undefined;
        functionalities?: undefined;
        count?: undefined;
        source?: undefined;
    } | {
        success: boolean;
        category: any;
        functionalities: import("./multiagent-client.js").MultiAgentFunctionality[];
        count: number;
        source: string;
        error?: undefined;
        errors?: undefined;
    } | {
        error: string;
        errors?: undefined;
        success?: undefined;
        category?: undefined;
        functionalities?: undefined;
        count?: undefined;
        source?: undefined;
    }>;
    getFunctionalitiesByType(client: MultiAgentClient, args: any): Promise<{
        error: string;
        errors: ValidationError[];
        success?: undefined;
        type?: undefined;
        functionalities?: undefined;
        count?: undefined;
        source?: undefined;
    } | {
        success: boolean;
        type: any;
        functionalities: import("./multiagent-client.js").MultiAgentFunctionality[];
        count: number;
        source: string;
        error?: undefined;
        errors?: undefined;
    } | {
        error: string;
        errors?: undefined;
        success?: undefined;
        type?: undefined;
        functionalities?: undefined;
        count?: undefined;
        source?: undefined;
    }>;
    getFunctionalitiesByComplexity(client: MultiAgentClient, args: any): Promise<{
        error: string;
        errors: ValidationError[];
        success?: undefined;
        complexity?: undefined;
        functionalities?: undefined;
        count?: undefined;
        source?: undefined;
    } | {
        success: boolean;
        complexity: any;
        functionalities: import("./multiagent-client.js").MultiAgentFunctionality[];
        count: number;
        source: string;
        error?: undefined;
        errors?: undefined;
    } | {
        error: string;
        errors?: undefined;
        success?: undefined;
        complexity?: undefined;
        functionalities?: undefined;
        count?: undefined;
        source?: undefined;
    }>;
    getFunctionalitiesByFile(client: MultiAgentClient, args: any): Promise<{
        error: string;
        errors: ValidationError[];
        success?: undefined;
        filename?: undefined;
        functionalities?: undefined;
        count?: undefined;
        source?: undefined;
    } | {
        success: boolean;
        filename: any;
        functionalities: import("./multiagent-client.js").MultiAgentFunctionality[];
        count: number;
        source: string;
        error?: undefined;
        errors?: undefined;
    } | {
        error: string;
        errors?: undefined;
        success?: undefined;
        filename?: undefined;
        functionalities?: undefined;
        count?: undefined;
        source?: undefined;
    }>;
    getNetworkTopologies(client: MultiAgentClient, args: any): Promise<{
        success: boolean;
        topologies: import("./multiagent-client.js").NetworkTopology[];
        count: number;
        usage_info: string;
        source: string;
        error?: undefined;
    } | {
        error: string;
        success?: undefined;
        topologies?: undefined;
        count?: undefined;
        usage_info?: undefined;
        source?: undefined;
    }>;
    getAgentRoles(client: MultiAgentClient, args: any): Promise<{
        success: boolean;
        roles: import("./multiagent-client.js").AgentRole[];
        count: number;
        permission_info: string;
        source: string;
        error?: undefined;
    } | {
        error: string;
        success?: undefined;
        roles?: undefined;
        count?: undefined;
        permission_info?: undefined;
        source?: undefined;
    }>;
    estimateSessionCount(client: MultiAgentClient, args: any): Promise<{
        error: string;
        errors: ValidationError[];
        success?: undefined;
        agent_count?: undefined;
        topology?: undefined;
        session_estimate?: undefined;
        planning_info?: undefined;
        source?: undefined;
    } | {
        success: boolean;
        agent_count: any;
        topology: any;
        session_estimate: {
            total_sessions: number;
            per_agent_sessions: number;
            shared_sessions: number;
            calculation: string;
        };
        planning_info: string;
        source: string;
        error?: undefined;
        errors?: undefined;
    } | {
        error: string;
        errors?: undefined;
        success?: undefined;
        agent_count?: undefined;
        topology?: undefined;
        session_estimate?: undefined;
        planning_info?: undefined;
        source?: undefined;
    }>;
    generateWorkflowExample(client: MultiAgentClient, args: any): Promise<{
        error: string;
        errors: ValidationError[];
        success?: undefined;
        parameters?: undefined;
        workflow_example?: undefined;
        implementation_tips?: undefined;
        source?: undefined;
    } | {
        success: boolean;
        parameters: {
            agent_count: any;
            topology: any;
            use_case: any;
        };
        workflow_example: {
            workflow_code: string;
            setup_steps: string[];
            execution_flow: string[];
            cleanup_steps: string[];
        };
        implementation_tips: string[];
        source: string;
        error?: undefined;
        errors?: undefined;
    } | {
        error: string;
        errors?: undefined;
        success?: undefined;
        parameters?: undefined;
        workflow_example?: undefined;
        implementation_tips?: undefined;
        source?: undefined;
    }>;
    getDatabaseStats(client: MultiAgentClient, args: any): Promise<{
        success: boolean;
        stats: {
            totalFunctionalities: number;
            categories: string[];
            types: string[];
            complexityLevels: Record<string, number>;
            safetyLevels: Record<string, number>;
            fileCount: number;
            lastUpdate: Date;
        };
        message: string;
        breakdown: {
            total_functionalities: number;
            categories: number;
            python_files: number;
            types: string[];
            complexity_distribution: Record<string, number>;
            safety_distribution: Record<string, number>;
        };
        source: string;
        error?: undefined;
    } | {
        error: string;
        success?: undefined;
        stats?: undefined;
        message?: undefined;
        breakdown?: undefined;
        source?: undefined;
    }>;
};
export {};
//# sourceMappingURL=tools.d.ts.map