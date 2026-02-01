"""
Multi-Agent Exercise - Stock Agent

This specialized sub-agent is responsible for fetching stock price data.
The tool is FULLY IMPLEMENTED with realistic mock data.
Your job is to complete the agent's instructions.
"""

import adk
import random


# ============================================
# STOCK PRICE TOOL (Fully Implemented)
# ============================================

@adk.tool
def get_stock_price(ticker: str) -> str:
    """
    Fetches the current stock price and related information for a given ticker symbol.
    
    Use this tool when you need to get stock market data for publicly traded companies.
    The ticker should be in standard format (e.g., "AAPL" for Apple, "GOOGL" for Google).
    
    This tool provides:
    - Current stock price
    - Price change (dollar amount and percentage)
    - Last update timestamp
    
    Args:
        ticker: The stock ticker symbol in uppercase format (e.g., "AAPL", "GOOGL", "MSFT").
                Common tickers include major tech companies, but any valid ticker works.
    
    Returns:
        A formatted string containing the stock symbol, current price, price change,
        percentage change, and last update time.
    
    Examples:
        get_stock_price("AAPL") → Returns Apple stock information
        get_stock_price("GOOGL") → Returns Google stock information
    """
    ticker = ticker.upper()
    
    # Mock price data for common stocks
    base_prices = {
        "AAPL": 180.50,
        "GOOGL": 142.30,
        "MSFT": 415.20,
        "AMZN": 175.80,
        "TSLA": 245.60,
        "META": 485.30,
        "NVDA": 722.15,
        "AMD": 165.40,
    }
    
    # Get base price or generate random one for unknown tickers
    base_price = base_prices.get(ticker, random.uniform(50, 500))
    
    # Add some random variation to simulate market movement
    current_price = round(base_price + random.uniform(-5, 5), 2)
    change = round(current_price - base_price, 2)
    change_percent = round((change / base_price) * 100, 2)
    
    # Format the response
    return f"""
Stock: {ticker}
Current Price: ${current_price}
Change: ${change} ({change_percent:+.2f}%)
Last Updated: 2026-02-02 00:06:23

Note: This is mock data for workshop purposes.
"""


# ============================================
# STOCK AGENT CONFIGURATION
# ============================================

stock_agent = adk.Agent(
    # --------------------------------------------
    # INSTRUCTIONS - FILL THIS IN!
    # --------------------------------------------
    instructions="""
    You are a specialized stock market data agent.
    
    ### YOUR ROLE ###
    [FILL IN: What is your primary responsibility? What makes you a specialist?]
    
    ### YOUR TOOL ###
    
    get_stock_price(ticker: str) -> str
    - Purpose: Fetches current stock prices and market data
    - When to use: [FILL IN: When should you use this tool?]
    - Input format: Ticker symbols like "AAPL", "GOOGL", "MSFT"
    
    ### YOUR BEHAVIOR ###
    
    - Tone: [FILL IN: Professional? Friendly? How should you communicate about financial data?]
    - Multiple stocks: [FILL IN: How do you handle requests for multiple stocks?]
    - Unknown tickers: [FILL IN: What do you do if someone asks for a company name instead of ticker?]
    - Data formatting: [FILL IN: How should you present stock information clearly?]
    
    ### EXAMPLE INTERACTIONS ###
    
    User: "What's the price of Apple stock?"
    You: [FILL IN: How would you respond?]
    
    User: "Get me prices for AAPL, GOOGL, and MSFT"
    You: [FILL IN: How would you handle multiple stocks?]
    """,
    
    # Tools (already configured!)
    tools=[get_stock_price],
    
    # Model configuration
    model="gemma-3-27b-it",
)
