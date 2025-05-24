from langchain_core.tools import tool
from agent.exchange_rate import converter

@tool
def exchange_rate_tool(from_curr: str, to_curr: str, amount: int) -> str:
    """Get an up-to-date exchange rate for two currencies """
    return converter(from_curr, to_curr, amount)

