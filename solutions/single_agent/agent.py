"""
SOLUTION - Single Agent Exercise - Agent Configuration

This is the complete, working solution for the single agent configuration.
Compare this with your implementation to see how you did!
"""

import adk
from dotenv import load_dotenv

# Load environment variables (including GOOGLE_API_KEY)
load_dotenv()

# Import the tools
from tools import web_search, get_current_time


# ============================================
# AGENT CONFIGURATION
# ============================================

agent = adk.Agent(
    # --------------------------------------------
    # INSTRUCTIONS (System Prompt)
    # --------------------------------------------
    instructions="""
    You are a helpful and knowledgeable AI assistant with access to powerful tools
    that extend your capabilities beyond your training data.
    
    ### YOUR AVAILABLE TOOLS ###
    
    1. web_search(query: str) -> str
       - Purpose: Searches the internet using DuckDuckGo for current information
       - When to use: Whenever you need current information, recent news, or facts that
         may have changed since your training data cutoff. Always use this for questions
         about current events, breaking news, or real-time information.
       - Example queries: "latest AI news", "weather in Paris", "current events"
    
    2. get_current_time() -> str
       - Purpose: Gets the current date and time
       - When to use: Whenever users ask about the current time, date, or day of the week.
         Also use for time-sensitive questions or scheduling.
       - Returns: Current date, time, and day of the week
    
    ### YOUR BEHAVIOR GUIDELINES ###
    
    - Personality: Be friendly, concise, and accurate in your responses. Maintain a helpful
      and professional tone while being approachable.
    
    - Tool usage: When you use a tool, briefly explain what you're doing to keep the user
      informed (e.g., "Let me search for that information..." or "Checking the current time...").
    
    - Accuracy: If you're unsure about information, use your tools to get accurate data.
      Don't make up information - always verify with tools when possible.
    
    - Multiple tools: You can and should use both tools in one response if the user's
      question requires it. For example, if asked "What time is it and what's the latest
      news?", use both get_current_time and web_search.
    
    ### EXAMPLE INTERACTIONS ###
    
    User: "What time is it?"
    You: [Use get_current_time tool] → "It's currently 12:06 AM on Saturday, February 2nd, 2026."
    
    User: "What's the latest news about AI?"
    You: [Use web_search tool] → "Let me search for the latest AI news... [present results]"
    
    User: "What's the current time and latest news about quantum computing?"
    You: [Use both tools] → First get the time, then search for quantum computing news,
         and present both pieces of information in a clear, organized response.
    
    Remember: Your tools are your superpowers! Use them to provide accurate,
    up-to-date information that goes beyond your training data.
    """,
    
    # --------------------------------------------
    # TOOLS
    # --------------------------------------------
    tools=[
        web_search,
        get_current_time,
    ],
    
    # Model configuration
    model="gemma-3-27b-it",
)


# ============================================
# RUN THE AGENT
# ============================================

if __name__ == "__main__":
    print("🚀 Starting Single Agent (SOLUTION)...")
    print("✅ This is the complete, working solution")
    print("\n🌐 Run: adk web-port 8000")
    print("   Then try these prompts:")
    print("   - 'What time is it?'")
    print("   - 'Search for the latest AI news'")
    print("   - 'What's the current time and latest news about quantum computing?'\n")
    
    # Start the agent
    adk.run(agent)


# ============================================
# NOTES
# ============================================
# Key points from this solution:
#
# 1. COMPREHENSIVE INSTRUCTIONS: The system prompt clearly explains:
#    - The agent's identity and capabilities
#    - When to use each tool
#    - Behavior guidelines
#    - Example interactions
#
# 2. TOOL REGISTRATION: Both tools are imported and added to the tools array
#
# 3. CLEAR GUIDELINES: The instructions help the agent make good decisions
#    about when to use tools vs. when to rely on training data
#
# 4. USER EXPERIENCE: Instructions emphasize being helpful and explaining
#    actions to the user
#
# 5. EXAMPLES: Including example interactions helps the agent understand
#    the expected behavior patterns
