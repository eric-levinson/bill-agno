import asyncio

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools, MultiMCPTools
from gridiron_toolkit.info import GridironTools

# This is the URL of the MCP server we want to use.
server_url = "http://192.168.68.66:8000/mcp/"


async def run_agent(message: str) -> None:

    # Initialize the MCP tools
    mcp_tools = MCPTools(transport="streamable-http", url=server_url)

    # Connect to the MCP server
    await mcp_tools.connect()
    print("Received MCP tools:", mcp_tools)
    
    # Place this directly after `await mcp_tools.connect()`
    mcp_tools.functions = {k: v for k, v in getattr(mcp_tools, "functions", {}).items() if k in {"get_player_info_tool", "get_players_by_sleeper_id_tool"}}
    print("Revised Received MCP tools:", mcp_tools)
    # Initialize the Agent
    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        tools=[mcp_tools],
        show_tool_calls=True,
        markdown=True,
    )

    # Run the agent
    await agent.aprint_response(message=message, stream=True, markdown=True)

    # Close the MCP connection
    await mcp_tools.close()


if __name__ == "__main__":
    asyncio.run(run_agent("Find the player with sleeper ID 11631"))