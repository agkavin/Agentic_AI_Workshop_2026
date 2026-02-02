from datetime import datetime
from ddgs import DDGS
from google.adk.agents import Agent
from dotenv import load_dotenv

load_dotenv()

def web_search(query: str) -> dict:
    """
    Finds current information on the web via DuckDuckGo.
    Use this for news, facts, or real-time data from the internet.

    Args:
        query (str): The search keywords (e.g., 'latest AI breakthroughs').

    Returns:
        dict: A success status with a 'report' of results or an 'error'.
    """
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)
            report = "\n".join([f"- {r['title']} ({r['href']}): {r['body']}" for r in results])
            return {"status": "success", "report": report}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

def get_current_time() -> dict:
    """
    Retrieves the system's current date and time.
    Use this whenever a user asks 'what time is it' or 'what is today's date'.

    Returns:
        dict: A success status with a formatted 'report' of the date/time.
    """
    return {"status": "success", "report": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

root_agent = Agent(
    name="single_agent",
    model="gemma-3-27b-it",
    description="A comprehensive assistant capable of searching the web and providing current time/date information.",
    instruction="""
    You are a friendly and professional AI assistant.
    
    ### CORE BEHAVIOR ###
    - GREETINGS: If the user greets you (e.g., 'Hello', 'Hi'), always greet them back warmly and ask how you can help.
    - HELPFULNESS: Provide concise and accurate answers using your tools when necessary.
    - CLARITY: Explain when you are using a tool to find information.
    
    ### TOOLS ###
    - web_search: 
       - Usage: Use for finding current news, facts, or any real-time data from the internet.
       - Schema: Accepts a string 'query' and returns detailed search results.
    - get_current_time: 
       - Usage: Use specifically when the user asks for the current time or date.
       - Schema: Takes no arguments and returns the formatted system time.
    """,
    tools=[web_search, get_current_time],
)
