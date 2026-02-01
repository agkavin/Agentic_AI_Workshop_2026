"""
SOLUTION - Multi-Agent Exercise - Stock Agent

This is the complete, working solution for the stock agent.
Compare this with your implementation to see how you did!
"""

import adk
import random


# ============================================
# STOCK PRICE TOOL
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
        percentage change, and last update time. The data is formatted for easy reading.
    
    Examples:
        get_stock_price("AAPL") → Returns Apple stock information
        get_stock_price("GOOGL") → Returns Google stock information
    """
    # Mock implementation - generates realistic-looking stock data
    # In production, you'd call a real API like:
    # - Alpha Vantage API
    # - Yahoo Finance API
    # - Finnhub API
    # - IEX Cloud API
    
    ticker = ticker.upper()
    
    # Generate mock price data
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
Last Updated: 2026-02-01 23:25:11

Note: This is mock data for workshop purposes.
In production, this would fetch real-time data from a financial API.
"""


# ============================================
# STOCK AGENT CONFIGURATION
# ============================================

stock_agent = adk.Agent(
    # --------------------------------------------
    # INSTRUCTIONS
    # --------------------------------------------
    instructions="""
    You are a specialized stock market data agent with expertise in financial information.
    
    ### YOUR ROLE ###
    You are responsible for fetching and presenting stock market data. You are a specialist
    in financial information and stock prices.
    
    ### YOUR TOOL ###
    
    get_stock_price(ticker: str) -> str
    - Purpose: Fetches current stock prices and market data
    - When to use: Whenever users ask about stock prices, market data, or ticker information
    - Input format: Ticker symbols like "AAPL", "GOOGL", "MSFT"
    
    ### YOUR BEHAVIOR ###
    
    - Tone: Professional and knowledgeable about financial markets. Be clear and concise
      when presenting stock data.
    
    - Multiple stocks: When asked for multiple stocks, fetch each one separately using
      the get_stock_price tool and present them in an organized, easy-to-read format.
    
    - Unknown tickers: If someone asks for a company name instead of a ticker symbol,
      convert it to the standard ticker (e.g., "Apple" → "AAPL", "Google" → "GOOGL",
      "Microsoft" → "MSFT").
    
    - Data formatting: Always present stock information clearly with proper currency symbols,
      percentages, and alignment. Make it easy to scan and understand.
    
    ### EXAMPLE INTERACTIONS ###
    
    User: "What's the price of Apple stock?"
    You: [Use get_stock_price("AAPL")] → Present the formatted stock information professionally
    
    User: "Get me prices for AAPL, GOOGL, and MSFT"
    You: [Call get_stock_price three times] → Present all three stocks in a well-organized format
    
    Remember: You are a specialist. Focus on providing accurate, well-formatted
    stock market data. Leave other tasks (like visualization) to other agents.
    """,
    
    # Tools available to this agent
    tools=[get_stock_price],
    
    # Model configuration
    model="gemma-3-27b-it",
)


# ============================================
# NOTES
# ============================================
# Key points from this solution:
#
# 1. DETAILED TOOL DESCRIPTION: The get_stock_price tool has comprehensive
#    documentation including use cases, parameters, and examples.
#
# 2. SPECIALIST INSTRUCTIONS: The agent knows it's a stock market specialist
#    and focuses on that domain exclusively.
#
# 3. CLEAR BEHAVIOR: Instructions explain how to handle different scenarios
#    (single stock, multiple stocks, company names vs. tickers).
#
# 4. PROFESSIONAL TONE: The agent maintains a professional demeanor appropriate
#    for financial data.
#
# 5. MOCK DATA TRANSPARENCY: Both the tool and instructions acknowledge this
#    is mock data for learning purposes.
