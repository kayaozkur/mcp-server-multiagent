/**
 * Tool handlers for Multi-Agent MCP Server
 */
import { logger } from "./logger.js";
export const toolHandlers = {
    async getFunctionalityInfo(client, args) {
        let errors = [];
        if (!args.functionality || typeof args.functionality !== 'string') {
            errors.push({ field: 'functionality', message: 'Functionality name is required and must be a string' });
        }
        if (errors.length > 0) {
            return { error: 'Validation failed', errors };
        }
        try {
            const result = await client.getFunctionalityInfo(args.functionality, args.include_examples ?? true);
            if (!result) {
                return {
                    error: `Multi-agent functionality '${args.functionality}' not found`,
                    suggestions: [
                        "Check functionality name spelling",
                        "Use multiagent_search_functionalities to find similar ones",
                        "Browse by category using multiagent_get_functionalities_by_category"
                    ]
                };
            }
            return {
                success: true,
                functionality_info: result,
                database_size: "99+ functionalities from 19 Python files",
                source: "comprehensive_multiagent_database"
            };
        }
        catch (error) {
            logger.error('Error getting functionality info:', error);
            return { error: `Failed to get functionality info: ${error instanceof Error ? error.message : String(error)}` };
        }
    },
    async searchFunctionalities(client, args) {
        let errors = [];
        if (!args.query || typeof args.query !== 'string') {
            errors.push({ field: 'query', message: 'Query is required and must be a string' });
        }
        const validCategories = [
            'agents', 'broadcasting', 'communication', 'configuration', 'dependencies',
            'hierarchy', 'inbox', 'messaging', 'monitoring', 'permissions', 'roles',
            'rules', 'screen', 'topology', 'triggers', 'all'
        ];
        if (args.category && !validCategories.includes(args.category)) {
            errors.push({
                field: 'category',
                message: `Category must be one of: ${validCategories.join(', ')}`
            });
        }
        if (errors.length > 0) {
            return { error: 'Validation failed', errors };
        }
        try {
            const results = await client.searchFunctionalities(args.query, args.category || 'all', args.max_results || 10);
            return {
                success: true,
                query: args.query,
                category: args.category || 'all',
                results_count: results.length,
                functionalities: results,
                search_tips: [
                    "Use specific terms like 'broadcast', 'topology', 'screen'",
                    "Try category filtering to narrow results",
                    "Search by filename like 'communication_patterns.py'"
                ]
            };
        }
        catch (error) {
            logger.error('Error searching functionalities:', error);
            return { error: `Failed to search functionalities: ${error instanceof Error ? error.message : String(error)}` };
        }
    },
    async getFunctionalitiesByCategory(client, args) {
        let errors = [];
        if (!args.category || typeof args.category !== 'string') {
            errors.push({ field: 'category', message: 'Category is required and must be a string' });
        }
        if (errors.length > 0) {
            return { error: 'Validation failed', errors };
        }
        try {
            const result = await client.getFunctionalitiesByCategory(args.category);
            return {
                success: true,
                category: args.category,
                functionalities: result,
                count: result.length,
                source: "comprehensive_multiagent_database"
            };
        }
        catch (error) {
            logger.error('Error getting functionalities by category:', error);
            return { error: `Failed to get functionalities by category: ${error instanceof Error ? error.message : String(error)}` };
        }
    },
    async getFunctionalitiesByType(client, args) {
        let errors = [];
        if (!args.type || typeof args.type !== 'string') {
            errors.push({ field: 'type', message: 'Type is required and must be a string' });
        }
        const validTypes = ['class', 'function', 'constant'];
        if (!validTypes.includes(args.type)) {
            errors.push({
                field: 'type',
                message: `Type must be one of: ${validTypes.join(', ')}`
            });
        }
        if (errors.length > 0) {
            return { error: 'Validation failed', errors };
        }
        try {
            const result = await client.getFunctionalitiesByType(args.type);
            return {
                success: true,
                type: args.type,
                functionalities: result,
                count: result.length,
                source: "comprehensive_multiagent_database"
            };
        }
        catch (error) {
            logger.error('Error getting functionalities by type:', error);
            return { error: `Failed to get functionalities by type: ${error instanceof Error ? error.message : String(error)}` };
        }
    },
    async getFunctionalitiesByComplexity(client, args) {
        let errors = [];
        if (!args.complexity || typeof args.complexity !== 'string') {
            errors.push({ field: 'complexity', message: 'Complexity level is required and must be a string' });
        }
        const validComplexity = ['low', 'moderate', 'high'];
        if (!validComplexity.includes(args.complexity)) {
            errors.push({
                field: 'complexity',
                message: `Complexity must be one of: ${validComplexity.join(', ')}`
            });
        }
        if (errors.length > 0) {
            return { error: 'Validation failed', errors };
        }
        try {
            const result = await client.getFunctionalitiesByComplexity(args.complexity);
            return {
                success: true,
                complexity: args.complexity,
                functionalities: result,
                count: result.length,
                source: "comprehensive_multiagent_database"
            };
        }
        catch (error) {
            logger.error('Error getting functionalities by complexity:', error);
            return { error: `Failed to get functionalities by complexity: ${error instanceof Error ? error.message : String(error)}` };
        }
    },
    async getFunctionalitiesByFile(client, args) {
        let errors = [];
        if (!args.filename || typeof args.filename !== 'string') {
            errors.push({ field: 'filename', message: 'Filename is required and must be a string' });
        }
        if (errors.length > 0) {
            return { error: 'Validation failed', errors };
        }
        try {
            const result = await client.getFunctionalitiesByFile(args.filename);
            return {
                success: true,
                filename: args.filename,
                functionalities: result,
                count: result.length,
                source: "comprehensive_multiagent_database"
            };
        }
        catch (error) {
            logger.error('Error getting functionalities by file:', error);
            return { error: `Failed to get functionalities by file: ${error instanceof Error ? error.message : String(error)}` };
        }
    },
    async getNetworkTopologies(client, args) {
        try {
            const topologies = await client.getNetworkTopologies();
            return {
                success: true,
                topologies: topologies,
                count: topologies.length,
                usage_info: "Each topology has different use cases and complexity levels",
                source: "multiagent_topology_database"
            };
        }
        catch (error) {
            logger.error('Error getting network topologies:', error);
            return { error: `Failed to get network topologies: ${error instanceof Error ? error.message : String(error)}` };
        }
    },
    async getAgentRoles(client, args) {
        try {
            const roles = await client.getAgentRoles();
            return {
                success: true,
                roles: roles,
                count: roles.length,
                permission_info: "Each role has different communication permissions and capabilities",
                source: "multiagent_role_database"
            };
        }
        catch (error) {
            logger.error('Error getting agent roles:', error);
            return { error: `Failed to get agent roles: ${error instanceof Error ? error.message : String(error)}` };
        }
    },
    async estimateSessionCount(client, args) {
        let errors = [];
        if (!args.agent_count || typeof args.agent_count !== 'number' || args.agent_count < 1) {
            errors.push({ field: 'agent_count', message: 'Agent count is required and must be a positive number' });
        }
        if (!args.topology || typeof args.topology !== 'string') {
            errors.push({ field: 'topology', message: 'Topology is required and must be a string' });
        }
        if (errors.length > 0) {
            return { error: 'Validation failed', errors };
        }
        try {
            const result = await client.estimateSessionCount(args.agent_count, args.topology);
            return {
                success: true,
                agent_count: args.agent_count,
                topology: args.topology,
                session_estimate: result,
                planning_info: "Use this for resource planning and session management",
                source: "multiagent_session_calculator"
            };
        }
        catch (error) {
            logger.error('Error estimating session count:', error);
            return { error: `Failed to estimate session count: ${error instanceof Error ? error.message : String(error)}` };
        }
    },
    async generateWorkflowExample(client, args) {
        let errors = [];
        if (!args.agent_count || typeof args.agent_count !== 'number' || args.agent_count < 2) {
            errors.push({ field: 'agent_count', message: 'Agent count is required and must be at least 2' });
        }
        if (!args.topology || typeof args.topology !== 'string') {
            errors.push({ field: 'topology', message: 'Topology is required and must be a string' });
        }
        if (!args.use_case || typeof args.use_case !== 'string') {
            errors.push({ field: 'use_case', message: 'Use case is required and must be a string' });
        }
        if (errors.length > 0) {
            return { error: 'Validation failed', errors };
        }
        try {
            const result = await client.generateWorkflowExample(args.agent_count, args.topology, args.use_case);
            return {
                success: true,
                parameters: {
                    agent_count: args.agent_count,
                    topology: args.topology,
                    use_case: args.use_case
                },
                workflow_example: result,
                implementation_tips: [
                    "Customize agent IDs and messages for your specific use case",
                    "Add error handling and logging as needed",
                    "Test with small agent counts first",
                    "Monitor screen sessions during execution"
                ],
                source: "multiagent_workflow_generator"
            };
        }
        catch (error) {
            logger.error('Error generating workflow example:', error);
            return { error: `Failed to generate workflow example: ${error instanceof Error ? error.message : String(error)}` };
        }
    },
    async getDatabaseStats(client, args) {
        try {
            const stats = client.getStats();
            return {
                success: true,
                stats: stats,
                message: `Database contains ${stats.totalFunctionalities} functionalities across ${stats.categories.length} categories from ${stats.fileCount} Python files`,
                breakdown: {
                    total_functionalities: stats.totalFunctionalities,
                    categories: stats.categories.length,
                    python_files: stats.fileCount,
                    types: stats.types,
                    complexity_distribution: stats.complexityLevels,
                    safety_distribution: stats.safetyLevels
                },
                source: "comprehensive_multiagent_database"
            };
        }
        catch (error) {
            logger.error('Error getting database stats:', error);
            return { error: `Failed to get database stats: ${error instanceof Error ? error.message : String(error)}` };
        }
    }
};
//# sourceMappingURL=tools.js.map