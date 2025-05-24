from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_ollama import ChatOllama
from langchain.memory import ConversationBufferMemory

from langchain.prompts import PromptTemplate
from tools import exchange_rate_tool
from IPython.display import Image, display
from langchain_core.messages import HumanMessage, SystemMessage

# initialize ConversationalMemory
#memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

llm = ChatOllama(
    model="PetrosStav/gemma3-tools:27b",
    temperature=0,
    )

tools = [exchange_rate_tool]

react_agent = create_react_agent(
    model = llm,
    tools = tools,
    #prompt="Do not use exchnage rate tool!",
)

#display(Image(react_agent.get_graph(xray=True).draw_mermaid_png()))

# Create the graph structure and store it in .png
image_data = react_agent.get_graph(xray=True).draw_mermaid_png()
file_path = "react_agent_graph.png"
with open(file_path, "wb") as file:
    file.write(image_data)

messages = [
    HumanMessage(content="What is the capital of France?")
]

messages = react_agent.invoke({"messages": messages})
print(f"Messages {messages}")

