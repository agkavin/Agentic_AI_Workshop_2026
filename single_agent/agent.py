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
            report = "\n".join([f"- {r['title']}: {r['href']}" for r in results])
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
    description="A helpful AI assistant with web search and time tools.",
    
    # --------------------------------------------
    # EXERCISE: Define the Agent's Behavior
    # --------------------------------------------
    instruction="""
    You are a helpful and knowledgeable AI assistant.
    
    ### YOUR TOOLS ###
    1. web_search(query: str): Use this for [FILL IN: when to use search?]
    2. get_current_time(): Use this for [FILL IN: when to use time?]
    
    ### YOUR PERSONALITY ###
    - [FILL IN: Describe your personality here (e.g., friendly, professional)]
    
    ### TOOL USAGE RULES ###
    - [FILL IN: Should you tell the user you are using a tool?]
    - [FILL IN: What should you do if a tool fails?]
    """,
    tools=[web_search, get_current_time],
)
