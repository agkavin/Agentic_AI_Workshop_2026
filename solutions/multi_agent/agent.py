from google.adk.agents import Agent
import random

def get_stock_price(ticker: str) -> dict:
    """
    Fetches the current trading price for a specific stock ticker.
    Use this when a user asks for the price of a stock (e.g., 'What is Google's price?').

    Args:
        ticker (str): The stock symbol (e.g., 'AAPL', 'GOOGL').

    Returns:
        dict: A success status with the 'report' containing the current price.
    """
    ticker = ticker.upper()
    price = round(random.uniform(50, 500), 2)
    return {"status": "success", "report": f"Current price of {ticker} is ${price}"}

def generate_bar_chart(data: dict) -> dict:
    """
    Creates a text-based ASCII bar chart comparing different categories.
    Use this to visualize numerical data trends or comparisons (e.g., stock price history).

    Args:
        data (dict): A dictionary mapping labels (str) to values (float/int).
                    Example: {'AAPL': 180, 'MSFT': 420}

    Returns:
        dict: A success status with the 'report' containing the ASCII chart.
    """
    try:
        if not data:
            return {"status": "error", "error_message": "No data for visualization."}
        max_val = max(data.values())
        chart = "\n--- Data Visualization ---\n"
        for key, value in data.items():
            bar = "█" * int((value / max_val) * 20) if max_val > 0 else 0
            chart += f"{key.ljust(10)} | {bar} ({value})\n"
        return {"status": "success", "report": chart}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

stock_agent = Agent(
    name="stock_agent",
    model="gemma-3-27b-it",
    description="A specialist agent that fetches real-time stock market data.",
    instruction="""
    You are a focused and analytical stock market specialist.
    
    ### CORE BEHAVIOR ###
    - GREETINGS: If specifically addressed with a greeting, respond politely before providing data.
    - PRECISION: Always use the 'get_stock_price' tool for any stock price inquiry.
    
    ### TOOL USAGE ###
    get_stock_price(ticker: str):
       - Usage: Fetches the current mock trading price of a stock.
       - Schema: Accepts a ticker (str) like 'AAPL' or 'TSLA'.
    """,
    tools=[get_stock_price],
)

data_visualization_agent = Agent(
    name="data_visualization_agent",
    model="gemma-3-27b-it",
    description="A specialist agent that creates text-based visualizations for data analysis.",
    instruction="""
    You are a creative data visualization specialist.
    
    ### CORE BEHAVIOR ###
    - GREETINGS: If specifically addressed with a greeting, respond politely.
    - VISUALIZATION: Use the 'generate_bar_chart' tool to create clear ASCII charts from data.
    
    ### TOOL USAGE ###
    generate_bar_chart(data: dict):
       - Usage: Transforms a dictionary of categories and values into a bar chart.
       - Schema: Accepts a dictionary where keys are category labels and values are numerical.
    """,
    tools=[generate_bar_chart],
)

root_agent = Agent(
    name="multi_agent",
    model="gemma-3-27b-it",
    description="The primary manager agent that coordinates financial data and visualization specialists.",
    instruction="""
    You are the manager and main point of contact for this multi-agent team.
    
    ### CORE BEHAVIOR ###
    - GREETINGS: Always greet the user back if they say hello or hi. Be welcoming!
    - COORDINATION: Delegate specialized tasks to your team members and summarize their results for the user.
    
    ### TEAM USAGE ###
    - stock_agent: Specialist for fetching current stock prices. Input: ticker (str).
    - data_visualization_agent: Specialist for creating ASCII charts. Input: data (dict).
    """,
    sub_agents=[stock_agent, data_visualization_agent],
)
