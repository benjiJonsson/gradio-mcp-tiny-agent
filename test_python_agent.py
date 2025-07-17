#!/usr/bin/env python3
"""
Test script for the Python MCP agent using huggingface_hub
"""
import os
import asyncio
from huggingface_hub import Agent

async def test_agent():
    """Test the Python agent with MCP server"""
    
    # Use deployed server for testing
    agent = Agent(
        model="Qwen/Qwen2.5-72B-Instruct",
        provider="nebius",
        api_key=os.getenv("HF_TOKEN"),  # Make sure to set your HF_TOKEN
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
    
    try:
        # Load tools
        await agent.load_tools()
        print(f"✅ Agent loaded successfully with {len(agent.available_tools)} tools")
        
        # List available tools
        print("\nAvailable tools:")
        for tool in agent.available_tools:
            print(f"  • {tool.function.name}: {tool.function.description}")
        
        # Test with a simple query
        print("\n" + "="*50)
        print("Testing agent with sentiment analysis...")
        response = await agent.run("Analyze the sentiment of this text: 'I love this new MCP framework!'")
        print(f"Response: {response}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure:")
        print("1. HF_TOKEN environment variable is set")
        print("2. npm and mcp-remote are installed")
        print("3. The MCP server is accessible")

if __name__ == "__main__":
    asyncio.run(test_agent())