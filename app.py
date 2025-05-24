import streamlit as st
from agent.react_agent import react_agent
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="Currency Chat Agent 💱")

st.title("Currency converter agent")
st.write("Ask me general questions about currency and about currency conversion")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous message history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new user input
if prompt := st.chat_input("How can I assist you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    chat_history = []
    for message in st.session_state.messages:
        if message["role"] == "user":
            chat_history.append(HumanMessage(content=message["content"]))
        else:
            chat_history.append(AIMessage(content=message["content"]))


    with st.chat_message("assistant"):
        with st.spinner("Let me think..."):
            response = react_agent.invoke({"messages": chat_history})
            ai_message = response["messages"][-1]
            content = ai_message.content
            st.markdown(content)

    st.session_state.messages.append({"role": "assistant", "content":content})