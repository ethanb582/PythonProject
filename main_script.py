import stocks 

stock_ticker = "AAPL"
checker = stocks.StockChecker(stock_ticker)
print(checker.stock_summary()) 

checker.set_ticker("GOOGL")
print(checker.stock_summary())  

market_cap = checker.get_market_cap()

#stocks.stock_summary(stock_ticker, price, prev_close, market_cap)

response = stocks.talk_to_voiceflow("I want to loose weight") 
if response.startswith("Error"):
    print("Voiceflow ERROR:", response)
else:
    print("Ethan:", response)
    
