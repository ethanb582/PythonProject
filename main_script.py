import stocks 

stock_ticker = "AAPL"
checker = stocks.StockChecker(stock_ticker, 5, 2) 

checker.stock_summary()

checker.set_ticker("GOOGL")
checker.stock_summary()

market_cap = checker.get_market_cap()
print("GOOGL Market Cap:", market_cap)

response = stocks.talk_to_voiceflow("I want to lose weight") 
if response.startswith("Error"):
    print("Voiceflow ERROR:", response)
else:
    print("Ethan:", response)
