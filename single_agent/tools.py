"""
Single Agent Exercise - Custom Tools

In this file, you'll work with two pre-defined tools that extend your agent's capabilities:
1. web_search: Search the internet using DuckDuckGo
2. get_current_time: Get the current date and time

These tools are FULLY IMPLEMENTED and ready to use. Your job is to understand how they work
and then configure the agent to use them effectively in agent.py.
"""

import adk
from datetime import datetime
from duckduckgo_search import DDGS


# ============================================
# TOOL 1: Web Search (DuckDuckGo)
# ============================================

@adk.tool
def web_search(query: str) -> str:
    """
    Searches the internet for current information about a given topic using DuckDuckGo.
    Use this when you need up-to-date information, news, or facts that you don't have 
    in your training data.
    
    This tool is particularly useful for:
    - Current events and breaking news
    - Recent developments in technology, science, or business
    - Real-time information that changes frequently
    - Fact-checking and verification
    
    Args:
        query: The search query string (e.g., "latest AI news", "weather in Paris",
               "stock market trends"). Be specific for better results.
    
    Returns:
        A formatted string containing the top 5 search results with titles, URLs,
        and brief descriptions.
    """
    try:
        with DDGS() as ddgs:
            # Perform search and get top 5 results
            results = list(ddgs.text(query, max_results=5))
            
            if not results:
                return f"No results found for: {query}"
            
            # Format the results nicely
            formatted_results = f"Search results for: {query}\n\n"
            for i, result in enumerate(results, 1):
                title = result.get('title', 'No title')
                url = result.get('href', 'No URL')
                snippet = result.get('body', 'No description')
                
                formatted_results += f"{i}. {title}\n"
                formatted_results += f"   URL: {url}\n"
                formatted_results += f"   {snippet}\n\n"
            
            return formatted_results
            
    except Exception as e:
        return f"Error performing search: {str(e)}\nPlease try a different query."


# ============================================
# TOOL 2: Get Current Time
# ============================================

@adk.tool
def get_current_time() -> str:
    """
    Gets the current date and time.
    Use this when you need to know what time it is right now, what day it is,
    or to perform time-based calculations.
    
    This tool is useful for:
    - Answering "what time is it?" questions
    - Determining the current date
    - Time-sensitive operations
    - Scheduling and time calculations
    
    Returns:
        A formatted string with the current date and time in a human-readable format,
        including the day of the week.
    """
    # Get the current date and time
    now = datetime.now()
    
    # Format it as a readable string
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Also include day of week for context
    day_of_week = now.strftime("%A")
    
    return f"Current date and time: {formatted_time} ({day_of_week})"


# ============================================
# TOOL SUMMARY
# ============================================
# These tools are complete and ready to use!
# 
# Next steps:
# 1. Go to agent.py
# 2. Look at how these tools are imported
# 3. Complete the agent's instructions (system prompt)
# 4. The tools are already registered - just focus on the prompt!
