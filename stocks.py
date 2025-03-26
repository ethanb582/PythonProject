# stocks.py
import requests  # Importing requests to make API calls,
import yfinance as yf# Importing Yahoo Finance to fetch real stock data,

class StockChecker:  # Defining a class to manage stock data retrieval,
    def __init__(self, ticker): 
        self.ticker = ticker
        
    def get_price(self, ticker):  # Method to fetch the latest stock price,
        stock = yf.Ticker(ticker)  # Create a Yahoo Finance object for the stock,
        price = stock.history(period="1d")["Close"].iloc[-1]  # Get latest closing price,
        return round(price, 2)  # Return rounded price,

    def get_previous_close(self, ticker):  # Method to fetch the previous close price,
        stock = yf.Ticker(ticker)  # Create a Yahoo Finance object for the stock,
        prev_close = stock.info.get("previousClose", "N/A")  # Get previous close price,
        return round(prev_close, 2) if isinstance(prev_close, (int, float)) else "N/A"  # Ensure it’s a number before rounding,

    def get_market_cap(self, ticker):  # Method to fetch the market capitalization of the stock,
        stock = yf.Ticker(ticker)  # Create a Yahoo Finance object for the stock,
        market_cap = stock.info.get("marketCap", "N/A")  # Get market cap,
        return f"${market_cap:,}" if isinstance(market_cap, int) else "N/A"  # Format as a readable number,

def stock_summary(ticker, price, prev_close, market_cap):  # Function outside the class to display stock summary,
    print(f"Stock: {ticker.upper()}")  # Display stock ticker,
    print(f"Current Price: ${price}")  # Display current price,
    print(f"Previous Close: ${prev_close}")  # Display previous close price,
    print(f"Market Cap: {market_cap}")  # Display market cap,

API_KEY = ""
PROJECT_ID = ""
USER_ID = ""  # Static user ID for Voiceflow

def talk_to_voiceflow(user_input):#function to send user input to Voiceflow and get a response 
    url = f"https://general-runtime.voiceflow.com/state/user/{USER_ID}/interact"

    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "userID": USER_ID, 
        "actions": [{"type": "text", "payload": user_input}]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        try:
            messages = response.json()
            print("Voiceflow Raw Response:", messages)

            for msg in messages:
                if "payload" in msg and "message" in msg["payload"]:
                    return msg["payload"]["message"]

            return "Voiceflow responded but didn't include a message."

        except Exception as e:
            return f"Error parsing response: {e}"

    elif response.status_code == 429:
        retry_after = response.headers.get("Retry-After")
        wait_time = f"{retry_after} seconds" if retry_after else "a few moments"
        return f"Error 429: Too Many Requests – You’ve hit the rate limit. Please wait {wait_time} before retrying."

    elif response.status_code == 503:
        return "Error 503: Voiceflow under maintenance, please visit https://statusgator.com/services/voiceflow for updates."

    else :
        return f"Error {response.status_code}: {response.text}
