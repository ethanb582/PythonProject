# stocks.py
import requests   
import yfinance as yf

class StockChecker: 
    def __init__(self, ticker): 
        self.ticker = ticker

    def get_ticker(self):
        return self.ticker  # Getter method that returns the current ticker stored in the object

    def set_ticker(self, new_ticker):
        self.ticker = new_ticker  # Setter method that updates the value of the ticker stored in the object

    def get_price(self): 
        """Fetches real stock price for a given ticker"""
        stock = yf.Ticker(self.ticker)  
        price = stock.history(period="1d")["Close"].iloc[-1]  
        return round(price, 2) 

    def get_previous_close(self): 
        """Fetches the previous day's closing price"""
        stock = yf.Ticker(self.ticker) 
        prev_close = stock.info.get("previousClose", "N/A")  
        return round(prev_close, 2) if isinstance(prev_close, (int, float)) else "N/A" 

    def get_market_cap(self): 
        #Fetches the stock's market capitalization
        stock = yf.Ticker(self.ticker) 
        market_cap = stock.info.get("marketCap", "N/A") 
        return f"${market_cap:,}" if isinstance(market_cap, int) else "N/A" 

    def stock_summary(self): 
        """Prints a simple stock summary"""
        print(f"Stock: {self.ticker.upper()}")  
        print(f"Current Price: ${self.get_price()}") 
        print(f"Previous Close: ${self.get_previous_close()}") 
        print(f"Market Cap: {self.get_market_cap()}") 

API_KEY = ""
PROJECT_ID = ""
USER_ID = "" 

def talk_to_voiceflow(user_input):
    #Sends user input to the Voiceflow API and returns a response
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
        return f"Error {response.status_code}: {response.text}"
