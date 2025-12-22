# Stock Portfolio Tracker - CodeAlpha

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("📊 Welcome to Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish adding stocks.\n")

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available. Try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
    except ValueError:
        print("❌ Please enter a valid number.\n")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    investment = stock_prices[stock_name] * quantity
    total_investment += investment

    print(f"✅ Added {quantity} shares of {stock_name}\n")

print("\n📈 Portfolio Summary")
for stock, qty in portfolio.items():
    print(f"{stock} - {qty} shares @ {stock_prices[stock]} each")

print(f"\n💰 Total Investment Value: ₹{total_investment}")

# Optional: Save result to file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock} - {qty} shares @ {stock_prices[stock]}\n")
    file.write(f"\nTotal Investment Value: ₹{total_investment}")

print("\n📁 Portfolio saved to portfolio_summary.txt")
