# main_script.py

import stocks  # Import stocks.py from the same folder,

# Create an instance of StockChecker class,
checker = stocks.StockChecker()

# Define a stock ticker to check,
stock_ticker = "AAPL"  # Example: Apple stock,

# Call the get_price method from the class,
price = checker.get_price(stock_ticker)

# Call the get_previous_close method from the class,
prev_close = checker.get_previous_close(stock_ticker)

# Call the get_market_cap method from the class,
market_cap = checker.get_market_cap(stock_ticker)

# Call the stock_summary function and pass all the data,
stocks.stock_summary(stock_ticker, price, prev_close, market_cap)
response = stocks.talk_to_voiceflow("I want to loose weight")  # Talk to Voiceflow
if response.startswith("Error"):
    print("Voiceflow ERROR:", response)
else:
    print("Ethan:", response)
