// Auto-generated multi-agent communication system database from all 21 Python files
export const MULTIAGENT_FUNCTIONALITIES = [
  {
    "name": "AdvancedAgentBehaviors",
    "description": "class: AdvancedAgentBehaviors",
    "type": "class",
    "category": "agents",
    "filename": "communication_patterns.py",
    "class": null,
    "examples": [
      "AdvancedAgentBehaviors() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "negotiator_handler",
        "filename": "communication_patterns.py",
        "type": "method",
        "class": "AdvancedAgentBehaviors",
        "description": "",
        "category": "patterns",
        "usage_pattern": "negotiator_handler() # Usage pattern for negotiator_handler",
        "safety_level": "safe"
      },
      {
        "name": "handler",
        "filename": "communication_patterns.py",
        "type": "method",
        "class": "AdvancedAgentBehaviors",
        "description": "",
        "category": "patterns",
        "usage_pattern": "handler() # Usage pattern for handler",
        "safety_level": "safe"
      },
      {
        "name": "create_collaborative_agents",
        "filename": "communication_patterns.py",
        "type": "method",
        "class": "AdvancedAgentBehaviors",
        "description": "task_assignments = {}  def collaborator_handler(agent_id: str): def handler(message: Message): if \"TASK_REQUEST:\" in message.content: task = message.content.split(\"TASK_REQUEST:\")[1] # Assign task part to this agent task_assignments[agent_id] = task network.agents[agent_id].send_message(message.sender, f\"TASK_ACCEPTED:{task}\") elif \"RESULT:\" in message.content: print(f\"[{agent_id}] Received result: {message.content}\") # Could aggregate results here return handler  for agent_id in network.agents: network.agents[agent_id].register_message_handler(\"text\", collaborator_handler(agent_id))  @staticmethod def create_competitive_agents(network: MultiAgentNetworkManager):",
        "category": "agents",
        "usage_pattern": "create_collaborative_agents() # Usage pattern for create_collaborative_agents",
        "safety_level": "moderate"
      },
      {
        "name": "competitor_handler",
        "filename": "communication_patterns.py",
        "type": "method",
        "class": "AdvancedAgentBehaviors",
        "description": "",
        "category": "patterns",
        "usage_pattern": "competitor_handler() # Usage pattern for competitor_handler",
        "safety_level": "safe"
      },
      {
        "name": "handler",
        "filename": "communication_patterns.py",
        "type": "method",
        "class": "AdvancedAgentBehaviors",
        "description": "",
        "category": "patterns",
        "usage_pattern": "handler() # Usage pattern for handler",
        "safety_level": "safe"
      },
      {
        "name": "demo_communication_patterns",
        "filename": "communication_patterns.py",
        "type": "method",
        "class": "AdvancedAgentBehaviors",
        "description": "",
        "category": "communication",
        "usage_pattern": "demo_communication_patterns() # Usage pattern for demo_communication_patterns",
        "safety_level": "safe"
      }
    ]
  },
  {
    "name": "Agent",
    "description": "class: Agent",
    "type": "class",
    "category": "agents",
    "filename": "hierarchical_broadcast_concept.py",
    "class": null,
    "examples": [
      "Agent() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "Agent",
    "description": "class: Agent",
    "type": "class",
    "category": "agents",
    "filename": "hierarchical_broadcast_system.py",
    "class": null,
    "examples": [
      "Agent() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "Agent",
    "description": "class: Agent",
    "type": "class",
    "category": "agents",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "Agent() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "AgentFact",
    "description": "class: AgentFact",
    "type": "class",
    "category": "agents",
    "filename": "rule_based_agent_config.py",
    "class": null,
    "examples": [
      "AgentFact() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "AgentRole",
    "description": "class: AgentRole",
    "type": "class",
    "category": "agents",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "AgentRole() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "demonstrate_3_agent_flow",
    "description": "print(\"3-AGENT COMMUNICATION EXAMPLE\") print(\"=\" * 35) print()  print(\"Scenario: Agent 1 broadcasts to Agent 2 and Agent 3\") print(\"-\" * 50) print()  print(\"Step 1 - Agent 1 sends broadcast:\") print(\"  screen -S agent2_inbox -X stuff 'BROADCAST: Meeting at 3pm'\") print(\"  screen -S agent3_inbox -X stuff 'BROADCAST: Meeting at 3pm'\") print(\"  screen -S agent1_outbox -X stuff 'BROADCAST SENT to agent2, agent3'\") print()  print(\"Step 2 - Agent 2 receives and responds:\") print(\"  screen -S agent2_inbox -X hardcopy /tmp/agent2_inbox\") print(\"  # Agent 2 reads: 'BROADCAST: Meeting at 3pm'\") print(\"  screen -S agent1_inbox -X stuff 'ACK: Agent 2 will attend'\") print(\"  screen -S agent2_outbox -X stuff 'SENT ACK to agent1'\") print()  print(\"Step 3 - Agent 3 receives and responds:\") print(\"  screen -S agent3_inbox -X hardcopy /tmp/agent3_inbox\") print(\"  # Agent 3 reads: 'BROADCAST: Meeting at 3pm'\") print(\"  screen -S agent1_inbox -X stuff 'ACK: Agent 3 will attend'\") print(\"  screen -S agent3_outbox -X stuff 'SENT ACK to agent1'\") print()  print(\"Step 4 - Agent 1 receives responses:\") print(\"  screen -S agent1_inbox -X hardcopy /tmp/agent1_inbox\") print(\"  # Agent 1 reads both ACK messages\") print()  def show_session_ownership():",
    "type": "function",
    "category": "agents",
    "filename": "communication_flow_explained.py",
    "class": null,
    "usage_pattern": "demonstrate_3_agent_flow() # Usage pattern for demonstrate_3_agent_flow",
    "examples": [
      "demonstrate_3_agent_flow() # Basic usage",
      "# print(\"3-AGENT COMMUNICATION EXAMPLE\") print(\"=\" * 35) print()  print(\"Scenario: Agent 1 broadcasts to Agent 2 and Agent 3\") print(\"-\" * 50) print()  print(\"Step 1 - Agent 1 sends broadcast:\") print(\"  screen -S agent2_inbox -X stuff 'BROADCAST: Meeting at 3pm'\") print(\"  screen -S agent3_inbox -X stuff 'BROADCAST: Meeting at 3pm'\") print(\"  screen -S agent1_outbox -X stuff 'BROADCAST SENT to agent2, agent3'\") print()  print(\"Step 2 - Agent 2 receives and responds:\") print(\"  screen -S agent2_inbox -X hardcopy /tmp/agent2_inbox\") print(\"  # Agent 2 reads: 'BROADCAST: Meeting at 3pm'\") print(\"  screen -S agent1_inbox -X stuff 'ACK: Agent 2 will attend'\") print(\"  screen -S agent2_outbox -X stuff 'SENT ACK to agent1'\") print()  print(\"Step 3 - Agent 3 receives and responds:\") print(\"  screen -S agent3_inbox -X hardcopy /tmp/agent3_inbox\") print(\"  # Agent 3 reads: 'BROADCAST: Meeting at 3pm'\") print(\"  screen -S agent1_inbox -X stuff 'ACK: Agent 3 will attend'\") print(\"  screen -S agent3_outbox -X stuff 'SENT ACK to agent1'\") print()  print(\"Step 4 - Agent 1 receives responses:\") print(\"  screen -S agent1_inbox -X hardcopy /tmp/agent1_inbox\") print(\"  # Agent 1 reads both ACK messages\") print()  def show_session_ownership():"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "TransparentAgent",
    "description": "class: TransparentAgent",
    "type": "class",
    "category": "agents",
    "filename": "common_inbox_system.py",
    "class": null,
    "examples": [
      "TransparentAgent() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "broadcast_message",
        "filename": "common_inbox_system.py",
        "type": "method",
        "class": "TransparentAgent",
        "description": "recipients = [agent for agent in self.all_agents if agent != self.agent_id]  # Send to all recipient inboxes for recipient in recipients: try: subprocess.run([ \"screen\", \"-S\", f\"{recipient}_inbox\", \"-X\", \"stuff\", f\"BROADCAST FROM {self.agent_id}: {content}\\n\" ], check=True)  # Trigger polling subprocess.run([ \"screen\", \"-S\", f\"{recipient}_signals\", \"-X\", \"stuff\", f\"POLL_TRIGGER:broadcast\\n\" ], check=True) except subprocess.CalledProcessError: pass  # Log to own outbox try: subprocess.run([ \"screen\", \"-S\", self.outbox_session, \"-X\", \"stuff\", f\"BROADCAST to {len(recipients)} agents: {content}\\n\" ], check=True) except subprocess.CalledProcessError: pass  # LOG TO COMMON INBOX (This is the key!) self.common_system.log_to_common_inbox( sender=self.agent_id, recipient=\"ALL\", content=content, msg_type=\"broadcast\" )  def start_monitoring(self):",
        "category": "broadcasting",
        "usage_pattern": "agent.broadcast_message(\"message\")",
        "safety_level": "moderate"
      },
      {
        "name": "stop_monitoring",
        "filename": "common_inbox_system.py",
        "type": "method",
        "class": "TransparentAgent",
        "description": "self.monitoring_active = False if self.monitor_thread: self.monitor_thread.join(timeout=2)  def _monitoring_loop(self):",
        "category": "inbox",
        "usage_pattern": "stop_monitoring() # Usage pattern for stop_monitoring",
        "safety_level": "moderate"
      },
      {
        "name": "_check_personal_inbox",
        "filename": "common_inbox_system.py",
        "type": "method",
        "class": "TransparentAgent",
        "description": "try: common_file = os.path.join(self.temp_dir, f\"snapshot_{self.agent_id}\") subprocess.run([ \"screen\", \"-S\", self.common_system.common_inbox_session, \"-X\", \"hardcopy\", common_file ], check=True)  with open(common_file, 'r') as f: content = f.read()  os.remove(common_file)  lines = [line for line in content.split('\\n') if line.strip() and \"] #\" in line]  return { \"agent_id\": self.agent_id, \"total_messages\": len(lines), \"recent_activity\": lines[-5:] if lines else [], \"message_types\": { \"direct\": len([l for l in lines if \"BROADCAST\" not in l]), \"broadcast\": len([l for l in lines if \"BROADCAST\" in l]) } }  except Exception: return {\"agent_id\": self.agent_id, \"error\": \"Failed to get snapshot\"}  def demonstrate_common_inbox():",
        "category": "inbox",
        "usage_pattern": "_check_personal_inbox() # Usage pattern for _check_personal_inbox",
        "safety_level": "moderate"
      },
      {
        "name": "show_simplified_architecture",
        "filename": "common_inbox_system.py",
        "type": "method",
        "class": "TransparentAgent",
        "description": "",
        "category": "inbox",
        "usage_pattern": "show_simplified_architecture() # Usage pattern for show_simplified_architecture",
        "safety_level": "moderate"
      }
    ]
  },
  {
    "name": "BroadcastMessage",
    "description": "class: BroadcastMessage",
    "type": "class",
    "category": "broadcasting",
    "filename": "broadcast_polling_system.py",
    "class": null,
    "examples": [
      "BroadcastMessage() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "high",
    "methods": [
      {
        "name": "__init__",
        "filename": "broadcast_polling_system.py",
        "type": "method",
        "class": "BroadcastMessage",
        "description": "",
        "category": "polling",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      },
      {
        "name": "start_polling",
        "filename": "broadcast_polling_system.py",
        "type": "method",
        "class": "BroadcastMessage",
        "description": "self.polling_active = True self._create_signal_session()  self.poll_thread = threading.Thread(target=self._adaptive_polling_loop, daemon=True) self.poll_thread.start() print(f\"[{self.agent_id}] Adaptive polling started\")  def stop_polling(self):",
        "category": "polling",
        "usage_pattern": "BroadcastPollingSystem.start_adaptive_polling()",
        "safety_level": "moderate"
      },
      {
        "name": "_create_signal_session",
        "filename": "broadcast_polling_system.py",
        "type": "method",
        "class": "BroadcastMessage",
        "description": "try: subprocess.run([\"screen\", \"-dmS\", self.signal_session], check=True) subprocess.run([ \"screen\", \"-S\", self.signal_session, \"-X\", \"stuff\", f\"echo 'Signal session for {self.agent_id} initialized'\\n\" ], check=True) except subprocess.CalledProcessError: pass  def _cleanup_signal_session(self):",
        "category": "polling",
        "usage_pattern": "_create_signal_session() # Usage pattern for _create_signal_session",
        "safety_level": "moderate"
      },
      {
        "name": "trigger_immediate_poll",
        "filename": "broadcast_polling_system.py",
        "type": "method",
        "class": "BroadcastMessage",
        "description": "try: # Send signal to own signal session subprocess.run([ \"screen\", \"-S\", self.signal_session, \"-X\", \"stuff\", f\"POLL_TRIGGER:{reason}:{datetime.now().isoformat()}\\n\" ], check=True)  print(f\"[{self.agent_id}] Poll trigger sent: {reason}\") except subprocess.CalledProcessError: print(f\"[{self.agent_id}] Failed to send poll trigger\")  def _adaptive_polling_loop(self):",
        "category": "polling",
        "usage_pattern": "trigger_immediate_poll() # Usage pattern for trigger_immediate_poll",
        "safety_level": "moderate"
      },
      {
        "name": "_check_poll_triggers",
        "filename": "broadcast_polling_system.py",
        "type": "method",
        "class": "BroadcastMessage",
        "description": "try: # Capture signal session signal_file = os.path.join(self.temp_dir, f\"signals_{self.agent_id}\") subprocess.run([ \"screen\", \"-S\", self.signal_session, \"-X\", \"hardcopy\", signal_file ], check=True)  with open(signal_file, 'r') as f: content = f.read()  os.remove(signal_file)  # Look for poll triggers lines = content.split('\\n') for line in lines: if \"POLL_TRIGGER:\" in line: parts = line.split(\"POLL_TRIGGER:\")[1].split(\":\") if parts: reason = parts[0] print(f\"[{self.agent_id}] Processing poll trigger: {reason}\")  # Adjust polling speed based on reason if reason in [\"broadcast\", \"urgent\"]: self._switch_to_urgent_polling()  # Clear the trigger by restarting session self._clear_signal_session()  except Exception as e: pass  # Signal checking is best-effort  def _switch_to_urgent_polling(self):",
        "category": "polling",
        "usage_pattern": "_check_poll_triggers() # Usage pattern for _check_poll_triggers",
        "safety_level": "moderate"
      },
      {
        "name": "reset_polling",
        "filename": "broadcast_polling_system.py",
        "type": "method",
        "class": "BroadcastMessage",
        "description": "",
        "category": "polling",
        "usage_pattern": "reset_polling() # Usage pattern for reset_polling",
        "safety_level": "moderate"
      },
      {
        "name": "_clear_signal_session",
        "filename": "broadcast_polling_system.py",
        "type": "method",
        "class": "BroadcastMessage",
        "description": "try: subprocess.run([ \"screen\", \"-S\", self.signal_session, \"-X\", \"stuff\", \"clear\\n\" ], check=True) except subprocess.CalledProcessError: pass  def _poll_inbox(self):",
        "category": "polling",
        "usage_pattern": "_clear_signal_session() # Usage pattern for _clear_signal_session",
        "safety_level": "moderate"
      },
      {
        "name": "_process_inbox_content",
        "filename": "broadcast_polling_system.py",
        "type": "method",
        "class": "BroadcastMessage",
        "description": "lines = content.split('\\n') for line in lines: if \"BROADCAST:\" in line: print(f\"[{self.agent_id}] Received broadcast: {line}\") # Handle broadcast message self._handle_broadcast_message(line) elif \"MSG from\" in line: print(f\"[{self.agent_id}] Received message: {line}\")  def _handle_broadcast_message(self, message: str):",
        "category": "polling",
        "usage_pattern": "_process_inbox_content() # Usage pattern for _process_inbox_content",
        "safety_level": "moderate"
      },
      {
        "name": "register_broadcast_handler",
        "filename": "broadcast_polling_system.py",
        "type": "method",
        "class": "BroadcastMessage",
        "description": "self.broadcast_handlers[name] = handler  class BroadcastSystem:",
        "category": "broadcasting",
        "usage_pattern": "register_broadcast_handler() # Usage pattern for register_broadcast_handler",
        "safety_level": "moderate"
      },
      {
        "name": "__init__",
        "filename": "broadcast_polling_system.py",
        "type": "method",
        "class": "BroadcastMessage",
        "description": "",
        "category": "polling",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      },
      {
        "name": "start_system",
        "filename": "broadcast_polling_system.py",
        "type": "method",
        "class": "BroadcastMessage",
        "description": "print(\"Starting broadcast system...\")  # Create screen sessions for agent in self.agents: try: subprocess.run([\"screen\", \"-dmS\", f\"{agent}_inbox\"], check=True) subprocess.run([\"screen\", \"-dmS\", f\"{agent}_outbox\"], check=True) except subprocess.CalledProcessError: pass  # Start polling for all agents for agent, manager in self.poll_managers.items(): manager.start_polling()  # Register default broadcast handler def make_handler(agent_id): def handler(sender, content): print(f\"[{agent_id}] BROADCAST RECEIVED from {sender}: {content}\") # Could trigger acknowledgment, logging, etc. return handler  manager.register_broadcast_handler(\"default\", make_handler(agent))  print(\"Broadcast system started!\")  def stop_system(self):",
        "category": "polling",
        "usage_pattern": "start_system() # Usage pattern for start_system",
        "safety_level": "moderate"
      },
      {
        "name": "send_broadcast",
        "filename": "broadcast_polling_system.py",
        "type": "method",
        "class": "BroadcastMessage",
        "description": "if sender not in self.agents: print(f\"Unknown sender: {sender}\") return  print(f\"\\n[BROADCAST] {sender} -> ALL: {message}\")  recipients = [agent for agent in self.agents if agent != sender]  # Send message to all recipient inboxes for recipient in recipients: try: subprocess.run([ \"screen\", \"-S\", f\"{recipient}_inbox\", \"-X\", \"stuff\", f\"MSG from {sender}: BROADCAST: {message}\\n\" ], check=True)  print(f\"  -> Delivered to {recipient}\")  except subprocess.CalledProcessError: print(f\"  -> Failed to deliver to {recipient}\")  # Log in sender's outbox try: subprocess.run([ \"screen\", \"-S\", f\"{sender}_outbox\", \"-X\", \"stuff\", f\"BROADCAST SENT to {len(recipients)} agents: {message}\\n\" ], check=True) except subprocess.CalledProcessError: pass  # Trigger immediate polling for all recipients for recipient in recipients: if recipient in self.poll_managers: self.poll_managers[recipient].trigger_immediate_poll(\"broadcast\")  print(f\"[BROADCAST] Poll triggers sent to {len(recipients)} agents\")  def demonstrate_broadcast_system():",
        "category": "broadcasting",
        "usage_pattern": "send_broadcast() # Usage pattern for send_broadcast",
        "safety_level": "moderate"
      }
    ]
  },
  {
    "name": "demonstrate_broadcast_triggers",
    "description": "print(\"BROADCAST TRIGGER MECHANISM\") print(\"=\" * 30)  agents = [\"agent1\", \"agent2\", \"agent3\"]  print(\"\\n1. NORMAL POLLING (every 5 seconds)\") print(\"   Each agent polls their inbox every 5 seconds\") print(\"   This is too slow for urgent broadcasts!\")  print(\"\\n2. BROADCAST TRIGGER MECHANISM\") print(\"   When agent sends broadcast:\") print(\"   a) Message goes to ALL recipient inboxes\") print(\"   b) IMMEDIATE poll trigger sent to each recipient\") print(\"   c) Recipients switch to urgent polling (0.5s)\") print(\"   d) After 10 seconds, return to normal polling\")  print(\"\\n3. IMPLEMENTATION:\") print(\"-\" * 15)  for i, agent in enumerate(agents, 1): print(f\"\\nAgent {i} ({agent}):\") print(f\"  Sessions: {agent}_inbox, {agent}_outbox, {agent}_signals\") print(f\"  Normal polling: Check {agent}_inbox every 5s\") print(f\"  Signal session: Receives poll triggers\") print(f\"  Urgent polling: Check {agent}_inbox every 0.5s\")  print(\"\\n4. BROADCAST SEQUENCE:\") print(\"-\" * 20) print(\"Step 1: agent1 sends broadcast 'Emergency meeting!'\") print(\"  -> Write to agent2_inbox: 'MSG from agent1: BROADCAST: Emergency meeting!'\") print(\"  -> Write to agent3_inbox: 'MSG from agent1: BROADCAST: Emergency meeting!'\") print(\"  -> Log in agent1_outbox: 'BROADCAST SENT to 2 agents'\")  print(\"\\nStep 2: Trigger immediate polling\") print(\"  -> Write to agent2_signals: 'POLL_TRIGGER:broadcast'\") print(\"  -> Write to agent3_signals: 'POLL_TRIGGER:broadcast'\")  print(\"\\nStep 3: Recipients detect triggers\") print(\"  -> agent2 checks agent2_signals, sees trigger\") print(\"  -> agent2 switches to urgent polling (0.5s intervals)\") print(\"  -> agent3 checks agent3_signals, sees trigger\") print(\"  -> agent3 switches to urgent polling (0.5s intervals)\")  print(\"\\nStep 4: Fast message delivery\") print(\"  -> Within 0.5s, both agents see the broadcast\") print(\"  -> Much faster than waiting up to 5s!\")  print(\"\\nStep 5: Return to normal\") print(\"  -> After 10s, agents return to 5s polling\")  def show_session_architecture():",
    "type": "function",
    "category": "broadcasting",
    "filename": "broadcast_trigger_demo.py",
    "class": null,
    "usage_pattern": "demonstrate_broadcast_triggers() # Usage pattern for demonstrate_broadcast_triggers",
    "examples": [
      "demonstrate_broadcast_triggers() # Basic usage",
      "# print(\"BROADCAST TRIGGER MECHANISM\") print(\"=\" * 30)  agents = [\"agent1\", \"agent2\", \"agent3\"]  print(\"\\n1. NORMAL POLLING (every 5 seconds)\") print(\"   Each agent polls their inbox every 5 seconds\") print(\"   This is too slow for urgent broadcasts!\")  print(\"\\n2. BROADCAST TRIGGER MECHANISM\") print(\"   When agent sends broadcast:\") print(\"   a) Message goes to ALL recipient inboxes\") print(\"   b) IMMEDIATE poll trigger sent to each recipient\") print(\"   c) Recipients switch to urgent polling (0.5s)\") print(\"   d) After 10 seconds, return to normal polling\")  print(\"\\n3. IMPLEMENTATION:\") print(\"-\" * 15)  for i, agent in enumerate(agents, 1): print(f\"\\nAgent {i} ({agent}):\") print(f\"  Sessions: {agent}_inbox, {agent}_outbox, {agent}_signals\") print(f\"  Normal polling: Check {agent}_inbox every 5s\") print(f\"  Signal session: Receives poll triggers\") print(f\"  Urgent polling: Check {agent}_inbox every 0.5s\")  print(\"\\n4. BROADCAST SEQUENCE:\") print(\"-\" * 20) print(\"Step 1: agent1 sends broadcast 'Emergency meeting!'\") print(\"  -> Write to agent2_inbox: 'MSG from agent1: BROADCAST: Emergency meeting!'\") print(\"  -> Write to agent3_inbox: 'MSG from agent1: BROADCAST: Emergency meeting!'\") print(\"  -> Log in agent1_outbox: 'BROADCAST SENT to 2 agents'\")  print(\"\\nStep 2: Trigger immediate polling\") print(\"  -> Write to agent2_signals: 'POLL_TRIGGER:broadcast'\") print(\"  -> Write to agent3_signals: 'POLL_TRIGGER:broadcast'\")  print(\"\\nStep 3: Recipients detect triggers\") print(\"  -> agent2 checks agent2_signals, sees trigger\") print(\"  -> agent2 switches to urgent polling (0.5s intervals)\") print(\"  -> agent3 checks agent3_signals, sees trigger\") print(\"  -> agent3 switches to urgent polling (0.5s intervals)\")  print(\"\\nStep 4: Fast message delivery\") print(\"  -> Within 0.5s, both agents see the broadcast\") print(\"  -> Much faster than waiting up to 5s!\")  print(\"\\nStep 5: Return to normal\") print(\"  -> After 10s, agents return to 5s polling\")  def show_session_architecture():"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "HierarchicalBroadcastRules",
    "description": "class: HierarchicalBroadcastRules",
    "type": "class",
    "category": "broadcasting",
    "filename": "hierarchical_broadcast_concept.py",
    "class": null,
    "examples": [
      "HierarchicalBroadcastRules() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "show_common_inbox_filtering",
        "filename": "hierarchical_broadcast_concept.py",
        "type": "method",
        "class": "HierarchicalBroadcastRules",
        "description": "print(\"\\n\\n\" + \"=\"*60) print(\"COMMON INBOX VIEW BY RANK\") print(\"=\"*60)  # Simulated common inbox messages (in chronological order) messages = [ {\"sender\": \"worker1\", \"rank\": Rank.WORKER, \"content\": \"Need help with task X\", \"priority\": 4}, {\"sender\": \"manager1\", \"rank\": Rank.MANAGER, \"content\": \"Team meeting at 3 PM\", \"priority\": 3}, {\"sender\": \"worker2\", \"rank\": Rank.WORKER, \"content\": \"Completed assignment A\", \"priority\": 4}, {\"sender\": \"ceo\", \"rank\": Rank.LEADER, \"content\": \"Quarterly results excellent!\", \"priority\": 2}, {\"sender\": \"user\", \"rank\": Rank.USER, \"content\": \"URGENT: System maintenance!\", \"priority\": 1} ]  rules = HierarchicalBroadcastRules()  # Show filtered view for each rank for viewer_rank in Rank: icon = {Rank.USER: \"👑\", Rank.LEADER: \"⭐\", Rank.MANAGER: \"🔶\", Rank.WORKER: \"🔸\"}[viewer_rank] print(f\"\\n{icon} {viewer_rank.name} VIEW OF COMMON INBOX:\") print(\"-\" * 30)  # Filter messages this rank can see visible_messages = [] for msg in messages: if rules.can_see_broadcast(viewer_rank, msg[\"rank\"]): visible_messages.append(msg)  # Sort by priority (user messages first) visible_messages.sort(key=lambda x: x[\"priority\"])  if visible_messages: for i, msg in enumerate(visible_messages, 1): sender_icon = {Rank.USER: \"👑\", Rank.LEADER: \"⭐\", Rank.MANAGER: \"🔶\", Rank.WORKER: \"🔸\"}[msg[\"rank\"]] print(f\"  {i}. {sender_icon} {msg['sender']}: {msg['content']}\") else: print(\"  (No messages visible)\")  def show_session_architecture():",
        "category": "hierarchy",
        "usage_pattern": "show_common_inbox_filtering() # Usage pattern for show_common_inbox_filtering",
        "safety_level": "safe"
      }
    ]
  },
  {
    "name": "HierarchicalBroadcastSystem",
    "description": "class: HierarchicalBroadcastSystem",
    "type": "class",
    "category": "broadcasting",
    "filename": "hierarchical_broadcast_system.py",
    "class": null,
    "examples": [
      "HierarchicalBroadcastSystem() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "setup_example_hierarchy",
        "filename": "hierarchical_broadcast_system.py",
        "type": "method",
        "class": "HierarchicalBroadcastSystem",
        "description": "# User (highest rank) self.add_agent(\"user\", Rank.USER)  # Leadership layer self.add_agent(\"ceo\", Rank.LEADER, reports_to=\"user\", manages=[\"manager1\", \"manager2\"])  # Management layer self.add_agent(\"manager1\", Rank.MANAGER, reports_to=\"ceo\", manages=[\"worker1\", \"worker2\"]) self.add_agent(\"manager2\", Rank.MANAGER, reports_to=\"ceo\", manages=[\"worker3\", \"worker4\"])  # Worker layer self.add_agent(\"worker1\", Rank.WORKER, reports_to=\"manager1\") self.add_agent(\"worker2\", Rank.WORKER, reports_to=\"manager1\") self.add_agent(\"worker3\", Rank.WORKER, reports_to=\"manager2\") self.add_agent(\"worker4\", Rank.WORKER, reports_to=\"manager2\")  def initialize_sessions(self):",
        "category": "hierarchy",
        "usage_pattern": "setup_example_hierarchy() # Usage pattern for setup_example_hierarchy",
        "safety_level": "moderate"
      },
      {
        "name": "cleanup_sessions",
        "filename": "hierarchical_broadcast_system.py",
        "type": "method",
        "class": "HierarchicalBroadcastSystem",
        "description": "return self.priority_order.get(broadcaster_rank, 999)  def log_hierarchical_broadcast(self, sender: str, content: str, broadcast_type: str = \"broadcast\"):",
        "category": "hierarchy",
        "usage_pattern": "ScreenAgentManager.cleanup_all_sessions()",
        "safety_level": "dangerous"
      },
      {
        "name": "send_direct_message",
        "filename": "hierarchical_broadcast_system.py",
        "type": "method",
        "class": "HierarchicalBroadcastSystem",
        "description": "if sender not in self.agents or recipient not in self.agents: print(f\"Unknown agent: {sender} or {recipient}\") return  sender_agent = self.agents[sender] recipient_agent = self.agents[recipient]  # Send to recipient's inbox try: subprocess.run([ \"screen\", \"-S\", f\"{recipient}_inbox\", \"-X\", \"stuff\", f\"DIRECT from {sender}: {content}\\n\" ], check=True) except subprocess.CalledProcessError: return  # Log to common inbox self.message_counter += 1 timestamp = datetime.now().strftime(\"%H:%M:%S\")  log_entry = (f\"[{timestamp}] #{self.message_counter:03d} \" f\"{sender_agent.rank.name} {sender} -> {recipient_agent.rank.name} {recipient}: {content}\")  try: subprocess.run([ \"screen\", \"-S\", self.common_inbox_session, \"-X\", \"stuff\", f\"{log_entry}\\n\" ], check=True) print(f\"[COMMON INBOX] {log_entry}\") except subprocess.CalledProcessError: pass  class HierarchicalAgent:",
        "category": "messaging",
        "usage_pattern": "send_direct_message() # Usage pattern for send_direct_message",
        "safety_level": "moderate"
      },
      {
        "name": "__init__",
        "filename": "hierarchical_broadcast_system.py",
        "type": "method",
        "class": "HierarchicalBroadcastSystem",
        "description": "",
        "category": "hierarchy",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      },
      {
        "name": "broadcast_message",
        "filename": "hierarchical_broadcast_system.py",
        "type": "method",
        "class": "HierarchicalBroadcastSystem",
        "description": "# Determine who should receive this broadcast my_rank = self.agent_info.rank recipients = []  for agent_id, agent in self.hierarchy_system.agents.items(): if (agent_id != self.agent_id and self.hierarchy_system.can_see_broadcast(agent.rank, my_rank)): recipients.append(agent_id)  # Send to recipient inboxes for recipient in recipients: try: subprocess.run([ \"screen\", \"-S\", f\"{recipient}_inbox\", \"-X\", \"stuff\", f\"BROADCAST from {my_rank.name} {self.agent_id}: {content}\\n\" ], check=True)  # Trigger polling subprocess.run([ \"screen\", \"-S\", f\"{recipient}_signals\", \"-X\", \"stuff\", f\"POLL_TRIGGER:broadcast\\n\" ], check=True) except subprocess.CalledProcessError: pass  # Log to own outbox try: subprocess.run([ \"screen\", \"-S\", self.outbox_session, \"-X\", \"stuff\", f\"BROADCAST ({my_rank.name}) to {len(recipients)} agents: {content}\\n\" ], check=True) except subprocess.CalledProcessError: pass  # Log to hierarchical common inbox self.hierarchy_system.log_hierarchical_broadcast(self.agent_id, content)  print(f\"[{self.agent_id}] Broadcast sent to {len(recipients)} agents\")  def send_direct_message(self, recipient: str, content: str):",
        "category": "broadcasting",
        "usage_pattern": "agent.broadcast_message(\"message\")",
        "safety_level": "moderate"
      },
      {
        "name": "start_monitoring",
        "filename": "hierarchical_broadcast_system.py",
        "type": "method",
        "class": "HierarchicalBroadcastSystem",
        "description": "self.monitoring_active = True self.monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True) self.monitor_thread.start() print(f\"[{self.agent_id}] Started hierarchical monitoring\")  def stop_monitoring(self):",
        "category": "hierarchy",
        "usage_pattern": "start_monitoring() # Usage pattern for start_monitoring",
        "safety_level": "moderate"
      },
      {
        "name": "_monitoring_loop",
        "filename": "hierarchical_broadcast_system.py",
        "type": "method",
        "class": "HierarchicalBroadcastSystem",
        "description": "while self.monitoring_active: try: # Monitor personal inbox self._check_personal_inbox()  # Monitor common inbox with hierarchy filtering self._check_hierarchical_common_inbox()  time.sleep(2)  except Exception as e: if self.monitoring_active: print(f\"[{self.agent_id}] Monitor error: {e}\") time.sleep(1)  def _check_personal_inbox(self):",
        "category": "hierarchy",
        "usage_pattern": "_monitoring_loop() # Usage pattern for _monitoring_loop",
        "safety_level": "moderate"
      },
      {
        "name": "_check_hierarchical_common_inbox",
        "filename": "hierarchical_broadcast_system.py",
        "type": "method",
        "class": "HierarchicalBroadcastSystem",
        "description": "my_rank = self.agent_info.rank  return { \"agent_id\": self.agent_id, \"my_rank\": my_rank.name, \"can_see_ranks\": [rank.name for rank in self.hierarchy_system.visibility_rules.get(my_rank, [])], \"reports_to\": self.agent_info.reports_to, \"manages\": self.agent_info.manages, \"hierarchy_peers\": [ agent_id for agent_id, agent in self.hierarchy_system.agents.items() if agent.rank == my_rank and agent_id != self.agent_id ] }  def demonstrate_hierarchical_broadcasts():",
        "category": "hierarchy",
        "usage_pattern": "_check_hierarchical_common_inbox() # Usage pattern for _check_hierarchical_common_inbox",
        "safety_level": "moderate"
      }
    ]
  },
  {
    "name": "CommunicationPatterns",
    "description": "class: CommunicationPatterns",
    "type": "class",
    "category": "communication",
    "filename": "communication_patterns.py",
    "class": null,
    "examples": [
      "CommunicationPatterns() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "star_topology_broadcast",
        "filename": "communication_patterns.py",
        "type": "method",
        "class": "CommunicationPatterns",
        "description": "if center_agent in network.agents: network.agents[center_agent].broadcast_message(f\"Star broadcast: {message}\")  @staticmethod def mesh_discussion(network: MultiAgentNetworkManager, topic: str):",
        "category": "broadcasting",
        "usage_pattern": "star_topology_broadcast() # Usage pattern for star_topology_broadcast",
        "safety_level": "safe"
      },
      {
        "name": "consensus_protocol",
        "filename": "communication_patterns.py",
        "type": "method",
        "class": "CommunicationPatterns",
        "description": "@staticmethod def create_negotiating_agents(network: MultiAgentNetworkManager):",
        "category": "patterns",
        "usage_pattern": "consensus_protocol() # Usage pattern for consensus_protocol",
        "safety_level": "safe"
      }
    ]
  },
  {
    "name": "CommunicationPermission",
    "description": "class: CommunicationPermission",
    "type": "class",
    "category": "communication",
    "filename": "omniscient_agent_system.py",
    "class": null,
    "examples": [
      "CommunicationPermission() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "ACTIVE",
    "description": "Configuration constant: ACTIVE",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "ACTIVE() # Basic usage",
      "# Configuration constant: ACTIVE"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "ANALYST",
    "description": "Configuration constant: ANALYST",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "ANALYST() # Basic usage",
      "# Configuration constant: ANALYST"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "ASSISTANT",
    "description": "Configuration constant: ASSISTANT",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "ASSISTANT() # Basic usage",
      "# Configuration constant: ASSISTANT"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "ASSISTANT",
    "description": "Configuration constant: ASSISTANT",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "ASSISTANT() # Basic usage",
      "# Configuration constant: ASSISTANT"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "BLOCKED",
    "description": "Configuration constant: BLOCKED",
    "type": "constant",
    "category": "configuration",
    "filename": "omniscient_agent_system.py",
    "class": null,
    "examples": [
      "BLOCKED() # Basic usage",
      "# Configuration constant: BLOCKED"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "BLOCKING",
    "description": "Configuration constant: BLOCKING",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrices.py",
    "class": null,
    "examples": [
      "BLOCKING() # Basic usage",
      "# Configuration constant: BLOCKING"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "BLOCKING",
    "description": "Configuration constant: BLOCKING",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrix_system.py",
    "class": null,
    "examples": [
      "BLOCKING() # Basic usage",
      "# Configuration constant: BLOCKING"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "BROADCAST",
    "description": "Configuration constant: BROADCAST",
    "type": "constant",
    "category": "configuration",
    "filename": "omniscient_agent_system.py",
    "class": null,
    "examples": [
      "BROADCAST() # Basic usage",
      "# Configuration constant: BROADCAST"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "COLLABORATIVE",
    "description": "Configuration constant: COLLABORATIVE",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrices.py",
    "class": null,
    "examples": [
      "COLLABORATIVE() # Basic usage",
      "# Configuration constant: COLLABORATIVE"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "COLLABORATIVE",
    "description": "Configuration constant: COLLABORATIVE",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrix_system.py",
    "class": null,
    "examples": [
      "COLLABORATIVE() # Basic usage",
      "# Configuration constant: COLLABORATIVE"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "CUSTOM",
    "description": "Configuration constant: CUSTOM",
    "type": "constant",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "CUSTOM() # Basic usage",
      "# Configuration constant: CUSTOM"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "DESIGNER",
    "description": "Configuration constant: DESIGNER",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "DESIGNER() # Basic usage",
      "# Configuration constant: DESIGNER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "DEVELOPER",
    "description": "Configuration constant: DEVELOPER",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "DEVELOPER() # Basic usage",
      "# Configuration constant: DEVELOPER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "DEVOPS",
    "description": "Configuration constant: DEVOPS",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "DEVOPS() # Basic usage",
      "# Configuration constant: DEVOPS"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "HIERARCHICAL",
    "description": "Configuration constant: HIERARCHICAL",
    "type": "constant",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "HIERARCHICAL() # Basic usage",
      "# Configuration constant: HIERARCHICAL"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "INFORMATIONAL",
    "description": "Configuration constant: INFORMATIONAL",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrices.py",
    "class": null,
    "examples": [
      "INFORMATIONAL() # Basic usage",
      "# Configuration constant: INFORMATIONAL"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "INFORMATIONAL",
    "description": "Configuration constant: INFORMATIONAL",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrix_system.py",
    "class": null,
    "examples": [
      "INFORMATIONAL() # Basic usage",
      "# Configuration constant: INFORMATIONAL"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "LEADER",
    "description": "Configuration constant: LEADER",
    "type": "constant",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "LEADER() # Basic usage",
      "# Configuration constant: LEADER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "LEADER",
    "description": "Configuration constant: LEADER",
    "type": "constant",
    "category": "configuration",
    "filename": "hierarchical_broadcast_concept.py",
    "class": null,
    "examples": [
      "LEADER() # Basic usage",
      "# Configuration constant: LEADER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "LEADER",
    "description": "Configuration constant: LEADER",
    "type": "constant",
    "category": "configuration",
    "filename": "hierarchical_broadcast_system.py",
    "class": null,
    "examples": [
      "LEADER() # Basic usage",
      "# Configuration constant: LEADER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "LINEAR",
    "description": "Configuration constant: LINEAR",
    "type": "constant",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "LINEAR() # Basic usage",
      "# Configuration constant: LINEAR"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "LINEAR",
    "description": "Configuration constant: LINEAR",
    "type": "constant",
    "category": "configuration",
    "filename": "hybrid_topology_system.py",
    "class": null,
    "examples": [
      "LINEAR() # Basic usage",
      "# Configuration constant: LINEAR"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "MANAGER",
    "description": "Configuration constant: MANAGER",
    "type": "constant",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "MANAGER() # Basic usage",
      "# Configuration constant: MANAGER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "MANAGER",
    "description": "Configuration constant: MANAGER",
    "type": "constant",
    "category": "configuration",
    "filename": "hierarchical_broadcast_concept.py",
    "class": null,
    "examples": [
      "MANAGER() # Basic usage",
      "# Configuration constant: MANAGER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "MANAGER",
    "description": "Configuration constant: MANAGER",
    "type": "constant",
    "category": "configuration",
    "filename": "hierarchical_broadcast_system.py",
    "class": null,
    "examples": [
      "MANAGER() # Basic usage",
      "# Configuration constant: MANAGER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "MANAGER",
    "description": "Configuration constant: MANAGER",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "MANAGER() # Basic usage",
      "# Configuration constant: MANAGER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "MESH",
    "description": "Configuration constant: MESH",
    "type": "constant",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "MESH() # Basic usage",
      "# Configuration constant: MESH"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "MESH",
    "description": "Configuration constant: MESH",
    "type": "constant",
    "category": "configuration",
    "filename": "hybrid_topology_system.py",
    "class": null,
    "examples": [
      "MESH() # Basic usage",
      "# Configuration constant: MESH"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "OBSERVE",
    "description": "Configuration constant: OBSERVE",
    "type": "constant",
    "category": "configuration",
    "filename": "omniscient_agent_system.py",
    "class": null,
    "examples": [
      "OBSERVE() # Basic usage",
      "# Configuration constant: OBSERVE"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "OBSERVER",
    "description": "Configuration constant: OBSERVER",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "OBSERVER() # Basic usage",
      "# Configuration constant: OBSERVER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "PARALLEL",
    "description": "Configuration constant: PARALLEL",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrices.py",
    "class": null,
    "examples": [
      "PARALLEL() # Basic usage",
      "# Configuration constant: PARALLEL"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "PARALLEL",
    "description": "Configuration constant: PARALLEL",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrix_system.py",
    "class": null,
    "examples": [
      "PARALLEL() # Basic usage",
      "# Configuration constant: PARALLEL"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "QA_TESTER",
    "description": "Configuration constant: QA_TESTER",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "QA_TESTER() # Basic usage",
      "# Configuration constant: QA_TESTER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "Rank",
    "description": "class: Rank",
    "type": "class",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "Rank() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "RECEIVE",
    "description": "Configuration constant: RECEIVE",
    "type": "constant",
    "category": "configuration",
    "filename": "omniscient_agent_system.py",
    "class": null,
    "examples": [
      "RECEIVE() # Basic usage",
      "# Configuration constant: RECEIVE"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "RING",
    "description": "Configuration constant: RING",
    "type": "constant",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "RING() # Basic usage",
      "# Configuration constant: RING"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "RING",
    "description": "Configuration constant: RING",
    "type": "constant",
    "category": "configuration",
    "filename": "hybrid_topology_system.py",
    "class": null,
    "examples": [
      "RING() # Basic usage",
      "# Configuration constant: RING"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "SEND",
    "description": "Configuration constant: SEND",
    "type": "constant",
    "category": "configuration",
    "filename": "omniscient_agent_system.py",
    "class": null,
    "examples": [
      "SEND() # Basic usage",
      "# Configuration constant: SEND"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "SEQUENTIAL",
    "description": "Configuration constant: SEQUENTIAL",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrices.py",
    "class": null,
    "examples": [
      "SEQUENTIAL() # Basic usage",
      "# Configuration constant: SEQUENTIAL"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "SEQUENTIAL",
    "description": "Configuration constant: SEQUENTIAL",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrix_system.py",
    "class": null,
    "examples": [
      "SEQUENTIAL() # Basic usage",
      "# Configuration constant: SEQUENTIAL"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "SILENT",
    "description": "Configuration constant: SILENT",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "SILENT() # Basic usage",
      "# Configuration constant: SILENT"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "STAR",
    "description": "Configuration constant: STAR",
    "type": "constant",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "STAR() # Basic usage",
      "# Configuration constant: STAR"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "STAR",
    "description": "Configuration constant: STAR",
    "type": "constant",
    "category": "configuration",
    "filename": "hybrid_topology_system.py",
    "class": null,
    "examples": [
      "STAR() # Basic usage",
      "# Configuration constant: STAR"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "SUPERVISORY",
    "description": "Configuration constant: SUPERVISORY",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrices.py",
    "class": null,
    "examples": [
      "SUPERVISORY() # Basic usage",
      "# Configuration constant: SUPERVISORY"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "SUPERVISORY",
    "description": "Configuration constant: SUPERVISORY",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrix_system.py",
    "class": null,
    "examples": [
      "SUPERVISORY() # Basic usage",
      "# Configuration constant: SUPERVISORY"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "SUPPORT",
    "description": "Configuration constant: SUPPORT",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "SUPPORT() # Basic usage",
      "# Configuration constant: SUPPORT"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "SUPPORTIVE",
    "description": "Configuration constant: SUPPORTIVE",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrices.py",
    "class": null,
    "examples": [
      "SUPPORTIVE() # Basic usage",
      "# Configuration constant: SUPPORTIVE"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "SUPPORTIVE",
    "description": "Configuration constant: SUPPORTIVE",
    "type": "constant",
    "category": "configuration",
    "filename": "dependency_matrix_system.py",
    "class": null,
    "examples": [
      "SUPPORTIVE() # Basic usage",
      "# Configuration constant: SUPPORTIVE"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "SystemConfig",
    "description": "class: SystemConfig",
    "type": "class",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "SystemConfig() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "TopicConfig",
    "description": "class: TopicConfig",
    "type": "class",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "TopicConfig() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "__post_init__",
        "filename": "configuration_variables.py",
        "type": "method",
        "class": "TopicConfig",
        "description": "return MasterConfig()  def create_simple_config(agents: List[str]) -> MasterConfig:",
        "category": "configuration",
        "usage_pattern": "__post_init__() # Usage pattern for __post_init__",
        "safety_level": "safe"
      }
    ]
  },
  {
    "name": "USER",
    "description": "Configuration constant: USER",
    "type": "constant",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "USER() # Basic usage",
      "# Configuration constant: USER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "USER",
    "description": "Configuration constant: USER",
    "type": "constant",
    "category": "configuration",
    "filename": "hierarchical_broadcast_concept.py",
    "class": null,
    "examples": [
      "USER() # Basic usage",
      "# Configuration constant: USER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "USER",
    "description": "Configuration constant: USER",
    "type": "constant",
    "category": "configuration",
    "filename": "hierarchical_broadcast_system.py",
    "class": null,
    "examples": [
      "USER() # Basic usage",
      "# Configuration constant: USER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "USER",
    "description": "Configuration constant: USER",
    "type": "constant",
    "category": "configuration",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "USER() # Basic usage",
      "# Configuration constant: USER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "WORKER",
    "description": "Configuration constant: WORKER",
    "type": "constant",
    "category": "configuration",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "WORKER() # Basic usage",
      "# Configuration constant: WORKER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "WORKER",
    "description": "Configuration constant: WORKER",
    "type": "constant",
    "category": "configuration",
    "filename": "hierarchical_broadcast_concept.py",
    "class": null,
    "examples": [
      "WORKER() # Basic usage",
      "# Configuration constant: WORKER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "WORKER",
    "description": "Configuration constant: WORKER",
    "type": "constant",
    "category": "configuration",
    "filename": "hierarchical_broadcast_system.py",
    "class": null,
    "examples": [
      "WORKER() # Basic usage",
      "# Configuration constant: WORKER"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "os",
      "pathlib"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "Dependency",
    "description": "class: Dependency",
    "type": "class",
    "category": "dependencies",
    "filename": "dependency_matrices.py",
    "class": null,
    "examples": [
      "Dependency() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "Dependency",
    "description": "class: Dependency",
    "type": "class",
    "category": "dependencies",
    "filename": "dependency_matrix_system.py",
    "class": null,
    "examples": [
      "Dependency() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "__init__",
        "filename": "dependency_matrix_system.py",
        "type": "method",
        "class": "Dependency",
        "description": "if from_agent not in self.agents or to_agent not in self.agents: raise ValueError(f\"Agents must be in system: {from_agent}, {to_agent}\")  dependency = Dependency( from_agent=from_agent, to_agent=to_agent, dependency_type=dep_type, strength=strength, bidirectional=bidirectional, condition=condition )  self.dependencies.append(dependency)  if bidirectional: reverse_dep = Dependency( from_agent=to_agent, to_agent=from_agent, dependency_type=dep_type, strength=strength, bidirectional=False,  # Avoid infinite recursion condition=condition ) self.dependencies.append(reverse_dep)  def generate_dependencies_from_rules(self):",
        "category": "dependencies",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      },
      {
        "name": "_apply_role_based_dependencies",
        "filename": "dependency_matrix_system.py",
        "type": "method",
        "class": "Dependency",
        "description": "print(\"\\nApplying ROLE-BASED dependencies...\")  # Find agents by role role_map = {} for agent in agents: role = agent.role if role not in role_map: role_map[role] = [] role_map[role].append(agent.agent_id)  # Rule: Tech leads have supervisory dependency on developers if 'tech_lead' in role_map: for tech_lead in role_map['tech_lead']: for role in ['frontend_developer', 'backend_developer', 'developer']: if role in role_map: for dev in role_map[role]: self.add_dependency(tech_lead, dev, DependencyType.SUPERVISORY, 0.8) self.add_dependency(dev, tech_lead, DependencyType.INFORMATIONAL, 0.7) print(f\"  ✓ {tech_lead} supervises {dev}\")  # Rule: Designers have collaborative dependency with frontend developers if 'designer' in role_map and 'frontend_developer' in role_map: for designer in role_map['designer']: for frontend in role_map['frontend_developer']: self.add_dependency(designer, frontend, DependencyType.COLLABORATIVE, 0.9, bidirectional=True) print(f\"  ✓ {designer} collaborates with {frontend}\")  # Rule: QA engineers have blocking dependency on developers for qa_role in ['qa_engineer', 'qa_manager']: if qa_role in role_map: for qa in role_map[qa_role]: for dev_role in ['frontend_developer', 'backend_developer']: if dev_role in role_map: for dev in role_map[dev_role]: self.add_dependency(qa, dev, DependencyType.BLOCKING, 0.8) print(f\"  ✓ {qa} blocked by {dev}\")  # Rule: DevOps has supportive dependency (others depend on DevOps) for devops_role in ['devops', 'devops_engineer']: if devops_role in role_map: for devops in role_map[devops_role]: for agent in agents: if agent.agent_id != devops and 'developer' in agent.role: self.add_dependency(agent.agent_id, devops, DependencyType.SUPPORTIVE, 0.6) print(f\"  ✓ {agent.agent_id} supported by {devops}\")  def _apply_phase_based_dependencies(self, project: ProjectFact, agents: List[AgentFact]):",
        "category": "dependencies",
        "usage_pattern": "_apply_role_based_dependencies() # Usage pattern for _apply_role_based_dependencies",
        "safety_level": "moderate"
      },
      {
        "name": "_apply_hierarchy_dependencies",
        "filename": "dependency_matrix_system.py",
        "type": "method",
        "class": "Dependency",
        "description": "print(\"\\nApplying HIERARCHY dependencies...\")  # Group by activity level (proxy for seniority) senior_agents = [a.agent_id for a in agents if a.activity_level == \"high\"] junior_agents = [a.agent_id for a in agents if a.activity_level == \"low\"]  # Senior agents have informational dependency on junior agents for senior in senior_agents: for junior in junior_agents: self.add_dependency(senior, junior, DependencyType.INFORMATIONAL, 0.5) self.add_dependency(junior, senior, DependencyType.SUPERVISORY, 0.6) print(f\"  ✓ Hierarchy: {senior} ↔ {junior}\")  def _apply_expertise_dependencies(self, agents: List[AgentFact]):",
        "category": "hierarchy",
        "usage_pattern": "_apply_hierarchy_dependencies() # Usage pattern for _apply_hierarchy_dependencies",
        "safety_level": "moderate"
      },
      {
        "name": "_apply_topology_dependencies",
        "filename": "dependency_matrix_system.py",
        "type": "method",
        "class": "Dependency",
        "description": "config = self.rule_system.derived_config topology = config.get('topology', 'mesh')  print(f\"\\nApplying {topology.upper()} TOPOLOGY dependencies...\")  if topology == \"star\": center = config.get('star_center', self.agents[0]) center_idx = self.agent_to_index[center]  # All agents have informational dependency on center for agent in self.agents: if agent != center: self.add_dependency(agent, center, DependencyType.INFORMATIONAL, 0.8) self.add_dependency(center, agent, DependencyType.SUPERVISORY, 0.7) print(f\"  ✓ Star: {agent} ↔ {center}\")  elif topology == \"linear\": # Sequential dependencies for i in range(len(self.agents) - 1): agent1 = self.agents[i] agent2 = self.agents[i + 1] self.add_dependency(agent2, agent1, DependencyType.SEQUENTIAL, 0.9) print(f\"  ✓ Linear: {agent2} → {agent1}\")  elif topology == \"hierarchical\": # Apply hierarchical dependencies (already done in hierarchy section) print(\"  ✓ Hierarchical dependencies applied via hierarchy rules\")  def build_matrices(self):",
        "category": "topology",
        "usage_pattern": "_apply_topology_dependencies() # Usage pattern for _apply_topology_dependencies",
        "safety_level": "moderate"
      },
      {
        "name": "_build_reachability_matrix",
        "filename": "dependency_matrix_system.py",
        "type": "method",
        "class": "Dependency",
        "description": "# Use Floyd-Warshall algorithm for transitive closure self.reachability_matrix = self.adjacency_matrix.copy()  for k in range(self.n_agents): for i in range(self.n_agents): for j in range(self.n_agents): self.reachability_matrix[i][j] = ( self.reachability_matrix[i][j] or (self.reachability_matrix[i][k] and self.reachability_matrix[k][j]) )  def _build_communication_matrix(self):",
        "category": "dependencies",
        "usage_pattern": "_build_reachability_matrix() # Usage pattern for _build_reachability_matrix",
        "safety_level": "moderate"
      },
      {
        "name": "build_dependency_graph",
        "filename": "dependency_matrix_system.py",
        "type": "method",
        "class": "Dependency",
        "description": "analysis = {}  # Critical dependencies (blocking) blocking_matrix = self.type_matrices[DependencyType.BLOCKING] critical_deps = [] for i in range(self.n_agents): for j in range(self.n_agents): if blocking_matrix[i][j] > 0.7:  # High strength blocking critical_deps.append((self.agents[i], self.agents[j], blocking_matrix[i][j])) analysis['critical_dependencies'] = critical_deps  # Communication hubs (high total communication requirements) comm_totals = np.sum(self.communication_matrix, axis=1) + np.sum(self.communication_matrix, axis=0) hub_idx = np.argmax(comm_totals) analysis['communication_hub'] = self.agents[hub_idx] analysis['hub_score'] = comm_totals[hub_idx]  # Isolated agents (low communication requirements) isolated_agents = [] for i, total in enumerate(comm_totals): if total < 0.5:  # Low communication isolated_agents.append(self.agents[i]) analysis['isolated_agents'] = isolated_agents  # Bottlenecks (agents many others depend on) in_degrees = np.sum(self.adjacency_matrix, axis=0) bottleneck_threshold = np.mean(in_degrees) + np.std(in_degrees) bottlenecks = [] for i, in_degree in enumerate(in_degrees): if in_degree > bottleneck_threshold: bottlenecks.append((self.agents[i], int(in_degree))) analysis['bottlenecks'] = bottlenecks  return analysis  def generate_polling_recommendations(self) -> Dict[str, float]:",
        "category": "dependencies",
        "usage_pattern": "build_dependency_graph() # Usage pattern for build_dependency_graph",
        "safety_level": "moderate"
      },
      {
        "name": "print_matrices",
        "filename": "dependency_matrix_system.py",
        "type": "method",
        "class": "Dependency",
        "description": "print(f\"\\nDEPENDENCY MATRICES\") print(\"=\" * 20)  # Helper function to print matrix def print_matrix(matrix, title): print(f\"\\n{title}:\") print(\"    \", end=\"\") for agent in self.agents: print(f\"{agent[:6]:>8}\", end=\"\") print()  for i, from_agent in enumerate(self.agents): print(f\"{from_agent[:6]:>6}\", end=\" \") for j, to_agent in enumerate(self.agents): value = matrix[i][j] if isinstance(value, bool): print(f\"{'T' if value else 'F':>8}\", end=\"\") else: print(f\"{value:.2f}:>8\", end=\"\") print()  # Print key matrices print_matrix(self.adjacency_matrix, \"ADJACENCY MATRIX (Direct Dependencies)\") print_matrix(self.reachability_matrix, \"REACHABILITY MATRIX (All Paths)\") print_matrix(self.communication_matrix, \"COMMUNICATION MATRIX (Final Requirements)\")  # Print type-specific matrices for important types important_types = [DependencyType.BLOCKING, DependencyType.COLLABORATIVE, DependencyType.SUPERVISORY] for dep_type in important_types: print_matrix(self.type_matrices[dep_type], f\"{dep_type.value.upper()} DEPENDENCIES\")  def demonstrate_dependency_system():",
        "category": "dependencies",
        "usage_pattern": "print_matrices() # Usage pattern for print_matrices",
        "safety_level": "moderate"
      }
    ]
  },
  {
    "name": "DependencyType",
    "description": "class: DependencyType",
    "type": "class",
    "category": "dependencies",
    "filename": "dependency_matrices.py",
    "class": null,
    "examples": [
      "DependencyType() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "DependencyType",
    "description": "class: DependencyType",
    "type": "class",
    "category": "dependencies",
    "filename": "dependency_matrix_system.py",
    "class": null,
    "examples": [
      "DependencyType() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "ProjectFact",
    "description": "class: ProjectFact",
    "type": "class",
    "category": "dependencies",
    "filename": "dependency_matrices.py",
    "class": null,
    "examples": [
      "ProjectFact() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "__init__",
        "filename": "dependency_matrices.py",
        "type": "method",
        "class": "ProjectFact",
        "description": "if from_agent not in self.agents or to_agent not in self.agents: raise ValueError(f\"Agents must be in system: {from_agent}, {to_agent}\")  dependency = Dependency( from_agent=from_agent, to_agent=to_agent, dependency_type=dep_type, strength=strength, bidirectional=bidirectional )  self.dependencies.append(dependency) print(f\"Added dependency: {from_agent} → {to_agent} ({dep_type.value}, {strength:.2f})\")  if bidirectional: reverse_dep = Dependency( from_agent=to_agent, to_agent=from_agent, dependency_type=dep_type, strength=strength, bidirectional=False ) self.dependencies.append(reverse_dep) print(f\"Added reverse: {to_agent} → {from_agent} ({dep_type.value}, {strength:.2f})\")  def generate_dependencies_from_context(self, agents_data: List[AgentFact], project: ProjectFact):",
        "category": "dependencies",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "safe"
      },
      {
        "name": "_apply_role_dependencies",
        "filename": "dependency_matrices.py",
        "type": "method",
        "class": "ProjectFact",
        "description": "print(\"\\nROLE-BASED DEPENDENCIES:\") print(\"-\" * 25)  # Create role mapping role_agents = {} for agent in agents_data: if agent.role not in role_agents: role_agents[agent.role] = [] role_agents[agent.role].append(agent.agent_id)  # Tech lead supervises developers if 'tech_lead' in role_agents: for tech_lead in role_agents['tech_lead']: for role in ['backend_developer', 'frontend_developer']: if role in role_agents: for dev in role_agents[role]: self.add_dependency(tech_lead, dev, DependencyType.SUPERVISORY, 0.8) self.add_dependency(dev, tech_lead, DependencyType.INFORMATIONAL, 0.7)  # Designer collaborates with frontend if 'designer' in role_agents and 'frontend_developer' in role_agents: for designer in role_agents['designer']: for frontend in role_agents['frontend_developer']: self.add_dependency(designer, frontend, DependencyType.COLLABORATIVE, 0.9, True)  # QA blocks on developers if 'qa_engineer' in role_agents: for qa in role_agents['qa_engineer']: for role in ['backend_developer', 'frontend_developer']: if role in role_agents: for dev in role_agents[role]: self.add_dependency(qa, dev, DependencyType.BLOCKING, 0.8)  # DevOps supports everyone if 'devops_engineer' in role_agents: for devops in role_agents['devops_engineer']: for agent in agents_data: if 'developer' in agent.role: self.add_dependency(agent.agent_id, devops, DependencyType.SUPPORTIVE, 0.6)  def _apply_phase_dependencies(self, project: ProjectFact, agents_data: List[AgentFact]):",
        "category": "dependencies",
        "usage_pattern": "_apply_role_dependencies() # Usage pattern for _apply_role_dependencies",
        "safety_level": "safe"
      },
      {
        "name": "_apply_expertise_dependencies",
        "filename": "dependency_matrices.py",
        "type": "method",
        "class": "ProjectFact",
        "description": "print(f\"\\nEXPERTISE DEPENDENCIES:\") print(\"-\" * 22)  for i, agent1 in enumerate(agents_data): for j, agent2 in enumerate(agents_data): if i != j: shared = agent1.expertise.intersection(agent2.expertise) if shared: strength = len(shared) / max(len(agent1.expertise), len(agent2.expertise)) if strength > 0.3:  # Significant overlap self.add_dependency(agent1.agent_id, agent2.agent_id, DependencyType.COLLABORATIVE, strength * 0.6)  def _apply_hierarchy_dependencies(self, agents_data: List[AgentFact]):",
        "category": "dependencies",
        "usage_pattern": "_apply_expertise_dependencies() # Usage pattern for _apply_expertise_dependencies",
        "safety_level": "safe"
      },
      {
        "name": "build_matrices",
        "filename": "dependency_matrices.py",
        "type": "method",
        "class": "ProjectFact",
        "description": "print(f\"\\nBUILDING MATRICES\") print(\"=\" * 17)  # Initialize matrices self.adjacency_matrix = np.zeros((self.n_agents, self.n_agents), dtype=int) self.strength_matrix = np.zeros((self.n_agents, self.n_agents))  # Initialize type-specific matrices for dep_type in DependencyType: self.type_matrices[dep_type] = np.zeros((self.n_agents, self.n_agents))  # Populate matrices for dep in self.dependencies: from_idx = self.agent_to_index[dep.from_agent] to_idx = self.agent_to_index[dep.to_agent]  # Adjacency matrix (binary) self.adjacency_matrix[from_idx][to_idx] = 1  # Strength matrix (weighted) self.strength_matrix[from_idx][to_idx] = max( self.strength_matrix[from_idx][to_idx], dep.strength )  # Type-specific matrix self.type_matrices[dep.dependency_type][from_idx][to_idx] = dep.strength  # Build derived matrices self._build_reachability_matrix() self._build_communication_matrix()  print(f\"✓ Adjacency Matrix: {self.n_agents}×{self.n_agents}\") print(f\"✓ Reachability Matrix (transitive closure)\") print(f\"✓ Strength Matrix (weighted)\") print(f\"✓ Type Matrices: {len(DependencyType)} types\") print(f\"✓ Communication Matrix (combined)\")  def _build_reachability_matrix(self):",
        "category": "dependencies",
        "usage_pattern": "build_matrices() # Usage pattern for build_matrices",
        "safety_level": "safe"
      },
      {
        "name": "_build_communication_matrix",
        "filename": "dependency_matrices.py",
        "type": "method",
        "class": "ProjectFact",
        "description": "# Weight different dependency types type_weights = { DependencyType.BLOCKING: 1.0,        # Highest priority DependencyType.SUPERVISORY: 0.9, DependencyType.COLLABORATIVE: 0.8, DependencyType.SEQUENTIAL: 0.7, DependencyType.INFORMATIONAL: 0.6, DependencyType.SUPPORTIVE: 0.5, DependencyType.PARALLEL: 0.3 }  self.communication_matrix = np.zeros((self.n_agents, self.n_agents))  for dep_type, weight in type_weights.items(): self.communication_matrix += self.type_matrices[dep_type] * weight  # Normalize to 0-1 range max_val = np.max(self.communication_matrix) if max_val > 0: self.communication_matrix /= max_val  def analyze_network(self):",
        "category": "communication",
        "usage_pattern": "_build_communication_matrix() # Usage pattern for _build_communication_matrix",
        "safety_level": "safe"
      },
      {
        "name": "_calculate_centrality",
        "filename": "dependency_matrices.py",
        "type": "method",
        "class": "ProjectFact",
        "description": "self.centrality_scores = {}  for i, agent in enumerate(self.agents): # In-degree centrality (how many depend on this agent) in_degree = np.sum(self.adjacency_matrix[:, i])  # Out-degree centrality (how many this agent depends on) out_degree = np.sum(self.adjacency_matrix[i, :])  # Communication centrality (total communication load) comm_in = np.sum(self.communication_matrix[:, i]) comm_out = np.sum(self.communication_matrix[i, :])  self.centrality_scores[agent] = { 'in_degree': in_degree, 'out_degree': out_degree, 'total_degree': in_degree + out_degree, 'comm_load': comm_in + comm_out }  print(\"Centrality Scores:\") for agent, scores in self.centrality_scores.items(): print(f\"  {agent}: in={scores['in_degree']}, out={scores['out_degree']}, \" f\"comm={scores['comm_load']:.2f}\")  def _find_communication_hubs(self):",
        "category": "dependencies",
        "usage_pattern": "_calculate_centrality() # Usage pattern for _calculate_centrality",
        "safety_level": "safe"
      },
      {
        "name": "_identify_bottlenecks",
        "filename": "dependency_matrices.py",
        "type": "method",
        "class": "ProjectFact",
        "description": "recommendations = {}  for i, agent in enumerate(self.agents): # Calculate communication intensity comm_intensity = (np.sum(self.communication_matrix[i, :]) + np.sum(self.communication_matrix[:, i]))  # Adjust polling based on intensity if comm_intensity > 1.5: factor = 0.3  # Very fast reason = \"High communication hub\" elif comm_intensity > 1.0: factor = 0.5  # Fast reason = \"Moderate communication load\" elif comm_intensity > 0.5: factor = 0.7  # Slightly faster reason = \"Some communication needs\" else: factor = 1.0  # Normal reason = \"Low communication needs\"  recommendations[agent] = { 'normal_interval': base_interval * factor, 'urgent_interval': base_interval * factor * 0.2, 'communication_intensity': comm_intensity, 'reasoning': reason }  return recommendations  def print_matrices(self):",
        "category": "dependencies",
        "usage_pattern": "_identify_bottlenecks() # Usage pattern for _identify_bottlenecks",
        "safety_level": "safe"
      },
      {
        "name": "print_matrix",
        "filename": "dependency_matrices.py",
        "type": "method",
        "class": "ProjectFact",
        "description": "",
        "category": "dependencies",
        "usage_pattern": "print_matrix() # Usage pattern for print_matrix",
        "safety_level": "safe"
      },
      {
        "name": "demonstrate_dependency_matrices",
        "filename": "dependency_matrices.py",
        "type": "method",
        "class": "ProjectFact",
        "description": "",
        "category": "dependencies",
        "usage_pattern": "demonstrate_dependency_matrices() # Usage pattern for demonstrate_dependency_matrices",
        "safety_level": "safe"
      }
    ]
  },
  {
    "name": "HierarchyConfig",
    "description": "class: HierarchyConfig",
    "type": "class",
    "category": "hierarchy",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "HierarchyConfig() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "__post_init__",
        "filename": "configuration_variables.py",
        "type": "method",
        "class": "HierarchyConfig",
        "description": "# Topology Settings topology_type: TopologyType = TopologyType.MESH dynamic_topology: bool = False              # Allow runtime topology changes  # Star Topology star_center_agent: str = \"agent1\"          # Which agent is center in star star_bidirectional: bool = True            # Star allows responses back to center  # Linear/Ring Topology linear_order: List[str] = None             # Order of agents in linear chain ring_direction: str = \"clockwise\"          # Direction for ring topology  # Mesh Topology mesh_full_connectivity: bool = True        # All agents connect to all others mesh_exclude_pairs: List[tuple] = None     # Agent pairs to exclude from mesh  # Hierarchical Topology hierarchy_layers: Dict[str, List[str]] = None  # Layer name -> agents in layer cross_layer_communication: bool = False    # Allow communication across layers  # Custom Topology custom_connections: Dict[str, List[str]] = None  # agent -> list of agents they can send to  # ============================================================================= # LOOP PREVENTION CONFIGURATION # =============================================================================  @dataclass class LoopPreventionConfig:",
        "category": "configuration",
        "usage_pattern": "__post_init__() # Usage pattern for __post_init__",
        "safety_level": "safe"
      }
    ]
  },
  {
    "name": "Rank",
    "description": "class: Rank",
    "type": "class",
    "category": "hierarchy",
    "filename": "hierarchical_broadcast_concept.py",
    "class": null,
    "examples": [
      "Rank() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "Rank",
    "description": "class: Rank",
    "type": "class",
    "category": "hierarchy",
    "filename": "hierarchical_broadcast_system.py",
    "class": null,
    "examples": [
      "Rank() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "CommonInboxSystem",
    "description": "class: CommonInboxSystem",
    "type": "class",
    "category": "inbox",
    "filename": "common_inbox_system.py",
    "class": null,
    "examples": [
      "CommonInboxSystem() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "cleanup_sessions",
        "filename": "common_inbox_system.py",
        "type": "method",
        "class": "CommonInboxSystem",
        "description": "def __init__(self, agent_id: str, all_agents: List[str], common_system: CommonInboxSystem): self.agent_id = agent_id self.all_agents = all_agents self.common_system = common_system self.temp_dir = tempfile.gettempdir()  # Personal sessions self.inbox_session = f\"{agent_id}_inbox\" self.outbox_session = f\"{agent_id}_outbox\" self.signals_session = f\"{agent_id}_signals\"  # Monitoring self.monitoring_active = False self.monitor_thread = None  def send_message(self, recipient: str, content: str):",
        "category": "inbox",
        "usage_pattern": "ScreenAgentManager.cleanup_all_sessions()",
        "safety_level": "dangerous"
      }
    ]
  },
  {
    "name": "demonstrate_message_flow",
    "description": "print(\"MESSAGE FLOW IN MULTI-AGENT SYSTEM\") print(\"=\" * 50)  print(\"\\nKEY INSIGHT: Agents don't capture each other's screens directly!\") print(\"Instead, they capture their OWN inbox to see messages sent TO them.\") print()  print(\"COMMUNICATION FLOW:\") print(\"-\" * 30) print(\"1. Agent A wants to send message to Agent B\") print(\"2. Agent A writes message to Agent B's INBOX session\") print(\"3. Agent B captures its OWN INBOX to see the message\") print(\"4. Agent B can respond by writing to Agent A's INBOX\") print()  print(\"DETAILED EXAMPLE - 2 Agents:\") print(\"-\" * 30) print(\"Sessions created:\") print(\"  • agent1_inbox    (Agent 1's mailbox)\") print(\"  • agent1_outbox   (Agent 1's sent log)\") print(\"  • agent2_inbox    (Agent 2's mailbox)\") print(\"  • agent2_outbox   (Agent 2's sent log)\") print()  print(\"Communication sequence:\") print(\"1. Agent 1 → Agent 2:\") print(\"   • Agent 1 executes: screen -S agent2_inbox -X stuff 'Hello Agent 2!'\") print(\"   • Agent 1 logs in own outbox: screen -S agent1_outbox -X stuff 'SENT TO agent2: Hello!'\") print(\"   • Agent 2 captures own inbox: screen -S agent2_inbox -X hardcopy /tmp/agent2_messages\") print(\"   • Agent 2 reads /tmp/agent2_messages and sees 'Hello Agent 2!'\") print()  print(\"2. Agent 2 → Agent 1 (response):\") print(\"   • Agent 2 executes: screen -S agent1_inbox -X stuff 'Hello back Agent 1!'\") print(\"   • Agent 2 logs in own outbox: screen -S agent2_outbox -X stuff 'SENT TO agent1: Hello back!'\") print(\"   • Agent 1 captures own inbox: screen -S agent1_inbox -X hardcopy /tmp/agent1_messages\") print(\"   • Agent 1 reads /tmp/agent1_messages and sees 'Hello back Agent 1!'\") print()  def demonstrate_hardcopy_mechanics():",
    "type": "function",
    "category": "messaging",
    "filename": "communication_flow_explained.py",
    "class": null,
    "usage_pattern": "demonstrate_message_flow() # Usage pattern for demonstrate_message_flow",
    "examples": [
      "demonstrate_message_flow() # Basic usage",
      "# print(\"MESSAGE FLOW IN MULTI-AGENT SYSTEM\") print(\"=\" * 50)  print(\"\\nKEY INSIGHT: Agents don't capture each other's screens directly!\") print(\"Instead, they capture their OWN inbox to see messages sent TO them.\") print()  print(\"COMMUNICATION FLOW:\") print(\"-\" * 30) print(\"1. Agent A wants to send message to Agent B\") print(\"2. Agent A writes message to Agent B's INBOX session\") print(\"3. Agent B captures its OWN INBOX to see the message\") print(\"4. Agent B can respond by writing to Agent A's INBOX\") print()  print(\"DETAILED EXAMPLE - 2 Agents:\") print(\"-\" * 30) print(\"Sessions created:\") print(\"  • agent1_inbox    (Agent 1's mailbox)\") print(\"  • agent1_outbox   (Agent 1's sent log)\") print(\"  • agent2_inbox    (Agent 2's mailbox)\") print(\"  • agent2_outbox   (Agent 2's sent log)\") print()  print(\"Communication sequence:\") print(\"1. Agent 1 → Agent 2:\") print(\"   • Agent 1 executes: screen -S agent2_inbox -X stuff 'Hello Agent 2!'\") print(\"   • Agent 1 logs in own outbox: screen -S agent1_outbox -X stuff 'SENT TO agent2: Hello!'\") print(\"   • Agent 2 captures own inbox: screen -S agent2_inbox -X hardcopy /tmp/agent2_messages\") print(\"   • Agent 2 reads /tmp/agent2_messages and sees 'Hello Agent 2!'\") print()  print(\"2. Agent 2 → Agent 1 (response):\") print(\"   • Agent 2 executes: screen -S agent1_inbox -X stuff 'Hello back Agent 1!'\") print(\"   • Agent 2 logs in own outbox: screen -S agent2_outbox -X stuff 'SENT TO agent1: Hello back!'\") print(\"   • Agent 1 captures own inbox: screen -S agent1_inbox -X hardcopy /tmp/agent1_messages\") print(\"   • Agent 1 reads /tmp/agent1_messages and sees 'Hello back Agent 1!'\") print()  def demonstrate_hardcopy_mechanics():"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "uuid",
      "datetime"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "demonstrate_message_routing",
    "description": "function: demonstrate_message_routing",
    "type": "function",
    "category": "messaging",
    "filename": "communication_flow_explained.py",
    "class": null,
    "usage_pattern": "demonstrate_message_routing() # Usage pattern for demonstrate_message_routing",
    "examples": [
      "demonstrate_message_routing() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "uuid",
      "datetime"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "GlobalMessage",
    "description": "class: GlobalMessage",
    "type": "class",
    "category": "messaging",
    "filename": "global_message_bus_system.py",
    "class": null,
    "examples": [
      "GlobalMessage() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "uuid",
      "datetime"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "__init__",
        "filename": "global_message_bus_system.py",
        "type": "method",
        "class": "GlobalMessage",
        "description": "",
        "category": "messaging",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      },
      {
        "name": "initialize_global_sessions",
        "filename": "global_message_bus_system.py",
        "type": "method",
        "class": "GlobalMessage",
        "description": "self.message_counter += 1 timestamp = datetime.now().isoformat()  # Create global message record global_msg = GlobalMessage( id=f\"msg_{self.message_counter:06d}\", sender=sender, recipient=recipient, content=content, timestamp=timestamp, message_type=message_type )  self.all_messages.append(global_msg)  # Format message for global sessions if message_type == \"broadcast\": log_entry = f\"[{timestamp}] BROADCAST {sender} -> ALL: {content}\" else: log_entry = f\"[{timestamp}] {sender} -> {recipient}: {content}\"  # Log to global inbox (all received messages) try: subprocess.run([ \"screen\", \"-S\", self.global_inbox_session, \"-X\", \"stuff\", f\"{log_entry}\\n\" ], check=True) except subprocess.CalledProcessError: pass  # Log to global outbox (all sent messages) try: subprocess.run([ \"screen\", \"-S\", self.global_outbox_session, \"-X\", \"stuff\", f\"{log_entry}\\n\" ], check=True) except subprocess.CalledProcessError: pass  # Log to global log with metadata try: metadata = f\"ID:{global_msg.id} TYPE:{message_type} SENDER:{sender} RECIPIENT:{recipient}\" subprocess.run([ \"screen\", \"-S\", self.global_log_session, \"-X\", \"stuff\", f\"[{timestamp}] {metadata} CONTENT:{content}\\n\" ], check=True) except subprocess.CalledProcessError: pass  print(f\"[GLOBAL BUS] Logged: {sender} -> {recipient}\")  class TransparentAgent:",
        "category": "messaging",
        "usage_pattern": "initialize_global_sessions() # Usage pattern for initialize_global_sessions",
        "safety_level": "moderate"
      },
      {
        "name": "__init__",
        "filename": "global_message_bus_system.py",
        "type": "method",
        "class": "GlobalMessage",
        "description": "",
        "category": "messaging",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      },
      {
        "name": "initialize_agent_sessions",
        "filename": "global_message_bus_system.py",
        "type": "method",
        "class": "GlobalMessage",
        "description": "sessions = [self.inbox_session, self.outbox_session, self.signals_session]  for session in sessions: try: subprocess.run([\"screen\", \"-dmS\", session], check=True) subprocess.run([ \"screen\", \"-S\", session, \"-X\", \"stuff\", f\"=== {session.upper()} INITIALIZED ===\\n\" ], check=True) except subprocess.CalledProcessError: pass  def cleanup_agent_sessions(self):",
        "category": "agents",
        "usage_pattern": "initialize_agent_sessions() # Usage pattern for initialize_agent_sessions",
        "safety_level": "moderate"
      },
      {
        "name": "send_message",
        "filename": "global_message_bus_system.py",
        "type": "method",
        "class": "GlobalMessage",
        "description": "# Send to recipient's personal inbox try: subprocess.run([ \"screen\", \"-S\", f\"{recipient}_inbox\", \"-X\", \"stuff\", f\"MSG from {self.agent_id}: {content}\\n\" ], check=True) except subprocess.CalledProcessError: print(f\"[{self.agent_id}] Failed to send to {recipient}\") return  # Log to own outbox try: subprocess.run([ \"screen\", \"-S\", self.outbox_session, \"-X\", \"stuff\", f\"SENT to {recipient}: {content}\\n\" ], check=True) except subprocess.CalledProcessError: pass  # LOG TO GLOBAL MESSAGE BUS self.global_bus.log_message_to_global_bus( sender=self.agent_id, recipient=recipient, content=content, message_type=\"direct\" )  print(f\"[{self.agent_id}] Sent to {recipient}: {content}\")  def broadcast_message(self, content: str):",
        "category": "messaging",
        "usage_pattern": "agent.send_message(\"recipient\", \"message\")",
        "safety_level": "moderate"
      },
      {
        "name": "start_monitoring",
        "filename": "global_message_bus_system.py",
        "type": "method",
        "class": "GlobalMessage",
        "description": "self.monitoring_active = True self.monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True) self.monitor_thread.start() print(f\"[{self.agent_id}] Started monitoring\")  def stop_monitoring(self):",
        "category": "messaging",
        "usage_pattern": "start_monitoring() # Usage pattern for start_monitoring",
        "safety_level": "moderate"
      },
      {
        "name": "_monitoring_loop",
        "filename": "global_message_bus_system.py",
        "type": "method",
        "class": "GlobalMessage",
        "description": "while self.monitoring_active: try: # Monitor personal inbox self._check_personal_inbox()  # Monitor global message bus self._check_global_activity()  time.sleep(2)  # Check every 2 seconds  except Exception as e: if self.monitoring_active: print(f\"[{self.agent_id}] Monitoring error: {e}\") time.sleep(1)  def _check_personal_inbox(self):",
        "category": "messaging",
        "usage_pattern": "_monitoring_loop() # Usage pattern for _monitoring_loop",
        "safety_level": "moderate"
      },
      {
        "name": "_check_global_activity",
        "filename": "global_message_bus_system.py",
        "type": "method",
        "class": "GlobalMessage",
        "description": "# Simple duplicate detection for global messages return False  def get_global_communication_summary(self) -> Dict:",
        "category": "messaging",
        "usage_pattern": "_check_global_activity() # Usage pattern for _check_global_activity",
        "safety_level": "moderate"
      },
      {
        "name": "demonstrate_global_message_bus",
        "filename": "global_message_bus_system.py",
        "type": "method",
        "class": "GlobalMessage",
        "description": "print(\"GLOBAL MESSAGE BUS SYSTEM\") print(\"=\" * 30)  agents = [\"agent1\", \"agent2\", \"agent3\", \"agent4\"]  # Create global message bus global_bus = GlobalMessageBus(agents) global_bus.initialize_global_sessions()  # Create transparent agents transparent_agents = {} for agent_id in agents: agent = TransparentAgent(agent_id, agents, global_bus) agent.initialize_agent_sessions() transparent_agents[agent_id] = agent  try: # Start monitoring for all agents for agent in transparent_agents.values(): agent.start_monitoring()  time.sleep(2)  # Let monitoring stabilize  print(\"\\n\" + \"=\"*50) print(\"SENDING MESSAGES WITH GLOBAL TRACKING...\") print(\"=\"*50)  # Send various messages transparent_agents[\"agent1\"].send_message(\"agent2\", \"Hello agent2, how are you?\") time.sleep(1)  transparent_agents[\"agent2\"].send_message(\"agent3\", \"Agent3, please start processing\") time.sleep(1)  transparent_agents[\"agent1\"].broadcast_message(\"Team meeting in 5 minutes!\") time.sleep(2)  transparent_agents[\"agent3\"].send_message(\"agent1\", \"Processing complete\") time.sleep(1)  transparent_agents[\"agent4\"].broadcast_message(\"System status: All normal\") time.sleep(2)  print(\"\\n\" + \"=\"*50) print(\"GLOBAL COMMUNICATION SUMMARIES...\") print(\"=\"*50)  # Get communication summaries for agent_id, agent in transparent_agents.items(): summary = agent.get_global_communication_summary() print(f\"\\n{agent_id.upper()} PERSPECTIVE:\") print(f\"  Total network messages seen: {summary.get('total_network_messages', 0)}\") print(f\"  Active agents: {', '.join(summary.get('agents_active', []))}\") if summary.get('recent_messages'): print(\"  Recent activity:\") for msg in summary['recent_messages'][-3:]: print(f\"    {msg}\")  print(\"\\nLetting system process messages...\") time.sleep(3)  except KeyboardInterrupt: print(\"\\nInterrupted...\") finally: # Cleanup for agent in transparent_agents.values(): agent.stop_monitoring() agent.cleanup_agent_sessions()  global_bus.cleanup_global_sessions()  def show_session_architecture():",
        "category": "messaging",
        "usage_pattern": "demonstrate_global_message_bus() # Usage pattern for demonstrate_global_message_bus",
        "safety_level": "moderate"
      }
    ]
  },
  {
    "name": "Message",
    "description": "class: Message",
    "type": "class",
    "category": "messaging",
    "filename": "multi_agent_screen_network.py",
    "class": null,
    "examples": [
      "Message() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "uuid",
      "datetime"
    ],
    "safety_level": "safe",
    "complexity": "high",
    "methods": [
      {
        "name": "__init__",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "",
        "category": "core",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "safe"
      },
      {
        "name": "start",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "self._create_sessions() self.running = True self.listener_thread = threading.Thread(target=self._message_listener, daemon=True) self.listener_thread.start() print(f\"Agent {self.agent_id} communication node started\")  def stop(self):",
        "category": "core",
        "usage_pattern": "start() # Usage pattern for start",
        "safety_level": "moderate"
      },
      {
        "name": "_create_sessions",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "for session in [self.inbox_session, self.outbox_session]: try: subprocess.run([\"screen\", \"-dmS\", session], check=True) # Initialize with a marker subprocess.run([ \"screen\", \"-S\", session, \"-X\", \"stuff\", f\"echo 'Session {session} initialized'\\n\" ], check=True) except subprocess.CalledProcessError: pass  def _cleanup_sessions(self):",
        "category": "core",
        "usage_pattern": "_create_sessions() # Usage pattern for _create_sessions",
        "safety_level": "moderate"
      },
      {
        "name": "send_message",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "message = Message( id=str(uuid.uuid4()), sender=self.agent_id, recipient=recipient, content=content, timestamp=datetime.now().isoformat(), message_type=message_type, metadata=metadata )  # Send to recipient's inbox recipient_inbox = f\"{recipient}_inbox\" try: # Write message as JSON to the recipient's inbox session subprocess.run([ \"screen\", \"-S\", recipient_inbox, \"-X\", \"stuff\", f\"echo 'MSG:{message.to_json()}'\\n\" ], check=True)  # Log in our outbox subprocess.run([ \"screen\", \"-S\", self.outbox_session, \"-X\", \"stuff\", f\"echo 'SENT:{message.to_json()}'\\n\" ], check=True)  return True except subprocess.CalledProcessError: return False  def broadcast_message(self, content: str, message_type: str = \"broadcast\", metadata: Dict = None):",
        "category": "messaging",
        "usage_pattern": "agent.send_message(\"recipient\", \"message\")",
        "safety_level": "safe"
      },
      {
        "name": "_message_listener",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "while self.running: try: # Capture inbox content output_file = os.path.join(self.temp_dir, f\"inbox_{self.agent_id}_output\") subprocess.run([ \"screen\", \"-S\", self.inbox_session, \"-X\", \"hardcopy\", output_file ], check=True)  # Read and parse messages with open(output_file, 'r') as f: content = f.read()  os.remove(output_file)  # Parse messages from content self._process_inbox_content(content)  except Exception as e: if self.running:  # Only log if we're supposed to be running print(f\"Error in message listener for {self.agent_id}: {e}\")  time.sleep(1)  # Check for messages every second  def _process_inbox_content(self, content: str):",
        "category": "messaging",
        "usage_pattern": "_message_listener() # Usage pattern for _message_listener",
        "safety_level": "safe"
      },
      {
        "name": "_handle_message",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "history = []  for session in [self.inbox_session, self.outbox_session]: try: output_file = os.path.join(self.temp_dir, f\"history_{session}_output\") subprocess.run([ \"screen\", \"-S\", session, \"-X\", \"hardcopy\", output_file ], check=True)  with open(output_file, 'r') as f: content = f.read()  os.remove(output_file) history.append(f\"=== {session} ===\") history.append(content)  except Exception: pass  return history  class MultiAgentNetworkManager:",
        "category": "messaging",
        "usage_pattern": "_handle_message() # Usage pattern for _handle_message",
        "safety_level": "safe"
      },
      {
        "name": "__init__",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "if agent_id in self.agents: raise ValueError(f\"Agent {agent_id} already exists\")  node = AgentCommunicationNode(agent_id, self) self.agents[agent_id] = node return node  def add_user(self, user_id: str = \"user\") -> AgentCommunicationNode:",
        "category": "core",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "safe"
      },
      {
        "name": "start_network",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "if self.user_node: self.user_node.start()  for agent in self.agents.values(): agent.start()  self._start_network_monitor() print(f\"Network started with {len(self.agents)} agents\" + (\" and 1 user\" if self.user_node else \"\"))  def stop_network(self):",
        "category": "network",
        "usage_pattern": "network.start_network()",
        "safety_level": "moderate"
      },
      {
        "name": "_start_network_monitor",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "status = { 'agents': {}, 'user': None, 'total_agents': len(self.agents), 'network_running': self.network_monitor_running }  for agent_id, agent in self.agents.items(): status['agents'][agent_id] = { 'running': agent.running, 'inbox_session': agent.inbox_session, 'outbox_session': agent.outbox_session }  if self.user_node: status['user'] = { 'id': self.user_node.agent_id, 'running': self.user_node.running }  return status  def broadcast_to_all(self, sender_id: str, message: str):",
        "category": "network",
        "usage_pattern": "_start_network_monitor() # Usage pattern for _start_network_monitor",
        "safety_level": "moderate"
      },
      {
        "name": "create_example_network",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "def create_2_agent_network():",
        "category": "network",
        "usage_pattern": "create_example_network() # Usage pattern for create_example_network",
        "safety_level": "moderate"
      },
      {
        "name": "agent1_handler",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "",
        "category": "agents",
        "usage_pattern": "agent1_handler() # Usage pattern for agent1_handler",
        "safety_level": "safe"
      },
      {
        "name": "agent2_handler",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "",
        "category": "agents",
        "usage_pattern": "agent2_handler() # Usage pattern for agent2_handler",
        "safety_level": "safe"
      },
      {
        "name": "create_4_agent_mesh_network",
        "filename": "multi_agent_screen_network.py",
        "type": "method",
        "class": "Message",
        "description": "",
        "category": "agents",
        "usage_pattern": "create_4_agent_mesh_network() # Usage pattern for create_4_agent_mesh_network",
        "safety_level": "moderate"
      }
    ]
  },
  {
    "name": "MessageState",
    "description": "class: MessageState",
    "type": "class",
    "category": "messaging",
    "filename": "loop_prevention_system.py",
    "class": null,
    "examples": [
      "MessageState() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "uuid",
      "datetime"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "cleanup_old_messages",
        "filename": "loop_prevention_system.py",
        "type": "method",
        "class": "MessageState",
        "description": "current_time = datetime.now() expired_messages = []  for msg_id, msg_state in self.processed_messages.items(): if current_time - msg_state.timestamp > self.message_ttl: expired_messages.append(msg_id)  for msg_id in expired_messages: msg_state = self.processed_messages.pop(msg_id) self.content_hashes.discard(msg_state.content_hash)  print(f\"[{self.agent_id}] Cleaned up {len(expired_messages)} expired messages\")  class SmartAgentNode:",
        "category": "messaging",
        "usage_pattern": "cleanup_old_messages() # Usage pattern for cleanup_old_messages",
        "safety_level": "dangerous"
      },
      {
        "name": "__init__",
        "filename": "loop_prevention_system.py",
        "type": "method",
        "class": "MessageState",
        "description": "# First check: Should we process this message at all? if not self.loop_prevention.should_process_message(message_content, sender): return None  # Record the message as processed message_state = self.loop_prevention.record_processed_message( message_content, sender )  # Determine message type and appropriate response response = self._generate_intelligent_response(message_content, sender)  # Check if we should actually send the response if response and self.loop_prevention.should_respond(message_state): self.loop_prevention.record_response_sent(message_state.message_id, response) return response  return None  def _generate_intelligent_response(self, message_content: str, sender: str) -> Optional[str]:",
        "category": "reliability",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      },
      {
        "name": "demonstrate_loop_prevention",
        "filename": "loop_prevention_system.py",
        "type": "method",
        "class": "MessageState",
        "description": "print(\"LOOP PREVENTION DEMONSTRATION\") print(\"=\" * 40)  # Create two agents agent1 = SmartAgentNode(\"agent1\") agent2 = SmartAgentNode(\"agent2\")  print(\"\\nSimulating conversation between agent1 and agent2:\") print(\"-\" * 50)  # Simulate message exchange messages = [ (\"agent1\", \"agent2\", \"Hello agent2!\"), (\"agent2\", \"agent1\", \"Hello agent1! How can I help you?\"), (\"agent1\", \"agent2\", \"Hello agent2!\"),  # Duplicate - should be ignored (\"agent2\", \"agent1\", \"What's the weather like?\"), (\"agent1\", \"agent2\", \"I understand your question. Let me process that...\"), (\"agent2\", \"agent1\", \"What's the weather like?\"),  # Duplicate - should be ignored (\"agent1\", \"agent2\", \"ACK\"),  # Should not generate response (\"agent2\", \"agent1\", \"ACK\"),  # Should not generate response ]  for sender, recipient, message in messages: print(f\"\\n{sender} -> {recipient}: '{message}'\")  if recipient == \"agent1\": response = agent1.process_incoming_message(message, sender) else: response = agent2.process_incoming_message(message, sender)  if response: print(f\"  {recipient} responds: '{response}'\") else: print(f\"  {recipient}: [No response - loop prevention]\")  def show_problematic_scenarios():",
        "category": "reliability",
        "usage_pattern": "demonstrate_loop_prevention() # Usage pattern for demonstrate_loop_prevention",
        "safety_level": "moderate"
      }
    ]
  },
  {
    "name": "ObserverAssistantSystem",
    "description": "class: ObserverAssistantSystem",
    "type": "class",
    "category": "monitoring",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "ObserverAssistantSystem() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen",
      "System monitoring permissions"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "psutil (optional)"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "setup_example_ecosystem",
        "filename": "observer_assistant_system.py",
        "type": "method",
        "class": "ObserverAssistantSystem",
        "description": "if agent_id not in self.agents: return False, f\"Agent {agent_id} not found\"  agent = self.agents[agent_id] rules = self.participation_rules[agent.participation_level]  # Can observe all topics if rules[\"can_observe_all\"] or \"all\" in agent.can_observe_topics: return True, \"Can observe all\"  # Check specific topic permissions if topic in agent.can_observe_topics: return True, f\"Can observe {topic} topic\"  # Assistant agents can observe messages from/to assisted agents if agent.participation_level == ParticipationLevel.ASSISTANT: if sender in agent.assists_agents: return True, f\"Observing assisted agent {sender}\"  return False, f\"{agent_id} cannot observe {topic} topic\"  def send_message(self, sender: str, recipient: str, content: str, topic: str = \"general\"):",
        "category": "roles",
        "usage_pattern": "setup_example_ecosystem() # Usage pattern for setup_example_ecosystem",
        "safety_level": "moderate"
      },
      {
        "name": "broadcast_message",
        "filename": "observer_assistant_system.py",
        "type": "method",
        "class": "ObserverAssistantSystem",
        "description": "can_broadcast, reason = self.can_agent_participate(sender, \"broadcast\", topic)  if not can_broadcast: print(f\"❌ BLOCKED: {reason}\") return False  sender_agent = self.agents[sender]  # Determine who can observe this broadcast observers = [] for agent_id, agent in self.agents.items(): if agent_id != sender: can_observe, _ = self.can_agent_observe(agent_id, topic, sender) if can_observe: observers.append(agent_id)  print(f\"📢 BROADCAST: {sender} ({sender_agent.role.value}) -> {len(observers)} observers\") print(f\"   Topic: {topic} | Content: {content}\") print(f\"   Observers: {', '.join(observers)}\")  # Log to common inbox self._log_to_common_inbox(sender, \"ALL\", content, topic, \"broadcast\")  return True  def request_assistance(self, requester: str, topic: str, content: str):",
        "category": "broadcasting",
        "usage_pattern": "agent.broadcast_message(\"message\")",
        "safety_level": "moderate"
      },
      {
        "name": "_log_to_common_inbox",
        "filename": "observer_assistant_system.py",
        "type": "method",
        "class": "ObserverAssistantSystem",
        "description": "sender_agent = self.agents[sender] participation_icon = { ParticipationLevel.ACTIVE: \"🟢\", ParticipationLevel.OBSERVER: \"👁️\", ParticipationLevel.ASSISTANT: \"🤝\", ParticipationLevel.SILENT: \"🔇\", ParticipationLevel.SUPPORT: \"🛠️\" }.get(sender_agent.participation_level, \"❓\")  log_entry = f\"[{topic}] {participation_icon} {sender} -> {recipient}: {content}\" print(f\"📝 COMMON INBOX: {log_entry}\")  def show_ecosystem_overview(self):",
        "category": "roles",
        "usage_pattern": "_log_to_common_inbox() # Usage pattern for _log_to_common_inbox",
        "safety_level": "moderate"
      },
      {
        "name": "demonstrate_observer_assistant_system",
        "filename": "observer_assistant_system.py",
        "type": "method",
        "class": "ObserverAssistantSystem",
        "description": "",
        "category": "monitoring",
        "usage_pattern": "demonstrate_observer_assistant_system() # Usage pattern for demonstrate_observer_assistant_system",
        "safety_level": "moderate"
      }
    ]
  },
  {
    "name": "PermissionRule",
    "description": "class: PermissionRule",
    "type": "class",
    "category": "permissions",
    "filename": "omniscient_agent_system.py",
    "class": null,
    "examples": [
      "PermissionRule() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "__init__",
        "filename": "omniscient_agent_system.py",
        "type": "method",
        "class": "PermissionRule",
        "description": "",
        "category": "monitoring",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      },
      {
        "name": "set_permission",
        "filename": "omniscient_agent_system.py",
        "type": "method",
        "class": "PermissionRule",
        "description": "perm = self.get_permission(from_agent, to_agent) return perm in [CommunicationPermission.SEND, CommunicationPermission.BROADCAST]  def can_observe(self, observer: str, target: str) -> bool:",
        "category": "permissions",
        "usage_pattern": "set_permission() # Usage pattern for set_permission",
        "safety_level": "moderate"
      },
      {
        "name": "add_global_observer",
        "filename": "omniscient_agent_system.py",
        "type": "method",
        "class": "PermissionRule",
        "description": "self.global_observers.add(agent)  def configure_linear_topology(self):",
        "category": "monitoring",
        "usage_pattern": "add_global_observer() # Usage pattern for add_global_observer",
        "safety_level": "moderate"
      },
      {
        "name": "configure_ring_topology",
        "filename": "omniscient_agent_system.py",
        "type": "method",
        "class": "PermissionRule",
        "description": "self.configure_linear_topology()  # Add the ring closure: last -> first if len(self.agents) > 1: last = self.agents[-1] first = self.agents[0] self.set_permission(last, first, CommunicationPermission.SEND) self.set_permission(first, last, CommunicationPermission.RECEIVE)  def configure_star_topology(self, center_agent: str):",
        "category": "topology",
        "usage_pattern": "configure_ring_topology() # Usage pattern for configure_ring_topology",
        "safety_level": "moderate"
      },
      {
        "name": "configure_mesh_topology",
        "filename": "omniscient_agent_system.py",
        "type": "method",
        "class": "PermissionRule",
        "description": "self._clear_permissions()  for agent1 in self.agents: for agent2 in self.agents: if agent1 != agent2: self.set_permission(agent1, agent2, CommunicationPermission.SEND) self.set_permission(agent1, agent2, CommunicationPermission.OBSERVE)  def configure_hierarchical_topology(self):",
        "category": "topology",
        "usage_pattern": "configure_mesh_topology() # Usage pattern for configure_mesh_topology",
        "safety_level": "moderate"
      },
      {
        "name": "_clear_permissions",
        "filename": "omniscient_agent_system.py",
        "type": "method",
        "class": "PermissionRule",
        "description": "self.permission_matrix.clear() self.global_observers.clear()  class OmniscientAgent:",
        "category": "permissions",
        "usage_pattern": "_clear_permissions() # Usage pattern for _clear_permissions",
        "safety_level": "moderate"
      },
      {
        "name": "__init__",
        "filename": "omniscient_agent_system.py",
        "type": "method",
        "class": "PermissionRule",
        "description": "self.capture_all_screens() observable = self.get_observable_screens()  report = { \"agent_id\": self.agent_id, \"timestamp\": time.time(), \"total_screens_captured\": len(self.screen_data), \"observable_screens\": len(observable), \"blocked_screens\": len(self.screen_data) - len(observable), \"permissions\": {}, \"intelligence\": [] }  # Add permission summary for agent in self.all_agents: if agent != self.agent_id: report[\"permissions\"][agent] = { \"can_send\": self.permission_manager.can_send(self.agent_id, agent), \"can_observe\": self.permission_manager.can_observe(self.agent_id, agent) }  # Add intelligence from observable screens for screen_name, content in observable.items(): if content.strip(): report[\"intelligence\"].append({ \"screen\": screen_name, \"content_length\": len(content), \"has_messages\": \"MSG from\" in content })  return report  def demonstrate_omniscient_system():",
        "category": "monitoring",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      }
    ]
  },
  {
    "name": "ParticipationLevel",
    "description": "class: ParticipationLevel",
    "type": "class",
    "category": "roles",
    "filename": "observer_assistant_system.py",
    "class": null,
    "examples": [
      "ParticipationLevel() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "Fact",
    "description": "class: Fact",
    "type": "class",
    "category": "rules",
    "filename": "prolog_rule_system.py",
    "class": null,
    "examples": [
      "Fact() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen",
      "SWI-Prolog (optional)"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "typing",
      "dataclasses"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "ProjectFact",
    "description": "class: ProjectFact",
    "type": "class",
    "category": "rules",
    "filename": "rule_based_agent_config.py",
    "class": null,
    "examples": [
      "ProjectFact() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "typing",
      "dataclasses"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "RuleBasedConfigSystem",
    "description": "class: RuleBasedConfigSystem",
    "type": "class",
    "category": "rules",
    "filename": "rule_based_agent_config.py",
    "class": null,
    "examples": [
      "RuleBasedConfigSystem() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "typing",
      "dataclasses"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "set_project_context",
        "filename": "rule_based_agent_config.py",
        "type": "method",
        "class": "RuleBasedConfigSystem",
        "description": "self.project = ProjectFact(project_type, phase, urgency, team_size, distribution)  def generate_configuration(self) -> Dict[str, Any]:",
        "category": "rules",
        "usage_pattern": "set_project_context() # Usage pattern for set_project_context",
        "safety_level": "safe"
      },
      {
        "name": "_apply_topology_rules",
        "filename": "rule_based_agent_config.py",
        "type": "method",
        "class": "RuleBasedConfigSystem",
        "description": "print(\"\\nApplying TOPOLOGY rules...\")  # Rule 1: Small startup teams use MESH for flexibility if (self.project.project_type == \"startup\" and self.project.team_size <= 6): self.derived_config[\"topology\"] = \"mesh\" self.derived_config[\"topology_reason\"] = \"Small startup team needs maximum flexibility\" print(\"  ✓ Rule: startup_small_team → mesh topology\")  # Rule 2: Large enterprise teams use HIERARCHICAL for structure elif (self.project.project_type == \"enterprise\" and self.project.team_size > 10): self.derived_config[\"topology\"] = \"hierarchical\" self.derived_config[\"topology_reason\"] = \"Large enterprise team needs clear structure\" print(\"  ✓ Rule: enterprise_large_team → hierarchical topology\")  # Rule 3: Development phase with high coordination needs STAR elif (self.project.phase == \"development\" and self._has_role(\"tech_lead\") and self.project.urgency in [\"critical\", \"urgent\"]): self.derived_config[\"topology\"] = \"star\" self.derived_config[\"star_center\"] = self._find_agent_by_role(\"tech_lead\") self.derived_config[\"topology_reason\"] = \"Critical development needs central coordination\" print(\"  ✓ Rule: critical_development → star topology with tech lead center\")  # Rule 4: Testing phase uses LINEAR for systematic testing elif self.project.phase == \"testing\": self.derived_config[\"topology\"] = \"linear\" self.derived_config[\"topology_reason\"] = \"Testing phase needs systematic handoffs\" print(\"  ✓ Rule: testing_phase → linear topology\")  # Rule 5: Planning phase uses MESH for brainstorming elif self.project.phase == \"planning\": self.derived_config[\"topology\"] = \"mesh\" self.derived_config[\"topology_reason\"] = \"Planning needs open collaboration\" print(\"  ✓ Rule: planning_phase → mesh topology\")  # Default: Medium mesh for balanced communication else: self.derived_config[\"topology\"] = \"mesh\" self.derived_config[\"topology_reason\"] = \"Default balanced communication\" print(\"  ✓ Rule: default → mesh topology\")  def _apply_polling_rules(self):",
        "category": "topology",
        "usage_pattern": "_apply_topology_rules() # Usage pattern for _apply_topology_rules",
        "safety_level": "safe"
      },
      {
        "name": "_apply_participation_rules",
        "filename": "rule_based_agent_config.py",
        "type": "method",
        "class": "RuleBasedConfigSystem",
        "description": "return any(agent.activity_level == \"high\" for agent in self.agents)  def show_knowledge_base(self):",
        "category": "rules",
        "usage_pattern": "_apply_participation_rules() # Usage pattern for _apply_participation_rules",
        "safety_level": "safe"
      },
      {
        "name": "demonstrate_rule_based_scenarios",
        "filename": "rule_based_agent_config.py",
        "type": "method",
        "class": "RuleBasedConfigSystem",
        "description": "",
        "category": "rules",
        "usage_pattern": "demonstrate_rule_based_scenarios() # Usage pattern for demonstrate_rule_based_scenarios",
        "safety_level": "safe"
      }
    ]
  },
  {
    "name": "TeamFact",
    "description": "class: TeamFact",
    "type": "class",
    "category": "rules",
    "filename": "prolog_rule_system.py",
    "class": null,
    "examples": [
      "TeamFact() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen",
      "SWI-Prolog (optional)"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "typing",
      "dataclasses"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "WorkflowFact",
    "description": "class: WorkflowFact",
    "type": "class",
    "category": "rules",
    "filename": "prolog_rule_system.py",
    "class": null,
    "examples": [
      "WorkflowFact() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen",
      "SWI-Prolog (optional)"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "typing",
      "dataclasses"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "__init__",
        "filename": "prolog_rule_system.py",
        "type": "method",
        "class": "WorkflowFact",
        "description": "if all(knowledge_base.query(condition) for condition in self.conditions): return self.conclusions return []  class KnowledgeBase:",
        "category": "rules",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      },
      {
        "name": "__init__",
        "filename": "prolog_rule_system.py",
        "type": "method",
        "class": "WorkflowFact",
        "description": "",
        "category": "rules",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      },
      {
        "name": "add_fact",
        "filename": "prolog_rule_system.py",
        "type": "method",
        "class": "WorkflowFact",
        "description": "content = pattern[pattern.find('(')+1:pattern.rfind(')')] return [part.strip() for part in content.split(',')]  def _match_value(self, pattern_value: str, actual_value: str) -> bool:",
        "category": "rules",
        "usage_pattern": "add_fact() # Usage pattern for add_fact",
        "safety_level": "moderate"
      },
      {
        "name": "infer",
        "filename": "prolog_rule_system.py",
        "type": "method",
        "class": "WorkflowFact",
        "description": "changed = True iterations = 0 max_iterations = 10  while changed and iterations < max_iterations: changed = False iterations += 1  # Sort rules by priority (higher priority first) sorted_rules = sorted(self.rules, key=lambda r: r.priority, reverse=True)  for rule in sorted_rules: conclusions = rule.evaluate(self) for conclusion in conclusions: if conclusion not in self.derived_facts: self.derived_facts.add(conclusion) changed = True print(f\"Derived: {conclusion} (from rule: {rule.name})\")  class AgentConfigurationSystem:",
        "category": "rules",
        "usage_pattern": "infer() # Usage pattern for infer",
        "safety_level": "moderate"
      },
      {
        "name": "__init__",
        "filename": "prolog_rule_system.py",
        "type": "method",
        "class": "WorkflowFact",
        "description": "",
        "category": "rules",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      },
      {
        "name": "_setup_rules",
        "filename": "prolog_rule_system.py",
        "type": "method",
        "class": "WorkflowFact",
        "description": "# TOPOLOGY RULES self.kb.add_rule(Rule( name=\"startup_mesh_topology\", conditions=[ \"project(startup, _, _, _)\", \"team(_, _, SIZE, _)\", # SIZE <= 6 would need custom logic ], conclusions=[\"topology(mesh)\", \"reason(small_team_needs_flexibility)\"], priority=10 ))  self.kb.add_rule(Rule( name=\"enterprise_hierarchical_topology\", conditions=[ \"project(enterprise, _, _, _)\", \"team(_, _, SIZE, _)\", # SIZE > 10 would need custom logic ], conclusions=[\"topology(hierarchical)\", \"reason(large_team_needs_structure)\"], priority=9 ))  self.kb.add_rule(Rule( name=\"development_phase_star_topology\", conditions=[ \"project(_, development, _, _)\", \"workflow(sequential)\" ], conclusions=[\"topology(star)\", \"star_center(tech_lead)\", \"reason(central_coordination_needed)\"], priority=8 ))  # POLLING FREQUENCY RULES self.kb.add_rule(Rule( name=\"critical_project_fast_polling\", conditions=[ \"project(_, _, critical, _)\" ], conclusions=[\"poll_interval(0.5)\", \"urgent_mode(enabled)\", \"reason(critical_timeline)\"], priority=10 ))  self.kb.add_rule(Rule( name=\"high_activity_agents_fast_polling\", conditions=[ \"agent(_, _, high)\" ], conclusions=[\"agent_poll_interval(1.0)\", \"reason(high_activity_needs_responsiveness)\"], priority=8 ))  self.kb.add_rule(Rule( name=\"distributed_team_frequent_polling\", conditions=[ \"project(_, _, _, distributed)\" ], conclusions=[\"poll_interval(1.0)\", \"broadcast_priority(high)\", \"reason(async_coordination)\"], priority=7 ))  # PARTICIPATION LEVEL RULES self.kb.add_rule(Rule( name=\"manager_active_participation\", conditions=[ \"agent(_, manager, _)\" ], conclusions=[\"participation_level(active)\", \"can_broadcast(true)\", \"reason(leadership_role)\"], priority=9 ))  self.kb.add_rule(Rule( name=\"intern_observer_participation\", conditions=[ \"agent(_, intern, _)\" ], conclusions=[\"participation_level(observer)\", \"can_broadcast(false)\", \"reason(learning_role)\"], priority=8 ))  self.kb.add_rule(Rule( name=\"designer_assistant_to_frontend\", conditions=[ \"agent(DESIGNER, designer, _)\", \"agent(FRONTEND, frontend_developer, _)\" ], conclusions=[\"assists(DESIGNER, FRONTEND)\", \"participation_level(assistant)\", \"reason(ui_collaboration)\"], priority=7 ))  # BROADCAST RULES self.kb.add_rule(Rule( name=\"testing_phase_qa_broadcasts\", conditions=[ \"project(_, testing, _, _)\", \"agent(_, qa_engineer, _)\" ], conclusions=[\"broadcast_priority(high)\", \"topic_focus(testing)\", \"reason(quality_focus)\"], priority=8 ))  self.kb.add_rule(Rule( name=\"deployment_phase_devops_priority\", conditions=[ \"project(_, deployment, _, _)\", \"agent(_, devops, _)\" ], conclusions=[\"broadcast_priority(critical)\", \"immediate_polling(true)\", \"reason(deployment_critical)\"], priority=10 ))  # TEAM COORDINATION RULES self.kb.add_rule(Rule( name=\"high_coordination_need_mesh\", conditions=[ \"team(_, _, _, high)\" ], conclusions=[\"team_topology(mesh)\", \"frequent_broadcasts(enabled)\", \"reason(tight_coordination)\"], priority=8 ))  self.kb.add_rule(Rule( name=\"low_coordination_hierarchical\", conditions=[ \"team(_, _, _, low)\" ], conclusions=[\"team_topology(hierarchical)\", \"broadcast_limit(managers_only)\", \"reason(minimal_overhead)\"], priority=6 ))  # WORKFLOW-BASED RULES self.kb.add_rule(Rule( name=\"sequential_workflow_linear_topology\", conditions=[ \"workflow(sequential)\" ], conclusions=[\"topology(linear)\", \"handoff_notifications(enabled)\", \"reason(sequential_dependencies)\"], priority=7 ))  self.kb.add_rule(Rule( name=\"parallel_workflow_mesh_topology\", conditions=[ \"workflow(parallel)\" ], conclusions=[\"topology(mesh)\", \"concurrent_broadcasts(enabled)\", \"reason(parallel_coordination)\"], priority=7 ))  def add_agent(self, agent_id: str, role: str, activity_level: str, domain_expertise: Set[str], team: str = None, reports_to: str = None):",
        "category": "rules",
        "usage_pattern": "_setup_rules() # Usage pattern for _setup_rules",
        "safety_level": "moderate"
      },
      {
        "name": "add_team",
        "filename": "prolog_rule_system.py",
        "type": "method",
        "class": "WorkflowFact",
        "description": "self.kb.add_fact(TeamFact( team_id=team_id, team_type=team_type, size=size, coordination_need=coordination_need ))  def add_project_context(self, project_type: str, phase: str, urgency: str, team_distribution: str):",
        "category": "rules",
        "usage_pattern": "add_team() # Usage pattern for add_team",
        "safety_level": "moderate"
      },
      {
        "name": "add_workflow",
        "filename": "prolog_rule_system.py",
        "type": "method",
        "class": "WorkflowFact",
        "description": "reasons = [] for fact in self.kb.derived_facts: if fact.startswith(\"reason(\"): reason = fact[fact.find('(')+1:fact.rfind(')')] reasons.append(reason) return reasons  def demonstrate_rule_based_system():",
        "category": "rules",
        "usage_pattern": "add_workflow() # Usage pattern for add_workflow",
        "safety_level": "moderate"
      }
    ]
  },
  {
    "name": "ScreenAgentManager",
    "description": "class: ScreenAgentManager",
    "type": "class",
    "category": "screen",
    "filename": "screen_agent_manager.py",
    "class": null,
    "examples": [
      "ScreenAgentManager() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time",
      "screen command-line tool"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "__init__",
        "filename": "screen_agent_manager.py",
        "type": "method",
        "class": "ScreenAgentManager",
        "description": "try: result = subprocess.run([ \"screen\", \"-list\" ], capture_output=True, text=True)  for line in result.stdout.split('\\n'): if self.session_name in line: return { \"name\": self.session_name, \"status\": \"Attached\" if \"Attached\" in line else \"Detached\", \"pid\": line.split('.')[0].strip() if '.' in line else \"Unknown\" }  return {\"name\": self.session_name, \"status\": \"Not Found\", \"pid\": \"N/A\"} except subprocess.CalledProcessError: return {\"name\": self.session_name, \"status\": \"Error\", \"pid\": \"N/A\"}  def kill_session(self) -> bool:",
        "category": "management",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "safe"
      },
      {
        "name": "main",
        "filename": "screen_agent_manager.py",
        "type": "method",
        "class": "ScreenAgentManager",
        "description": "",
        "category": "management",
        "usage_pattern": "main() # Usage pattern for main",
        "safety_level": "safe"
      }
    ]
  },
  {
    "name": "BasicTopology",
    "description": "class: BasicTopology",
    "type": "class",
    "category": "topology",
    "filename": "hybrid_topology_system.py",
    "class": null,
    "examples": [
      "BasicTopology() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "TopologyConfig",
    "description": "class: TopologyConfig",
    "type": "class",
    "category": "topology",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "TopologyConfig() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "__post_init__",
        "filename": "configuration_variables.py",
        "type": "method",
        "class": "TopologyConfig",
        "description": "# Topic Settings enable_topics: bool = True                 # Use topic-based communication default_topic: str = \"general\"            # Default topic for messages  # Predefined Topics standard_topics: Set[str] = None           # Standard topics available allow_custom_topics: bool = True           # Allow creation of new topics  # Topic Permissions topic_visibility: Dict[str, List[str]] = None      # topic -> agents who can see topic_participation: Dict[str, List[str]] = None   # topic -> agents who can participate  # Topic Behavior topic_isolation: bool = False              # Topics are completely isolated cross_topic_references: bool = True        # Allow references between topics  def __post_init__(self): if self.standard_topics is None: self.standard_topics = { \"general\", \"development\", \"design\", \"testing\", \"deployment\", \"planning\", \"support\", \"emergency\" }  # ============================================================================= # MASTER CONFIGURATION CLASS # =============================================================================  @dataclass class MasterConfig:",
        "category": "configuration",
        "usage_pattern": "__post_init__() # Usage pattern for __post_init__",
        "safety_level": "safe"
      }
    ]
  },
  {
    "name": "TopologyConfig",
    "description": "class: TopologyConfig",
    "type": "class",
    "category": "topology",
    "filename": "topology_specific_sessions.py",
    "class": null,
    "examples": [
      "TopologyConfig() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "__init__",
        "filename": "topology_specific_sessions.py",
        "type": "method",
        "class": "TopologyConfig",
        "description": "sessions = [] capture_patterns = {}  # Assign roles leader = self.agents[0] if self.agents else None lieutenants = self.agents[1:3] if len(self.agents) > 2 else self.agents[1:2] if len(self.agents) > 1 else [] workers = self.agents[3:] if len(self.agents) > 3 else []  # All agents still need sessions for agent in self.agents: sessions.extend([f\"{agent}_inbox\", f\"{agent}_outbox\"]) capture_patterns[agent] = [f\"{agent}_inbox\"]  roles = [] if leader: roles.append(f\"Leader: {leader}\") if lieutenants: roles.append(f\"Lieutenants: {', '.join(lieutenants)}\") if workers: roles.append(f\"Workers: {', '.join(workers)}\")  return TopologyConfig( name=\"Hierarchical\", description=\"Command structure: Leader -> Lieutenants -> Workers\", sessions_needed=sessions, capture_patterns=capture_patterns, communication_rules=[ \"Leader sends commands to Lieutenants\", \"Lieutenants distribute tasks to Workers\", \"Workers report back up the chain\", f\"Roles: {'; '.join(roles)}\" ], efficiency_rating=\"MEDIUM - Structured but limited paths\" )  def optimized_topology_for_use_case(self, use_case: str) -> TopologyConfig:",
        "category": "utilities",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "safe"
      },
      {
        "name": "compare_session_requirements",
        "filename": "topology_specific_sessions.py",
        "type": "method",
        "class": "TopologyConfig",
        "description": "print(\"SESSION REQUIREMENTS BY TOPOLOGY\") print(\"=\" * 50)  num_agents = 4 manager = TopologySessionManager(num_agents)  topologies = [ manager.linear_topology(), manager.ring_topology(), manager.star_topology(), manager.mesh_topology(), manager.hierarchical_topology() ]  for topology in topologies: print(f\"\\n{topology.name.upper()}\") print(\"-\" * len(topology.name)) print(f\"Description: {topology.description}\") print(f\"Total Sessions: {len(topology.sessions_needed)}\") print(f\"Efficiency: {topology.efficiency_rating}\")  print(f\"\\nSessions Required:\") for session in topology.sessions_needed: print(f\"  • {session}\")  print(f\"\\nCapture Patterns:\") for agent, sessions in topology.capture_patterns.items(): print(f\"  {agent} monitors: {', '.join(sessions)}\")  print(f\"\\nCommunication Rules:\") for rule in topology.communication_rules: print(f\"  • {rule}\")  def show_capture_optimization():",
        "category": "utilities",
        "usage_pattern": "compare_session_requirements() # Usage pattern for compare_session_requirements",
        "safety_level": "safe"
      },
      {
        "name": "demonstrate_dynamic_topology_switching",
        "filename": "topology_specific_sessions.py",
        "type": "method",
        "class": "TopologyConfig",
        "description": "",
        "category": "topology",
        "usage_pattern": "demonstrate_dynamic_topology_switching() # Usage pattern for demonstrate_dynamic_topology_switching",
        "safety_level": "safe"
      }
    ]
  },
  {
    "name": "TopologyLayer",
    "description": "class: TopologyLayer",
    "type": "class",
    "category": "topology",
    "filename": "hybrid_topology_system.py",
    "class": null,
    "examples": [
      "TopologyLayer() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "__init__",
        "filename": "hybrid_topology_system.py",
        "type": "method",
        "class": "TopologyLayer",
        "description": "# Main pipeline pipeline_agents = self.all_agents[1:]  # All except first pipeline = TopologyLayer( name=\"pipeline\", agents=pipeline_agents, internal_topology=BasicTopology.LINEAR )  # Supervisor oversees pipeline supervisor = TopologyLayer( name=\"supervisor\", agents=[self.all_agents[0]], internal_topology=BasicTopology.STAR )  return { \"topology_type\": \"Supervised Pipeline\", \"pipeline\": pipeline, \"supervisor\": supervisor, \"pattern\": \"Star supervision over linear pipeline\", \"description\": \"Supervisor monitors/controls linear processing pipeline\" }  def demonstrate_hybrid_topologies():",
        "category": "topology",
        "usage_pattern": "__init__() # Usage pattern for __init__",
        "safety_level": "moderate"
      },
      {
        "name": "show_topology_mathematics",
        "filename": "hybrid_topology_system.py",
        "type": "method",
        "class": "TopologyLayer",
        "description": "",
        "category": "topology",
        "usage_pattern": "show_topology_mathematics() # Usage pattern for show_topology_mathematics",
        "safety_level": "moderate"
      }
    ]
  },
  {
    "name": "TopologyType",
    "description": "class: TopologyType",
    "type": "class",
    "category": "topology",
    "filename": "configuration_variables.py",
    "class": null,
    "examples": [
      "TopologyType() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "show_timing_comparison",
    "description": "function: show_timing_comparison",
    "type": "function",
    "category": "triggers",
    "filename": "broadcast_trigger_demo.py",
    "class": null,
    "usage_pattern": "show_timing_comparison() # Usage pattern for show_timing_comparison",
    "examples": [
      "show_timing_comparison() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": []
  },
  {
    "name": "SessionCalculator",
    "description": "class: SessionCalculator",
    "type": "class",
    "category": "utilities",
    "filename": "session_calculator.py",
    "class": null,
    "examples": [
      "SessionCalculator() # Basic usage",
      "# Multi-agent system functionality"
    ],
    "alternatives": [],
    "requirements": [
      "Python 3.7+",
      "GNU Screen"
    ],
    "dependencies": [
      "subprocess",
      "threading",
      "json",
      "time"
    ],
    "safety_level": "safe",
    "complexity": "low",
    "methods": [
      {
        "name": "demo_different_configurations",
        "filename": "session_calculator.py",
        "type": "method",
        "class": "SessionCalculator",
        "description": "configurations = [ (2, True),   # 2 agents + user (2, False),  # 2 agents only (3, True),   # 3 agents + user (4, True),   # 4 agents + user (5, True),   # 5 agents + user ]  for num_agents, include_user in configurations: calc = SessionCalculator.visualize_network(num_agents, include_user)  print(f\"\\nCOMMAND TO CREATE ALL SESSIONS:\") print(\"-\" * 40) for session in calc['session_list']: print(f\"screen -dmS {session}\")  print(f\"\\nCOMMAND TO LIST SESSIONS:\") print(\"-\" * 40) print(\"screen -list\")  print(f\"\\nCOMMAND TO CLEANUP ALL SESSIONS:\") print(\"-\" * 40) for session in calc['session_list']: print(f\"screen -S {session} -X quit\")  input(\"\\nPress Enter to continue to next configuration...\")  def check_existing_sessions():",
        "category": "utilities",
        "usage_pattern": "demo_different_configurations() # Usage pattern for demo_different_configurations",
        "safety_level": "safe"
      },
      {
        "name": "create_test_sessions",
        "filename": "session_calculator.py",
        "type": "method",
        "class": "SessionCalculator",
        "description": "calc = SessionCalculator.calculate_sessions(num_agents, include_user)  print(f\"Creating {calc['total_sessions']} screen sessions...\")  success_count = 0 for session in calc['session_list']: try: subprocess.run(['screen', '-dmS', session], check=True) print(f\"✓ Created: {session}\") success_count += 1 except subprocess.CalledProcessError: print(f\"✗ Failed: {session}\")  print(f\"\\nCreated {success_count}/{calc['total_sessions']} sessions successfully\")  # Show current sessions print(\"\\nCurrent screen sessions:\") check_existing_sessions()  def cleanup_test_sessions(num_agents: int, include_user: bool = True):",
        "category": "utilities",
        "usage_pattern": "create_test_sessions() # Usage pattern for create_test_sessions",
        "safety_level": "moderate"
      }
    ]
  }
];

export const TOTAL_FUNCTIONALITIES = 101;
export const PYTHON_FILES_COUNT = 21;
export const CATEGORIES = ["agents","broadcasting","communication","configuration","dependencies","hierarchy","inbox","messaging","monitoring","permissions","roles","rules","screen","topology","triggers","utilities"];
export const TYPES = ["class","function","constant"];
