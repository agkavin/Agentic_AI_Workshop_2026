# 🧠 Understanding Agentic AI - Single Agent

## What is an AI Agent?

An **AI Agent** is more than just a chatbot. While a simple LLM (Large Language Model) can only generate text, an agent can:

- 🤔 **Think** about what to do
- 🛠️ **Use tools** to perform actions
- 👀 **Observe** the results
- 🔄 **Iterate** until the task is complete

This makes agents capable of solving complex, multi-step problems autonomously.

---

## The ReAct Loop

The core of agentic behavior is the **ReAct loop** (Reasoning + Acting):

```
┌─────────────────────────────────────────┐
│  1. THOUGHT (Reasoning)                 │
│     "I need to find the current time"   │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  2. ACTION (Tool Call)                  │
│     Call: get_current_time()            │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  3. OBSERVATION (Tool Result)           │
│     "2026-02-01 23:25:11"               │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  4. THOUGHT (Reasoning)                 │
│     "I have the time, I can respond"    │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  5. FINAL RESPONSE                      │
│     "It's currently 11:25 PM on Feb 1"  │
└─────────────────────────────────────────┘
```

This loop continues until the agent has enough information to answer the user's question.

---

## AI Agent vs. Simple LLM

| Feature | Simple LLM | AI Agent |
|---------|-----------|----------|
| **Knowledge** | Only training data (static) | Training data + real-time tools |
| **Actions** | Generate text only | Call functions, APIs, search web |
| **Problem Solving** | Single-step responses | Multi-step reasoning |
| **Accuracy** | Can hallucinate facts | Can verify with tools |
| **Example** | "I don't know the current time" | Calls `get_current_time()` tool |

---

## How Tools Extend Agent Capabilities

**Without tools:**
```
User: "What time is it?"
Agent: "I don't have access to real-time information."
```

**With tools:**
```
User: "What time is it?"
Agent: [THOUGHT] I need to get the current time
      [ACTION] Call get_current_time()
      [OBSERVATION] "2026-02-01 23:25:11"
      [RESPONSE] "It's currently 11:25 PM on February 1st, 2026."
```

---

## The Role of System Prompts (Instructions)

The **instructions** (also called system prompt) define:

1. **Identity**: Who is the agent?
   - "You are a helpful research assistant..."

2. **Capabilities**: What can it do?
   - "You have access to web search and time tools..."

3. **Behavior**: How should it act?
   - "Be concise and cite sources..."

4. **Tool Usage Guidelines**: When to use each tool?
   - "Use web_search for current events..."

**Good instructions = Better agent behavior!**

---

## Tool Descriptions Matter

When you write a tool's docstring, the agent uses it to decide **when** to call that tool.

**Poor description:**
```python
@adk.tool
def web_search(query: str) -> str:
    """Searches the web."""
    ...
```

**Good description:**
```python
@adk.tool
def web_search(query: str) -> str:
    """
    Searches the internet for current information about a given topic.
    Use this when you need up-to-date information, news, or facts that
    you don't have in your training data.
    
    Args:
        query: The search query (e.g., "latest AI news", "weather in Paris")
    
    Returns:
        Search results as a formatted string
    """
    ...
```

The agent reads these descriptions and uses them to make intelligent decisions!

---

## Your Exercise

In this exercise, you'll:

1. ✅ **Complete tool descriptions** in `tools.py`
   - Help the agent understand when to use each tool

2. ✅ **Implement `get_current_time()`** in `tools.py`
   - Give the agent the ability to know the current time

3. ✅ **Write agent instructions** in `agent.py`
   - Define the agent's personality and behavior

4. ✅ **Register tools** in `agent.py`
   - Connect the tools to the agent

5. ✅ **Test in the Web UI**
   - See the ReAct loop in action!

---

## Testing Your Agent

Once you've completed the code, run:

```bash
cd single_agent
adk web-port 8000
```

Try these prompts:

- ✅ "What time is it?" → Should use `get_current_time()`
- ✅ "Search for the latest AI news" → Should use `web_search()`
- ✅ "What's the current time and latest news about AI?" → Should use both tools!

Watch the Web UI to see the ReAct loop in action. You'll see:
- The agent's thoughts
- Which tools it calls
- The tool results
- The final response

---

## Key Takeaways

1. 🧠 **Agents think, act, and observe** in a loop (ReAct)
2. 🛠️ **Tools extend capabilities** beyond text generation
3. 📝 **Good descriptions** help agents make smart decisions
4. 🎯 **Instructions define behavior** and personality
5. 🔄 **The loop continues** until the task is complete

---

**Next:** Once you've mastered single agents, move on to `multi_agent/` to learn about orchestration and specialization! 🚀
