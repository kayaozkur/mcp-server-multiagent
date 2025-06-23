#!/usr/bin/env node

/**
 * Comprehensive parser for ALL 21 multi-agent communication Python files
 * Generates complete multi-agent functionality database
 */

const fs = require('fs');
const path = require('path');

const multiAgentPath = '/Users/kayaozkur/Desktop/lepion/multi_agent_communication';

// Read all Python files in the multi-agent directory
function getAllPythonFiles() {
    const files = fs.readdirSync(multiAgentPath);
    return files.filter(file => file.endsWith('.py')).map(file => {
        const content = fs.readFileSync(path.join(multiAgentPath, file), 'utf8');
        return { filename: file, content };
    });
}

// Parse Python file to extract classes, functions, and key concepts
function parsePythonFile(filename, content) {
    const functionalities = [];
    const lines = content.split('\n');
    let currentClass = null;
    let currentFunction = null;
    let inDocstring = false;
    let docstringBuffer = [];
    
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        const trimmedLine = line.trim();
        
        // Handle docstrings
        if (trimmedLine.includes('"""') || trimmedLine.includes("'''")) {
            if (inDocstring) {
                inDocstring = false;
                const docstring = docstringBuffer.join(' ').trim();
                if (currentFunction && docstring) {
                    currentFunction.description = docstring;
                }
                docstringBuffer = [];
            } else {
                inDocstring = true;
                docstringBuffer = [];
            }
            continue;
        }
        
        if (inDocstring) {
            docstringBuffer.push(trimmedLine);
            continue;
        }
        
        // Parse class definitions
        const classMatch = trimmedLine.match(/^class\s+(\w+)(?:\([^)]*\))?:/);
        if (classMatch) {
            currentClass = {
                name: classMatch[1],
                filename: filename,
                type: 'class',
                methods: [],
                description: '',
                category: determineCategory(filename, classMatch[1])
            };
            functionalities.push(currentClass);
            continue;
        }
        
        // Parse function/method definitions
        const funcMatch = trimmedLine.match(/^def\s+(\w+)\s*\([^)]*\):/);
        if (funcMatch) {
            currentFunction = {
                name: funcMatch[1],
                filename: filename,
                type: currentClass ? 'method' : 'function',
                class: currentClass ? currentClass.name : null,
                description: '',
                category: determineCategory(filename, funcMatch[1]),
                usage_pattern: generateUsagePattern(funcMatch[1], filename),
                safety_level: determineSafetyLevel(funcMatch[1], filename)
            };
            
            if (currentClass) {
                currentClass.methods.push(currentFunction);
            } else {
                functionalities.push(currentFunction);
            }
            continue;
        }
        
        // Parse global variables and constants
        const varMatch = trimmedLine.match(/^([A-Z_][A-Z0-9_]*)\s*=\s*(.+)/);
        if (varMatch && !trimmedLine.startsWith('#')) {
            functionalities.push({
                name: varMatch[1],
                filename: filename,
                type: 'constant',
                value: varMatch[2],
                description: `Configuration constant: ${varMatch[1]}`,
                category: 'configuration'
            });
        }
    }
    
    return functionalities;
}

function determineCategory(filename, name) {
    const categoryMap = {
        'multi_agent_screen_network.py': 'core',
        'screen_agent_manager.py': 'management',
        'communication_patterns.py': 'patterns',
        'communication_flow_explained.py': 'flow',
        'broadcast_polling_system.py': 'polling',
        'broadcast_trigger_demo.py': 'triggers',
        'common_inbox_system.py': 'inbox',
        'configuration_variables.py': 'configuration',
        'dependency_matrices.py': 'dependencies',
        'dependency_matrix_system.py': 'dependencies',
        'global_message_bus_system.py': 'messaging',
        'hierarchical_broadcast_concept.py': 'hierarchy',
        'hierarchical_broadcast_system.py': 'hierarchy',
        'hybrid_topology_system.py': 'topology',
        'loop_prevention_system.py': 'reliability',
        'observer_assistant_system.py': 'roles',
        'omniscient_agent_system.py': 'monitoring',
        'prolog_rule_system.py': 'rules',
        'rule_based_agent_config.py': 'rules'
    };
    
    const baseCategory = categoryMap[filename] || 'utilities';
    
    // Refine category based on function/class name
    if (name.toLowerCase().includes('broadcast')) return 'broadcasting';
    if (name.toLowerCase().includes('message')) return 'messaging';
    if (name.toLowerCase().includes('screen')) return 'screen';
    if (name.toLowerCase().includes('agent')) return 'agents';
    if (name.toLowerCase().includes('network')) return 'network';
    if (name.toLowerCase().includes('communication')) return 'communication';
    if (name.toLowerCase().includes('topology')) return 'topology';
    if (name.toLowerCase().includes('hierarchy')) return 'hierarchy';
    if (name.toLowerCase().includes('permission')) return 'permissions';
    if (name.toLowerCase().includes('observer')) return 'monitoring';
    
    return baseCategory;
}

