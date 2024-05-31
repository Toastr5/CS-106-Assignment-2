stock_ticker = str((input("Enter a stock ticker symbol: ")))
shares = float(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))
#calcuations
total_investment = shares * cost_per_share
print(f"Total investment in {stock_ticker} is {total_investment}")
