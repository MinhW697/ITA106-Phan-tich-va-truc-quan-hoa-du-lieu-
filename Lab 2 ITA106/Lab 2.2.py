import matplotlib.pyplot as plt
import yfinance as yf
ticker = "AAPL"

start_date="2022-01-01"
end_date="2024-01-01"
stock = yf.download(ticker, start=start_date, end=end_date)
stock.head()

plt.figure(figsize=(14,7))
plt.plot(stock['Close'], label='Closing Price', color='blue')
plt.title(f'{ticker} Stock Closing Price (from {start_date} to {end_date})')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt. grid(True)

stock["MA50"] = stock["Close"].rolling(window=50).mean()
stock["MA200"] = stock["Close"].rolling(window=200).mean()

plt.figure(figsize=(14, 7))
plt.plot(stock['Close'], label='Closing Price', color='blue', alpha=0.7)
plt.plot(stock['MA50'], label='50-Day Moving Average', color='red', alpha=0.7)
plt.plot(stock['MA200'], label='200-Day Moving Average', color='green', alpha=0.7)
plt.title(f'{ticker} Stock Closing Price with Moving Averages (from {start_date} to {end_date})')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
