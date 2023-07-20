import requests
import matplotlib.pyplot as plt

# Make the API request
url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=50VWQN1P6DU4HAGA'
response = requests.get(url)
data = response.json()

# Extract top gainers and top losers data
top_gainers = data['top_gainers']
top_losers = data['top_losers']

# Extract ticker symbols and change percentages for top gainers
gainer_ticker_symbols = [gainer['ticker'] for gainer in top_gainers]
gainer_change_percentages = [float(gainer['change_percentage'].strip('%')) for gainer in top_gainers]

# Extract ticker symbols and change percentages for top losers
loser_ticker_symbols = [loser['ticker'] for loser in top_losers]
loser_change_percentages = [float(loser['change_percentage'].strip('%')) for loser in top_losers]

# Plot the top gainers chart
plt.figure(figsize=(10, 6))
plt.bar(gainer_ticker_symbols, gainer_change_percentages, color='g')
plt.xlabel('Ticker Symbol')
plt.ylabel('Change Percentage (%)')
plt.title('Top Gainers in the Stock Market')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Plot the top losers chart
plt.figure(figsize=(10, 6))
plt.bar(loser_ticker_symbols, loser_change_percentages, color='r')
plt.xlabel('Ticker Symbol')
plt.ylabel('Change Percentage (%)')
plt.title('Top Losers in the Stock Market')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()