# finbotx

# Currency Converter Agent 💱

A conversational AI agent built with LangGraph and Streamlit that provides real-time currency conversion and exchange rate information using natural language queries.

## Features

- **Natural Language Processing**: Ask questions in plain English like "How much is 100 USD in EUR?"
- **Real-time Exchange Rates**: Uses exchangerate.host API for up-to-date currency conversion
- **Chat Interface**: Clean, bubble-style chat UI with theme-aware styling
- **ReAct Agent**: Built with LangGraph's ReAct (Reasoning and Acting) framework
- **Local LLM**: Uses Ollama with Gemma3 model for local inference

## Project Structure

```
currency-converter-agent/
├── agent/
│   ├── __init__.py          # Package initialization
│   ├── exchange_rate.py     # Currency conversion API logic
│   ├── react_agent.py       # LangGraph ReAct agent setup
│   └── tools.py             # LangChain tool definitions
├── app.py                   # Streamlit web application
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Prerequisites

1. **Python 3.8+**
2. **LLM Provider** (choose one):
   - **Ollama** (local) - installed and running locally
   - **OpenAI API** (cloud) - API key required
   - **Anthropic Claude API** (cloud) - API key required
3. **Exchange Rate API Key** from exchangerate.host

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/developsomethingcool/finbotx
   cd finbotx
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   
   # For OpenAI (if using cloud models)
   pip install langchain-openai
   
   # For Anthropic (if using cloud models)
   pip install langchain-anthropic
   ```

3. **Set up your LLM provider:**

   **Option A: Ollama (Local)**
   ```bash
   # Install Ollama (if not already installed)
   # Visit: https://ollama.ai/download
   
   # Pull the required model
   ollama pull PetrosStav/gemma3-tools:27b
   ```

   **Option B: OpenAI (Cloud)**
   - Get your API key from: https://platform.openai.com/api-keys
   - Add to your `.env` file (see step 4)

   **Option C: Anthropic Claude (Cloud)**
   - Get your API key from: https://console.anthropic.com/
   - Add to your `.env` file (see step 4)

4. **Configure environment variables:**
   Create a `.env` file in the project root:
   
   **For Ollama (local):**
   ```env
   PRIVATE_KEY=your_exchangerate_api_key_here
   ```
   
   **For OpenAI:**
   ```env
   PRIVATE_KEY=your_exchangerate_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   
   **For Anthropic:**
   ```env
   PRIVATE_KEY=your_exchangerate_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```
   
   Get your exchange rate API key from: https://exchangerate.host/

## Usage

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** to the URL shown in the terminal (typically `http://localhost:8501`)

3. **Start chatting** with the agent using natural language:
   - "Convert 100 USD to EUR"
   - "What's the current exchange rate for GBP to JPY?"
   - "How much is 50 CAD in AUD?"

## Configuration

### Changing the LLM Model

**Using Ollama (Local):**
Update the model name in `agent/react_agent.py`:
```python
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="your-preferred-model",  # Change this
    temperature=0,
)
```

**Using OpenAI (Cloud):**
Replace the LLM configuration in `agent/react_agent.py`:
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",  # or "gpt-3.5-turbo", "gpt-4-turbo", etc.
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")  # Don't forget to import os
)
```

**Using Anthropic Claude (Cloud):**
Replace the LLM configuration in `agent/react_agent.py`:
```python
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",  # or "claude-3-opus-20240229", etc.
    temperature=0,
    api_key=os.getenv("ANTHROPIC_API_KEY")  # Don't forget to import os
)
```

### API Configuration

The exchange rate service is configured in `agent/exchange_rate.py`. You can modify the API endpoint or add additional error handling as needed.

## Architecture

- **Frontend**: Streamlit provides the web interface with custom CSS for chat bubbles
- **Agent**: LangGraph ReAct agent handles reasoning and tool usage
- **LLM**: Supports multiple providers:
  - **Ollama**: Local inference for privacy and control
  - **OpenAI**: Cloud-based GPT models (GPT-4, GPT-3.5, etc.)
  - **Anthropic**: Cloud-based Claude models (Claude-3.5, Claude-3, etc.)
- **Tools**: LangChain tools wrap the currency conversion API
- **API**: exchangerate.host provides real-time exchange rate data

## Troubleshooting

**Common Issues:**

1. **Ollama - Model not found**: Ensure you've pulled the correct Ollama model
2. **OpenAI - API errors**: Check your OpenAI API key and account credits
3. **Anthropic - API errors**: Verify your Anthropic API key and usage limits
4. **Exchange rate API errors**: Check your API key in the `.env` file
5. **Connection issues**: 
   - For Ollama: Verify Ollama is running (`ollama list`)
   - For cloud providers: Check your internet connection
6. **Import errors**: Make sure all dependencies are installed

**Debug Mode:**

Uncomment the graph visualization code in `agent/react_agent.py` to generate a visual representation of the agent's decision-making process.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- Powered by [Ollama](https://ollama.ai/)
- Exchange rates from [exchangerate.host](https://exchangerate.host/)
- UI built with [Streamlit](https://streamlit.io/)
