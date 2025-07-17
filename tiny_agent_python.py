import os
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
                "http://localhost:7860/gradio_api/mcp/sse"  # Your Gradio MCP server
            ]
        )
    ],
)