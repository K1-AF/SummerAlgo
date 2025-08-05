import yfinance as yf
import matplotlib.pyplot as plt

# 1. Download AAPL historical data (daily)
data = yf.download('AAPL', start='2000-01-01')  # You can adjust the start date

# 2. Simulate buying $1000 worth of AAPL at the first available close price
initial_cash = 1000
buy_price = data['Close'].iloc[0]
shares_bought = initial_cash / buy_price

# 3. Value at the end (latest close)
final_price = data['Close'].iloc[-1]
final_value = float(shares_bought * final_price)

# Plot portfolio value over time
portfolio_values = data['Close'] * shares_bought
plt.figure(figsize=(10, 5))
plt.plot(data.index, portfolio_values, label='Portfolio Value')
plt.title('Buy and Hold Portfolio Value Over Time (AAPL)')
plt.xlabel('Date')
plt.ylabel('Portfolio Value ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Calculate return
percent_return = ((final_value - initial_cash) / initial_cash) * 100

print(f"Buy and Hold AAPL from {data.index[0].date()} to {data.index[-1].date()}")
print(f"Initial investment: ${initial_cash:.2f}")
print(f"Final value: ${final_value:.2f}")
print(f"Total return: {percent_return:.2f}%")