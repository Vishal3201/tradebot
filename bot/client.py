# bot/client.py

import os
import random
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "fake_secret_key_0987654321")
SECRET_KEY = os.getenv("SECRET_KEY", "fake_secret_key_0987654321")

class BinanceClient:
    def __init__(self, api_key=API_KEY, secret_key=SECRET_KEY):
        self.api_key = api_key
        self.secret_key = secret_key
        print(f"Initialized BinanceClient with API_KEY={api_key}")

    def get_account_info(self):
        # Fake balances
        return {
            "balances": [
                {"asset": "BTC", "free": str(round(random.uniform(0, 1), 6))},
                {"asset": "ETH", "free": str(round(random.uniform(0, 10), 4))},
                {"asset": "USDT", "free": str(round(random.uniform(0, 1000), 2))},
            ],
            "accountType": "SPOT"
        }

    def create_order(self, symbol, side, quantity, price=None):
        # Fake order creation
        order_id = random.randint(1000, 9999)
        print(f"Fake order created: {side} {quantity} {symbol} at {price if price else 'market'} (ID: {order_id})")
        return {
            "symbol": symbol,
            "side": side,
            "quantity": quantity,
            "price": price if price else "market",
            "status": "FILLED",
            "orderId": order_id
        }

    def get_price(self, symbol):
        # Fake price data
        return round(random.uniform(1000, 50000), 2)
