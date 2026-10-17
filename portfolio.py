
import csv

# Sample current stock prices (not live market prices)
stock_prices = {
    "AAPL": 220.00,
    "MSFT": 510.00,
    "GOOGL": 250.00,
    "TSLA": 350.00
}

portfolio = {}

# Step 1: Take investment details
number_of_stocks = int(input("How many stocks do you want to add? "))

for i in range(number_of_stocks):
    print(f"\nStock {i + 1}")

    ticker = input("Enter ticker (AAPL/MSFT/GOOGL/TSLA): ").upper().strip()

    if ticker not in stock_prices:
        print("Ticker not found in sample price list. Skipping.")
        continue

    buy_price = float(input("Enter buy price per share: "))
    quantity = int(input("Enter number of shares: "))

    if buy_price <= 0 or quantity <= 0:
        print("Price and quantity must be positive. Skipping.")
        continue

    portfolio[ticker] = {
        "buy_price": buy_price,
        "quantity": quantity
    }

# Step 2: Calculate portfolio performance
total_invested = 0
total_market_value = 0
summary = []

for ticker, details in portfolio.items():
    buy_price = details["buy_price"]
    quantity = details["quantity"]
    current_price = stock_prices[ticker]

    invested = buy_price * quantity
    market_value = current_price * quantity
    profit_loss = market_value - invested
    percentage = (profit_loss / invested) * 100

    total_invested += invested
    total_market_value += market_value

    summary.append([
        ticker,
        buy_price,
        current_price,
        quantity,
        invested,
        market_value,
        profit_loss,
        percentage
    ])

    print(f"\nStock: {ticker}")
    print(f"Invested: ${invested:.2f}")
    print(f"Current value: ${market_value:.2f}")
    print(f"Profit/Loss: ${profit_loss:.2f}")
    print(f"Gain/Loss: {percentage:.2f}%")

# Step 3: Calculate overall performance
total_profit_loss = total_market_value - total_invested

if total_invested > 0:
    total_percentage = (total_profit_loss / total_invested) * 100
else:
    total_percentage = 0

print("\n===== PORTFOLIO SUMMARY =====")
print(f"Total invested: ${total_invested:.2f}")
print(f"Total market value: ${total_market_value:.2f}")
print(f"Total profit/loss: ${total_profit_loss:.2f}")
print(f"Overall gain/loss: {total_percentage:.2f}%")

# Step 4: Save results to CSV
with open("portfolio_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Ticker",
        "Buy Price",
        "Current Price",
        "Quantity",
        "Invested",
        "Market Value",
        "Profit/Loss",
        "Gain/Loss (%)"
    ])

    writer.writerows(summary)

    writer.writerow([])
    writer.writerow([
        "TOTAL", "", "", "",
        total_invested,
        total_market_value,
        total_profit_loss,
        total_percentage
    ])

print("\nPortfolio saved to portfolio_summary.csv")
