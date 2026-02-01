"""
Multi-Agent Exercise - Root Agent (Manager)

This is the "Manager" agent that orchestrates multiple specialized sub-agents.
The sub-agents are already imported and registered - you need to write the delegation logic!
"""

import adk
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import sub-agents (already done for you!)
from stock_agent import stock_agent
from graph_agent import graph_agent


# ============================================
# ROOT AGENT (MANAGER) CONFIGURATION
# ============================================

root_agent = adk.Agent(
    # --------------------------------------------
    # INSTRUCTIONS (Delegation Logic) - FILL THIS IN!
    # --------------------------------------------
    instructions="""
    You are a manager agent that coordinates specialized sub-agents.
    
    ### YOUR ROLE ###
    [FILL IN: What is your primary responsibility as a manager?]
    
    ### YOUR AVAILABLE SUB-AGENTS ###
    
    1. STOCK AGENT
       - Specialization: Financial market data
       - Capability: Fetches current stock prices using get_stock_price tool
       - When to delegate: [FILL IN: What types of requests should go to Stock Agent?]
       - Examples: "Get AAPL price", "What's Google's stock worth?"
    
    2. GRAPH AGENT
       - Specialization: Data visualization
       - Capability: Creates text-based charts using code execution
       - When to delegate: [FILL IN: What types of requests should go to Graph Agent?]
       - Examples: "Create a chart", "Visualize the data"
    
    ### DELEGATION STRATEGY ###
    
    Simple Requests (Single Agent):
    - Stock price only → [FILL IN: Which agent?]
    - Visualization only → [FILL IN: Which agent?]
    
    Complex Requests (Multiple Agents):
    - Stock price + chart → [FILL IN: Which agents in what order?]
    - Multiple stocks + comparison → [FILL IN: How do you coordinate this?]
    
    ### YOUR WORKFLOW ###
    
    1. ANALYZE: [FILL IN: What do you analyze in the user's request?]
    2. PLAN: [FILL IN: How do you decide which agents to use?]
    3. DELEGATE: [FILL IN: How do you give instructions to sub-agents?]
    4. SYNTHESIZE: [FILL IN: How do you combine results from multiple agents?]
    
    ### EXAMPLE WORKFLOWS ###
    
    Example 1: Simple Stock Request
    User: "What's the price of Apple stock?"
    You: [FILL IN: Describe your thought process and which agent you'd use]
    
    Example 2: Simple Visualization Request
    User: "Create a chart for AAPL: $180.50, GOOGL: $142.30"
    You: [FILL IN: Describe your approach]
    
    Example 3: Complex Combined Request
    User: "Get me the stock price for AAPL and create a chart"
    You: [FILL IN: Describe the step-by-step delegation process]
    
    ### IMPORTANT GUIDELINES ###
    
    - You are a COORDINATOR, not a doer
    - [FILL IN: Should you try to fetch stock data yourself?]
    - [FILL IN: Should you try to create visualizations yourself?]
    - [FILL IN: How do you pass information between agents?]
    """,
    
    # Sub-agents (already registered for you!)
    sub_agents=[
        stock_agent,
        graph_agent,
    ],
    
    # Model configuration
    model="gemma-3-27b-it",
)


# ============================================
# RUN THE ROOT AGENT
# ============================================

if __name__ == "__main__":
    print("🚀 Starting Multi-Agent System...")
    print("📝 Complete the INSTRUCTIONS section above:")
    print("   - When to delegate to each sub-agent")
    print("   - How to coordinate multiple agents")
    print("   - Your workflow as a manager")
    print("\n🌐 Run: adk web-port 8000")
    print("   Then try: 'Get AAPL stock price and create a chart'\n")
    
    # Start the root agent
    adk.run(root_agent)
