"""
Single Agent Exercise - Agent Configuration

In this file, you'll configure your first AI agent by completing the INSTRUCTIONS (system prompt).
The tools are already imported and registered - you just need to write the prompt that tells
the agent how to behave and when to use each tool.
"""

import adk
from dotenv import load_dotenv

# Load environment variables (including GOOGLE_API_KEY)
load_dotenv()

# Import the tools (already done for you!)
from tools import web_search, get_current_time


# ============================================
# AGENT CONFIGURATION
# ============================================

agent = adk.Agent(
    # --------------------------------------------
    # INSTRUCTIONS (System Prompt) - FILL THIS IN!
    # --------------------------------------------
    # This is where you define the agent's personality, role, and behavior.
    # Good instructions make the difference between a helpful and unhelpful agent!
    
    instructions="""
    You are a helpful and knowledgeable AI assistant with access to powerful tools.
    
    ### YOUR AVAILABLE TOOLS ###
    
    1. web_search(query: str) -> str
       - Purpose: Searches the internet using DuckDuckGo for current information
       - When to use: [FILL IN: When should the agent use this tool?]
       - Example queries: "latest AI news", "weather in Paris", "current events"
    
    2. get_current_time() -> str
       - Purpose: Gets the current date and time
       - When to use: [FILL IN: When should the agent use this tool?]
       - Returns: Current date, time, and day of the week
    
    ### YOUR BEHAVIOR GUIDELINES ###
    
    - Personality: [FILL IN: How should the agent behave? Friendly? Professional? Concise?]
    - Tool usage: [FILL IN: Should you explain when you're using a tool?]
    - Accuracy: [FILL IN: What should you do if you're unsure about information?]
    - Multiple tools: [FILL IN: Can you use both tools in one response if needed?]
    
    ### EXAMPLE INTERACTIONS ###
    
    User: "What time is it?"
    You: [FILL IN: Describe how you would respond]
    
    User: "What's the latest news about AI?"
    You: [FILL IN: Describe how you would respond]
    
    User: "What's the current time and latest news about quantum computing?"
    You: [FILL IN: Describe how you would respond - hint: use both tools!]
    """,
    
    # --------------------------------------------
    # TOOLS (Already configured for you!)
    # --------------------------------------------
    tools=[
        web_search,
        get_current_time,
    ],
    
    # Model configuration (using Gemma 3)
    model="gemma-3-27b-it",
)


# ============================================
# RUN THE AGENT
# ============================================

if __name__ == "__main__":
    print("🚀 Starting Single Agent...")
    print("📝 Complete the INSTRUCTIONS section above:")
    print("   - When to use each tool")
    print("   - Behavior guidelines")
    print("   - Example interactions")
    print("\n🌐 Run: adk web-port 8000")
    print("   Then open the Web UI to chat with your agent!\n")
    
    # Start the agent
    adk.run(agent)
