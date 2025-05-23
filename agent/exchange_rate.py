import requests
import os 
from dotenv import load_dotenv, dotenv_values 

load_dotenv() 
api_key = os.getenv("PRIVATE_KEY")


def converter(from_curr, to_curr, amount):
    """Makes API Request to currency exchange service to get up-to-date exchange rate"""
    URL = f"https://api.exchangerate.host/convert?access_key={api_key}&from={from_curr.upper()}&to={to_curr.upper()}&amount={amount}"
    try:
        r = requests.get(url = URL)
        data = r.json()
        print(f'Results: {data}')
        return data
    except requests.exceptions.RequestException as errex:
        print("Exception request")

#print(converter("JPY", "EUR", 100000))