function generateUsagePattern(name, filename) {
    const patterns = {
        // Core system patterns
        'MultiAgentNetworkManager': 'network = MultiAgentNetworkManager()',
        'AgentCommunicationNode': 'agent = network.add_agent("agent_id")',
        'send_message': 'agent.send_message("recipient", "message")',
        'broadcast_message': 'agent.broadcast_message("message")',
        'start_network': 'network.start_network()',
        'stop_network': 'network.stop_network()',
        
        // Communication patterns
        'ring_topology': 'CommunicationPatterns.ring_topology(network, "message")',
        'star_topology': 'CommunicationPatterns.star_topology_broadcast(network, "central_agent", "message")',
        'mesh_topology': 'CommunicationPatterns.mesh_discussion(network, "topic")',
        'hierarchical': 'CommunicationPatterns.hierarchical_communication(network)',
        
        // Management functions
        'create_session': 'ScreenAgentManager.create_session("session_name")',
        'cleanup_sessions': 'ScreenAgentManager.cleanup_all_sessions()',
        'capture_screen': 'ScreenAgentManager.capture_screen_content("session_name")',
        
        // Configuration
        'setup_permissions': 'setup_permissions(agent_id, permissions_dict)',
        'configure_topology': 'configure_topology(network, topology_type)',
        
        // Monitoring
        'monitor_network': 'OmniscientAgent.monitor_all_communications()',
        'get_network_stats': 'network.get_communication_statistics()',
        
        // Broadcast systems
        'start_polling': 'BroadcastPollingSystem.start_adaptive_polling()',
        'trigger_urgent': 'BroadcastTriggerDemo.signal_urgent_broadcast()',
        
        // Rule systems
        'apply_rules': 'RuleBasedSystem.apply_communication_rules(message)',
        'check_permissions': 'PermissionMatrix.check_agent_permissions(agent_id, action)'
    };
    
    return patterns[name] || `${name}() # Usage pattern for ${name}`;
}

function determineSafetyLevel(name, filename) {
    // System management functions are typically more dangerous
    const dangerous = ['cleanup', 'terminate', 'kill', 'delete', 'remove', 'destroy'];
    const moderate = ['create', 'start', 'stop', 'modify', 'update', 'configure', 'setup'];
    
    const nameLower = name.toLowerCase();
    
    if (dangerous.some(word => nameLower.includes(word))) {
        return 'dangerous';
    }
    if (moderate.some(word => nameLower.includes(word)) || filename.includes('system')) {
        return 'moderate';
    }
    return 'safe';
}

function generateMultiAgentInfo(functionality) {
    const examples = generateExamples(functionality);
    const alternatives = generateAlternatives(functionality);
    const requirements = generateRequirements(functionality);
    const dependencies = generateDependencies(functionality);
    
    return {
        name: functionality.name,
        description: functionality.description || `${functionality.type}: ${functionality.name}`,
        type: functionality.type,
        category: functionality.category,
        filename: functionality.filename,
        class: functionality.class || null,
        usage_pattern: functionality.usage_pattern,
        examples: examples,
        alternatives: alternatives,
        requirements: requirements,
        dependencies: dependencies,
        safety_level: functionality.safety_level || 'safe',
        complexity: determineComplexity(functionality),
        methods: functionality.methods || []
    };
}

function generateExamples(functionality) {
    const exampleMap = {
        // Core system examples
        'MultiAgentNetworkManager': [
            'network = MultiAgentNetworkManager()',
            'user = network.add_user()',
            'agent1 = network.add_agent("agent1")',
            'network.start_network()'
        ],
        'AgentCommunicationNode': [
            'agent = AgentCommunicationNode("agent1", network)',
            'agent.send_message("agent2", "Hello!")',
            'agent.broadcast_message("Hello everyone!")'
        ],
        'send_message': [
            'agent.send_message("agent2", "Direct message")',
            'agent.send_message("user", "Report complete")',
            'agent.send_message("assistant", "Need help with task")'
        ],
        
        // Communication patterns
        'ring_topology': [
            'CommunicationPatterns.ring_topology(network, "Pass the token")',
            '# Messages flow: A1 → A2 → A3 → A4 → A1'
        ],
        'star_topology_broadcast': [
            'CommunicationPatterns.star_topology_broadcast(network, "leader", "New directive")',
            '# Central agent broadcasts to all others'
        ],
        'mesh_discussion': [
            'CommunicationPatterns.mesh_discussion(network, "Topic: Project planning")',
            '# All agents participate in open discussion'
        ],
        
        // Management examples
        'create_session': [
            'ScreenAgentManager.create_session("agent1_inbox")',
            'ScreenAgentManager.create_session("common_inbox")'
        ],
        'cleanup_sessions': [
            'ScreenAgentManager.cleanup_all_sessions()',
            'ScreenAgentManager.cleanup_agent_sessions("agent1")'
        ]
    };
    
    return exampleMap[functionality.name] || [
        `${functionality.name}() # Basic usage`,
        `# ${functionality.description || 'Multi-agent system functionality'}`
    ];
}

