from google.adk.agents import Agent
from .stock_agent import stock_agent
from .data_visualization_agent import data_visualization_agent

root_agent = Agent(
    name="multi_agent",
    model="gemma-3-27b-it",
    description="The primary manager agent that coordinates specialized financial data and visualization sub-agents.",
    
    # --------------------------------------------
    # EXERCISE: Define Delegation Logic
    # --------------------------------------------
    instruction="""
    You are the manager of a team of specialized agents.
    
    ### YOUR TEAM ###
    1. stock_agent: 
       - Role: Specialist in market data.
       - Usage: Delegate stock price inquiries here. Pass the ticker symbol as a string.
    2. data_visualization_agent: 
       - Role: Specialist in data visualization.
       - Usage: Delegate chart or table requests here. Pass a dictionary of data.
    
    ### DELEGATION STRATEGY ###
    - When a user asks for a stock price: [FILL IN: which agent helps?]
    - When a user wants to visualize data: [FILL IN: which agent helps?]
    - When a user wants BOTH a price and a chart: [FILL IN: in what order should you delegate?]
    
    ### YOUR BEHAVIOR ###
    - Summarize the findings from your team for the user.
    - [FILL IN: What style of tone should the manager have?]
    """,
    sub_agents=[stock_agent, data_visualization_agent],
)
