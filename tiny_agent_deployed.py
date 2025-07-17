import os
from huggingface_hub import Agent
from huggingface_hub.inference._mcp.mcp_client import StdioServerConfig

# For deployment - connects to the HF Space server
agent = Agent(
    model="Qwen/Qwen2.5-72B-Instruct",
    provider="nebius",
    servers=[
        StdioServerConfig(
            command="npx",
            args=[
                "mcp-remote",
                "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse"  # Deployed HF Space
            ]
        )
    ],
)