function generateAlternatives(functionality) {
    const alternativeMap = {
        'MultiAgentNetworkManager': ['DistributedSystem', 'ClusterManager'],
        'AgentCommunicationNode': ['AgentProcess', 'CommunicationInterface'],
        'send_message': ['publish_message', 'emit_event', 'broadcast'],
        'ring_topology': ['chain_topology', 'circular_broadcast'],
        'star_topology': ['hub_and_spoke', 'centralized_broadcast'],
        'mesh_topology': ['full_connectivity', 'peer_to_peer'],
        'create_session': ['spawn_process', 'create_thread'],
        'cleanup_sessions': ['terminate_processes', 'shutdown_network']
    };
    
    return alternativeMap[functionality.name] || [];
}

function generateRequirements(functionality) {
    const requirements = ['Python 3.7+', 'GNU Screen'];
    
    if (functionality.filename.includes('prolog')) {
        requirements.push('SWI-Prolog (optional)');
    }
    
    if (functionality.category === 'monitoring') {
        requirements.push('System monitoring permissions');
    }
    
    if (functionality.safety_level === 'dangerous') {
        requirements.push('Administrative privileges');
    }
    
    return requirements;
}

function generateDependencies(functionality) {
    const baseDependencies = ['subprocess', 'threading', 'json', 'time'];
    
    const dependencyMap = {
        'screen': ['screen command-line tool'],
        'messaging': ['uuid', 'datetime'],
        'monitoring': ['psutil (optional)'],
        'rules': ['typing', 'dataclasses'],
        'configuration': ['os', 'pathlib']
    };
    
    const categoryDeps = dependencyMap[functionality.category] || [];
    return [...baseDependencies, ...categoryDeps];
}

function determineComplexity(functionality) {
    if (functionality.type === 'class' && functionality.methods && functionality.methods.length > 10) {
        return 'high';
    }
    if (functionality.category === 'core' || functionality.category === 'management') {
        return 'high';
    }
    if (functionality.safety_level === 'dangerous') {
        return 'moderate';
    }
    return 'low';
}

// Parse all files
console.log('Parsing all 21 multi-agent communication Python files...');
const pythonFiles = getAllPythonFiles();
const allFunctionalities = [];

for (const file of pythonFiles) {
    console.log(`Parsing ${file.filename}...`);
    const functionalities = parsePythonFile(file.filename, file.content);
    allFunctionalities.push(...functionalities);
}

// Generate complete multi-agent info for each functionality
const completeMultiAgentSystem = allFunctionalities.map(generateMultiAgentInfo);

// Sort by category and name for better organization
completeMultiAgentSystem.sort((a, b) => {
    if (a.category !== b.category) {
        return a.category.localeCompare(b.category);
    }
    return a.name.localeCompare(b.name);
});

// Output statistics
console.log(`\\nParsed ${pythonFiles.length} Python files`);
console.log(`Total functionalities: ${allFunctionalities.length}`);
console.log('Categories:', [...new Set(completeMultiAgentSystem.map(f => f.category))]);
console.log('Types:', [...new Set(completeMultiAgentSystem.map(f => f.type))]);

// Count by type
const typeCount = completeMultiAgentSystem.reduce((acc, f) => {
    acc[f.type] = (acc[f.type] || 0) + 1;
    return acc;
}, {});
console.log('\\nBreakdown by type:', typeCount);

// Count by category
const categoryCount = completeMultiAgentSystem.reduce((acc, f) => {
    acc[f.category] = (acc[f.category] || 0) + 1;
    return acc;
}, {});
console.log('Breakdown by category:', categoryCount);

// Write to TypeScript file
const output = `// Auto-generated multi-agent communication system database from all 21 Python files
export const MULTIAGENT_FUNCTIONALITIES = ${JSON.stringify(completeMultiAgentSystem, null, 2)};

export const TOTAL_FUNCTIONALITIES = ${completeMultiAgentSystem.length};
export const PYTHON_FILES_COUNT = ${pythonFiles.length};
export const CATEGORIES = ${JSON.stringify([...new Set(completeMultiAgentSystem.map(f => f.category))])};
export const TYPES = ${JSON.stringify([...new Set(completeMultiAgentSystem.map(f => f.type))])};
`;

fs.writeFileSync('/Users/kayaozkur/Desktop/lepion/mcp-multiagent-server/src/generated-multiagent.ts', output);

console.log(`\\n✅ Generated ${completeMultiAgentSystem.length} multi-agent functionalities from ${pythonFiles.length} Python files`);
console.log('✅ Written to: src/generated-multiagent.ts');
console.log('✅ Ready for multi-agent communication intelligence!');