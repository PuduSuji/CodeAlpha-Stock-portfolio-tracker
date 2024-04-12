import requests

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= quantity:
                self.portfolio[symbol] -= quantity
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]
            else:
                print("Error: Not enough shares of", symbol)
        else:
            print("Error: Stock", symbol, "not found in portfolio")

    def track_portfolio(self):
        print("Current Portfolio:")
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price is not None:
                value = price * quantity
                total_value += value
                print(f"{symbol}: {quantity} shares - Current Price: ${price:.2f} - Total Value: ${value:.2f}")
            else:
                print(f"Error: Failed to fetch data for {symbol}")
        print("Total Portfolio Value: ${:.2f}".format(total_value))

    def get_stock_price(self, symbol):
        API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
        try:
            response = requests.get(url)
            data = response.json()
            price = float(data['Global Quote']['05. price'])
            return price
        except Exception as e:
            print("Error fetching data for", symbol, ":", e)
            return None
