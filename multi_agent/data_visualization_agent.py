from google.adk.agents import Agent

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
            return {"status": "error", "error_message": "No data provided for visualization."}
        
        max_val = max(data.values())
        chart = "--- Data Visualization ---\n\n"
        
        for key, value in data.items():
            # Scale the bar length (max 20 characters)
            bar_length = int((value / max_val) * 20) if max_val > 0 else 0
            bar = "█" * bar_length
            chart += f"{key.ljust(10)} | {bar} ({value})\n"
            
        return {"status": "success", "report": chart}
    except Exception as e:
        return {"status": "error", "error_message": f"Visualization error: {str(e)}"}

data_visualization_agent = Agent(
    name="data_visualization_agent",
    model="gemma-3-27b-it",
    description="A specialist agent that creates text-based visualizations.",
    
    # --------------------------------------------
    # EXERCISE: Define the Data Visualization Agent's Behavior
    # --------------------------------------------
    instruction="""
    You are a data visualization specialist.
    
    ### YOUR GOAL ###
    Create clear and readable text-based visualizations using ASCII characters.
    
    ### YOUR TOOL ###
    generate_bar_chart(data: dict): 
       - Usage: Use this to generate a text-based bar chart.
       - Schema: Accepts a dictionary 'data' where keys are labels (str) and values are numbers (float/int).
    
    ### YOUR BEHAVIOR ###
    - [FILL IN: How should you describe the chart to the user?]
    - [FILL IN: What should you do if the data is incomplete?]
    """,
    tools=[generate_bar_chart],
)
