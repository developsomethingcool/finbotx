import streamlit as st
from agent.react_agent import react_agent
from langchain_core.messages import HumanMessage, AIMessage
from datetime import datetime

st.set_page_config(page_title="Currency Chat Agent 💱", layout="centered")

# --- Theme-aware bubble styling ---
st.markdown("""
<style>
/* Common bubble styling */
.chat-bubble {
    padding: 0.8em 1.2em;
    margin-bottom: 0.5em;
    font-size: 1.05em;
    max-width: 80%;
    line-height: 1.4;
}
/* Light mode */
@media (prefers-color-scheme: light) {
  .chat-bubble-user {
      background-color: #D1E8FF;
      color: #000;
      border-radius: 1.3em 1.3em 0.2em 1.3em;
      align-self: flex-end;
      margin-right: 2em;
  }
  .chat-bubble-ai {
      background-color: #F6F6F8;
      color: #000;
      border-radius: 1.3em 1.3em 1.3em 0.2em;
      align-self: flex-start;
      margin-left: 2em;
  }
}
/* Dark mode */
@media (prefers-color-scheme: dark) {
  .chat-bubble-user {
      background-color: #3A3A3F;
      color: #FFF;
      border-radius: 1.3em 1.3em 0.2em 1.3em;
      align-self: flex-end;
      margin-right: 2em;
  }
  .chat-bubble-ai {
      background-color: #2A2A2E;
      color: #EEE;
      border-radius: 1.3em 1.3em 1.3em 0.2em;
      align-self: flex-start;
      margin-left: 2em;
  }
}
/* Timestamps */
.chat-time {
    font-size: 0.8em;
    color: #888;
    margin-bottom: 0.8em;
}
/* Scrollable chat area */
.chat-area {
    display: flex;
    flex-direction: column;
    gap: 0.4em;
    max-height: 60vh;
    overflow-y: auto;
    padding-right: 1em;
    margin-bottom: 1.2em;
}
</style>
""", unsafe_allow_html=True)

st.title("💱 Currency Converter Agent")
st.markdown("Ask me general questions about currency or currency conversion, e.g., `How much is 100 USD in EUR?`")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Option to clear chat
col1, col2 = st.columns([0.7, 0.3])
with col2:
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()

# --- Message area ---
st.markdown('<div class="chat-area">', unsafe_allow_html=True)
for message in st.session_state.messages:
    role = message["role"]
    timestamp = message.get("time", "")
    content = message["content"]
    bubble_class = "chat-bubble-user" if role == "user" else "chat-bubble-ai"
    icon = "🧑‍💻" if role == "user" else "🤖"
    st.markdown(
        f'<div class="{bubble_class}">{icon} {content}</div>'
        f'<div class="chat-time">{timestamp}</div>' if timestamp else "",
        unsafe_allow_html=True,
    )
st.markdown('</div>', unsafe_allow_html=True)

# --- User input ---
if prompt := st.chat_input("Type your message and press Enter..."):
    timestamp = datetime.now().strftime("%H:%M")
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "time": timestamp
    })
    # Prepare message objects for agent
    chat_history = []
    for message in st.session_state.messages:
        if message["role"] == "user":
            chat_history.append(HumanMessage(content=message["content"]))
        else:
            chat_history.append(AIMessage(content=message["content"]))
    # Agent response
    with st.chat_message("assistant"):
        with st.spinner("Let me think..."):
            response = react_agent.invoke({"messages": chat_history})
            ai_message = response["messages"][-1]
            content = ai_message.content
            st.markdown(content)
    timestamp = datetime.now().strftime("%H:%M")
    st.session_state.messages.append({
        "role": "assistant",
        "content": content,
        "time": timestamp
    })