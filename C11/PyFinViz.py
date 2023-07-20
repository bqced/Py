import requests
import matplotlib.pyplot as plt

def visualize_stock_chart(stock_symbol):
    # Make API request to retrieve daily time series data for the stock symbol
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey=50VWQN1P6DU4HAGA'
    response = requests.get(url)
    data = response.json()

    # Extract time series data for daily timestamps, opening prices, and closing prices
    time_series = data.get('Time Series (Daily)', {})
    timestamps = list(time_series.keys())[::-1]  # Reverse the list of timestamps for chronological order
    opening_prices = [float(values['1. open']) for values in time_series.values()][::-1]  # Reverse the list of opening prices
    closing_prices = [float(values['4. close']) for values in time_series.values()][::-1]  # Reverse the list of closing prices

    # Select a subset of timestamps for display (e.g., every 7th timestamp)
    display_timestamps = timestamps[::7]
    display_opening_prices = opening_prices[::7]
    display_closing_prices = closing_prices[::7]

    # Plot the daily chart with lines for opening and closing prices
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, opening_prices, marker='o', color='g', label='Opening Price')
    plt.plot(timestamps, closing_prices, marker='o', color='b', label='Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{stock_symbol} Daily Stock Prices')
    plt.xticks(display_timestamps, rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Prompt the user to enter a stock symbol
stock_symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()

# Visualize the daily chart with lines for opening and closing prices for the entered stock symbol
visualize_stock_chart(stock_symbol)