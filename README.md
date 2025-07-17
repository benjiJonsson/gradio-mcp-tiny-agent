---
title: Mcp Client
emoji: 🦀
colorFrom: red
colorTo: red
sdk: gradio
sdk_version: 5.37.0
app_file: app.py
pinned: false
---

# MCP Client with Gradio and Tiny Agents

This project demonstrates building Model Context Protocol (MCP) clients using Gradio and Tiny Agents. It shows how to create AI applications that can connect to multiple tool providers through a standardized interface.

## What you can do

- Use a web interface to interact with MCP tools
- Run a command-line agent with JSON configuration
- Create Python agents programmatically
- Access tools like prime factorization and image processing

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Set your Hugging Face token:
```bash
export HF_TOKEN=your_token_here
```

## Usage

### Web Interface (Gradio)

```bash
python app.py
```

Opens a web interface at http://localhost:7860 where you can chat with the agent and use MCP tools.

### Command Line Agent

```bash
cd my-agent
tiny-agents run agent.json
```

Interactive command-line interface. Try asking:
- "Prime factorization of 68"
- "What are the prime factors of 42?"

### Python Agent

```python
from huggingface_hub import Agent
from huggingface_hub.inference._mcp.mcp_client import StdioServerConfig

agent = Agent(
    model="Qwen/Qwen2.5-72B-Instruct",
    provider="nebius",
    servers=[
        StdioServerConfig(
            command="npx",
            args=[
                "mcp-remote",
                "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse"
            ]
        )
    ],
)
```

Test with:
```bash
python test_python_agent.py
```

## Available Tools

The MCP server provides:
- Prime factorization
- Image generation (cheetah images)
- Image orientation detection
- Sepia filter application

## Files

- `app.py` - Gradio web interface
- `my-agent/agent.json` - Tiny agent configuration
- `tiny_agent_python.py` - Python agent for local server
- `tiny_agent_deployed.py` - Python agent for deployed server
- `test_python_agent.py` - Test script
- `requirements.txt` - Python dependencies
- `package.json` - Node.js dependencies

## Requirements

- Python 3.8+
- Node.js and npm
- Hugging Face API token (set as HF_TOKEN environment variable)
