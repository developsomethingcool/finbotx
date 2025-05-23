from langchain_core.tools import tool
from exchange_rate import *

@tool
def exchange_rate_tool(from_curr: str, to_curr: str) -> str:
    """Get an up-to-date exchange rate for two currencies """
    pass