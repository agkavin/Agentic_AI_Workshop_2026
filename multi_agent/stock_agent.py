import random
from google.adk.agents import Agent

def get_stock_price(ticker: str) -> dict:
    """
    Fetches the current trading price for a specific stock ticker.
    Use this when a user asks for the price of a stock (e.g., 'What is Google's price?').

    Args:
        ticker (str): The stock symbol (e.g., 'AAPL', 'GOOGL').

    Returns:
        dict: A success status with the 'report' containing the current price.
    """
    price = round(next(iter(random.sample(range(100, 500), 1))) + random.random(), 2)
    return {"status": "success", "report": f"{ticker.upper()}: ${price}"}

stock_agent = Agent(
    name="stock_agent",
    model="gemma-3-27b-it",
    description="A specialized agent that fetches stock market data.",
    
    # --------------------------------------------
    # EXERCISE: Define the Stock Agent's Behavior
    # --------------------------------------------
    instruction="""
    You are a stock market expert.
    
    ### YOUR TOOL ###
    get_stock_price(ticker: str): Use this to [FILL IN: when to fetch prices?]
    
    ### YOUR PERSONA ###
    - [FILL IN: How should you talk about stocks? (e.g., professional, analytical)]
    
    ### HANDLING DATA ###
    - [FILL IN: What should you do if the ticker is missing?]
    - [FILL IN: How should you format the price report?]
    """,
    tools=[get_stock_price],
)
