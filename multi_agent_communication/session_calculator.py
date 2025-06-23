#!/usr/bin/env python3
"""
Screen Session Calculator and Visualizer
Shows exactly how many screen sessions are created for different agent configurations
"""

import subprocess
from typing import List, Dict

class SessionCalculator:
    """Calculate and visualize screen sessions for different network sizes"""
    
    @staticmethod
    def calculate_sessions(num_agents: int, include_user: bool = True) -> Dict:
        """Calculate total sessions needed for a given network size"""
        
        # Each agent needs: 1 inbox + 1 outbox = 2 sessions per agent
        agent_sessions = num_agents * 2
        
        # User needs: 1 inbox + 1 outbox = 2 sessions (if included)
        user_sessions = 2 if include_user else 0
        
        total_sessions = agent_sessions + user_sessions
        
        return {
            'num_agents': num_agents,
            'include_user': include_user,
            'sessions_per_agent': 2,
            'agent_sessions': agent_sessions,
            'user_sessions': user_sessions,
            'total_sessions': total_sessions,
            'session_list': SessionCalculator._generate_session_list(num_agents, include_user)
        }
    
    @staticmethod
    def _generate_session_list(num_agents: int, include_user: bool) -> List[str]:
        """Generate the actual list of screen session names"""
        sessions = []
        
        # User sessions (if included)
        if include_user:
            sessions.extend(['user_inbox', 'user_outbox'])
        
        # Agent sessions
        for i in range(1, num_agents + 1):
            sessions.extend([f'agent{i}_inbox', f'agent{i}_outbox'])
        
        return sessions
    
    @staticmethod
    def visualize_network(num_agents: int, include_user: bool = True):
        """Create a visual representation of the network and its sessions"""
        
        calc = SessionCalculator.calculate_sessions(num_agents, include_user)
        
        print(f"\n{'='*60}")
        print(f"NETWORK CONFIGURATION: {num_agents} Agents" + (" + User" if include_user else ""))
        print(f"{'='*60}")
        
        print(f"\nTOTAL SCREEN SESSIONS NEEDED: {calc['total_sessions']}")
        print(f"  • Agent sessions: {calc['agent_sessions']} ({num_agents} agents × 2 sessions each)")
        if include_user:
            print(f"  • User sessions: {calc['user_sessions']} (1 user × 2 sessions)")
        
        print(f"\nSESSION BREAKDOWN:")
        print("-" * 30)
        
        if include_user:
            print("USER SESSIONS:")
            print("  • user_inbox    (receives messages)")
            print("  • user_outbox   (sent messages log)")
            print()
        
        print("AGENT SESSIONS:")
        for i in range(1, num_agents + 1):
            print(f"  Agent {i}:")
            print(f"    • agent{i}_inbox    (receives messages)")
            print(f"    • agent{i}_outbox   (sent messages log)")
        
        print(f"\nCOMMUNICATION CHANNELS:")
        print("-" * 30)
        
        # Calculate possible communication pairs
        total_nodes = num_agents + (1 if include_user else 0)
        possible_pairs = total_nodes * (total_nodes - 1)  # Directed pairs
        unique_pairs = possible_pairs // 2  # Undirected pairs
        
        print(f"  • Total nodes: {total_nodes}")
        print(f"  • Possible directed channels: {possible_pairs}")
        print(f"  • Unique bidirectional pairs: {unique_pairs}")
        
        # Show communication matrix
        nodes = []
        if include_user:
            nodes.append("User")
        nodes.extend([f"A{i}" for i in range(1, num_agents + 1)])
        
        print(f"\nCOMMUNICATION MATRIX:")
        print("-" * 30)
        print("     ", end="")
        for node in nodes:
            print(f"{node:>6}", end="")
        print()
        
        for i, sender in enumerate(nodes):
            print(f"{sender:>4} ", end="")
            for j, receiver in enumerate(nodes):
                if i == j:
                    print("   -  ", end="")  # Can't send to self
                else:
                    print("  <->", end="")   # Bidirectional
            print()
        
        return calc

