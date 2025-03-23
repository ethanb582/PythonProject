

import stocks  # Import stocks.py from the same folder,

checker = stocks.StockChecker() # Create an instance of StockChecker class,

stock_ticker = "AAPL" # Define a stock ticker to check, # Example: Apple stock,

price = checker.get_price(stock_ticker)# Call the get_price method from the class,

prev_close = checker.get_previous_close(stock_ticker)# Call the get_previous_close method from the class,

market_cap = checker.get_market_cap(stock_ticker)# Call the get_market_cap method from the class,


stocks.stock_summary(stock_ticker, price, prev_close, market_cap) # Call the stock_summary function and pass all the data,
response = stocks.talk_to_voiceflow("I want to loose weight")  # Talk to Voiceflow
if response.startswith("Error"): # Check if the response starts with the word "Error", 
    print("Voiceflow ERROR:", response)  # If it does, print an error message with the actual response
else: # If the response does not start with "Error", 
    print("Ethan:", response) # Print the response as if it's coming from "Ethan",
