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

This project implements both a Gradio MCP client and a tiny agent configuration following the tutorial sheets.

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

### Gradio MCP Client

Run the Gradio interface:
```bash
python app.py
```

This will start a web interface that connects to the MCP server and provides a chat interface.

### Tiny Agent (JSON Configuration)

Run the tiny agent via JSON configuration:
```bash
cd my-agent
tiny-agents run agent.json
```

The agent is configured to connect to the MCP server via the `my-agent/agent.json` configuration file.

### Python Agent (huggingface_hub)

You can also create a Python agent using the huggingface_hub library:

```python
from huggingface_hub import Agent

agent = Agent(
    model="Qwen/Qwen2.5-72B-Instruct",
    provider="nebius",
    servers=[
        {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse"
            ]
        }
    ],
)
```

Test the Python agent:
```bash
python test_python_agent.py
```

## Files

- `app.py`: Gradio MCP client implementation
- `my-agent/agent.json`: Tiny agent JSON configuration
- `tiny_agent_python.py`: Python agent using huggingface_hub (local server)
- `tiny_agent_deployed.py`: Python agent using huggingface_hub (deployed server)
- `test_python_agent.py`: Test script for Python agent
- `requirements.txt`: Python dependencies
- `package.json`: Node.js dependencies

## Environment Variables

- `HF_TOKEN`: Hugging Face API token for model access