def demo_different_configurations():
    """Demonstrate different network configurations"""
    
    configurations = [
        (2, True),   # 2 agents + user
        (2, False),  # 2 agents only
        (3, True),   # 3 agents + user
        (4, True),   # 4 agents + user
        (5, True),   # 5 agents + user
    ]
    
    for num_agents, include_user in configurations:
        calc = SessionCalculator.visualize_network(num_agents, include_user)
        
        print(f"\nCOMMAND TO CREATE ALL SESSIONS:")
        print("-" * 40)
        for session in calc['session_list']:
            print(f"screen -dmS {session}")
        
        print(f"\nCOMMAND TO LIST SESSIONS:")
        print("-" * 40)
        print("screen -list")
        
        print(f"\nCOMMAND TO CLEANUP ALL SESSIONS:")
        print("-" * 40)
        for session in calc['session_list']:
            print(f"screen -S {session} -X quit")
        
        input("\nPress Enter to continue to next configuration...")

def check_existing_sessions():
    """Check what screen sessions currently exist"""
    try:
        result = subprocess.run(['screen', '-list'], capture_output=True, text=True)
        print("EXISTING SCREEN SESSIONS:")
        print("-" * 30)
        if result.stdout.strip():
            print(result.stdout)
        else:
            print("No screen sessions currently running")
        return result.stdout
    except subprocess.CalledProcessError:
        print("Error checking screen sessions")
        return ""

def create_test_sessions(num_agents: int, include_user: bool = True):
    """Actually create the screen sessions for testing"""
    calc = SessionCalculator.calculate_sessions(num_agents, include_user)
    
    print(f"Creating {calc['total_sessions']} screen sessions...")
    
    success_count = 0
    for session in calc['session_list']:
        try:
            subprocess.run(['screen', '-dmS', session], check=True)
            print(f"✓ Created: {session}")
            success_count += 1
        except subprocess.CalledProcessError:
            print(f"✗ Failed: {session}")
    
    print(f"\nCreated {success_count}/{calc['total_sessions']} sessions successfully")
    
    # Show current sessions
    print("\nCurrent screen sessions:")
    check_existing_sessions()

def cleanup_test_sessions(num_agents: int, include_user: bool = True):
    """Clean up test sessions"""
    calc = SessionCalculator.calculate_sessions(num_agents, include_user)
    
    print(f"Cleaning up {calc['total_sessions']} screen sessions...")
    
    cleanup_count = 0
    for session in calc['session_list']:
        try:
            subprocess.run(['screen', '-S', session, '-X', 'quit'], check=True)
            print(f"✓ Removed: {session}")
            cleanup_count += 1
        except subprocess.CalledProcessError:
            print(f"✗ Failed to remove: {session}")
    
    print(f"\nCleaned up {cleanup_count}/{calc['total_sessions']} sessions")

if __name__ == "__main__":
    print("Screen Session Calculator for Multi-Agent Networks")
    print("=" * 55)
    
    while True:
        print("\nOptions:")
        print("1. Show network configurations")
        print("2. Check existing sessions")  
        print("3. Create test sessions")
        print("4. Cleanup test sessions")
        print("5. Quick calculation")
        print("0. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            demo_different_configurations()
        elif choice == "2":
            check_existing_sessions()
        elif choice == "3":
            num_agents = int(input("Number of agents: "))
            include_user = input("Include user? (y/n): ").lower().startswith('y')
            create_test_sessions(num_agents, include_user)
        elif choice == "4":
            num_agents = int(input("Number of agents to cleanup: "))
            include_user = input("Include user? (y/n): ").lower().startswith('y')
            cleanup_test_sessions(num_agents, include_user)
        elif choice == "5":
            num_agents = int(input("Number of agents: "))
            include_user = input("Include user? (y/n): ").lower().startswith('y')
            SessionCalculator.visualize_network(num_agents, include_user)
        elif choice == "0":
            break
        else:
            print("Invalid choice!")