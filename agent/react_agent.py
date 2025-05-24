from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from agent.tools import exchange_rate_tool

llm = ChatOllama(
    model="PetrosStav/gemma3-tools:27b",
    temperature=0,
    )

tools = [exchange_rate_tool]

react_agent = create_react_agent(
    model = llm,
    tools = tools,
)

# Visualize the graph
#=================================
# Create the graph structure and store it in .png
# image_data = react_agent.get_graph(xray=True).draw_mermaid_png()
# file_path = "react_agent_graph.png"
# with open(file_path, "wb") as file:
#     file.write(image_data)
#=================================

