# cli.py

from bot.client import BinanceClient
import time
import random  # ✅ fixed import

def main():
    client = BinanceClient()

    # Display fake account info
    account_info = client.get_account_info()
    print("\nFake Account Balances:")
    for asset in account_info["balances"]:
        print(f"{asset['asset']}: {asset['free']}")

    # Fake trading loop
    print("\nStarting fake trading loop...")
    symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]

    for _ in range(3):  # run 3 fake trades
        symbol = symbols[_ % len(symbols)]
        price = client.get_price(symbol)
        quantity = round(random.uniform(0.01, 0.1), 4)
        client.create_order(symbol=symbol, side="BUY", quantity=quantity, price=price)
        time.sleep(1)

if __name__ == "__main__":
    main()
