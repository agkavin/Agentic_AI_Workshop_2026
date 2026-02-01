# 🤖 Introduction to Agentic AI Workshop

Welcome to the **Agentic AI Workshop**! In this hands-on 1.5-hour session, you'll learn how to build intelligent AI agents using the **Google ADK (Agent Development Kit)** framework.

## 🎯 Learning Objectives

By the end of this workshop, you will:

- ✅ Understand what makes an AI "agentic" (vs. simple LLM calls)
- ✅ Build a single-agent system with custom tools
- ✅ Create a multi-agent orchestration with specialized sub-agents
- ✅ Learn the ReAct loop (Thought → Action → Observation)
- ✅ Deploy and test agents using the ADK Web UI

---

## 🚀 Quick Start with GitHub Codespaces

### Step 1: Open in Codespaces

1. **Fork this repository** to your GitHub account
2. Click the green **"Code"** button
3. Select **"Codespaces"** tab
4. Click **"Create codespace on main"**

GitHub will automatically:
- ✨ Set up a Python 3.11 environment
- ✨ Install `google-adk` and dependencies
- ✨ Configure port forwarding for the Web UI

**Wait for the setup to complete** (you'll see "✅ Environment ready!" in the terminal).

---

### Step 2: Get Your Google API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy your API key

---

### Step 3: Configure Your Environment

1. Open the `.env` file in the root directory
2. Replace `your_key_here` with your actual API key:
   ```
   GOOGLE_API_KEY=AIzaSy...your_actual_key
   ```
3. Save the file (Ctrl+S / Cmd+S)

---

### Step 4: Launch the ADK Web UI

Run this command in the terminal:

```bash
adk web-port 8000
```

You should see:
- 🌐 A pop-up notification to open the Web UI
- 🔗 Click **"Open in Browser"** to access the dashboard

The Web UI allows you to:
- Chat with your agents
- See tool calls in real-time
- Debug the ReAct loop
- Test multi-agent orchestration

---

## 📚 Workshop Structure

### Exercise 1: Single Agent (30 minutes)

**Location:** `single_agent/`

**What you'll build:**
- A conversational agent with two custom tools:
  - `web_search`: Search the internet for information
  - `get_current_time`: Get the current date and time

**Files to complete:**
- `tools.py`: Define tool functions with proper descriptions
- `agent.py`: Configure the agent with instructions and tools

**Learning resource:**
- Read `single_agent/LEARN.md` to understand the ReAct loop

**Testing:**
Navigate to the `single_agent/` directory and run:
```bash
cd single_agent
adk web-port 8000
```

Try asking:
- "What time is it?"
- "Search for the latest news about AI agents"

---

### Exercise 2: Multi-Agent Orchestration (45 minutes)

**Location:** `multi_agent/`

**What you'll build:**
- A **Manager Agent** that delegates tasks to specialized sub-agents:
  - **Stock Agent**: Fetches stock price data (mocked)
  - **Graph Agent**: Generates text-based visualizations

**Files to complete:**
- `root_agent.py`: Configure the manager with delegation logic
- `stock_agent.py`: Complete the stock data agent
- `graph_agent.py`: Complete the visualization agent

**Learning resource:**
- Read `multi_agent/LEARN.md` to understand multi-agent patterns

**Testing:**
Navigate to the `multi_agent/` directory and run:
```bash
cd multi_agent
adk web-port 8000
```

Try asking:
- "Get me the stock price for AAPL and create a chart"
- "What's the current price of GOOGL?"

---

## 💡 Solutions

Stuck? Check the `solutions/` directory for complete, working implementations:

- `solutions/single_agent/`: Fully functional single-agent code
- `solutions/multi_agent/`: Complete multi-agent orchestration

**Tip:** Try to complete the exercises on your own first! The solutions are there to help you learn, not to copy-paste.

---

## 🛠️ Troubleshooting

### "Module not found: google-adk"
Run: `pip install -r requirements.txt`

### "API key not found"
Make sure you've set `GOOGLE_API_KEY` in the `.env` file

### Port 8000 already in use
Stop any running ADK processes with Ctrl+C, then try again

### Web UI not opening
Check the "PORTS" tab in VS Code and click the globe icon next to port 8000

---

## 📖 Additional Resources

- [Google ADK Documentation](https://google.github.io/adk/)
- [Agentic AI Concepts](https://www.anthropic.com/research/building-effective-agents)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

---

## 🎓 Workshop Flow

1. **Introduction (10 min)**: What is Agentic AI?
2. **Exercise 1 (30 min)**: Build a single agent with tools
3. **Exercise 2 (45 min)**: Create multi-agent orchestration
4. **Wrap-up (5 min)**: Next steps and resources

---

## 🤝 Contributing

Found a bug or have suggestions? Feel free to open an issue or submit a pull request!

---

## 📝 License

This workshop is provided for educational purposes. Feel free to use and modify for your learning!

---

**Happy coding! 🚀**
