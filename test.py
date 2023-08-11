import requests
import json
import time
from datetime import datetime

def get_candlestick_data(symbol, interval, limit):
    endpoint = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    
    response = requests.get(endpoint, params=params)
    data = response.json()
    
    candlesticks = []
    for entry in data:
        candlestick = {
            "timestamp": entry[0] / 1000,  # Convert timestamp to seconds
            "open": float(entry[1]),
            "high": float(entry[2]),
            "low": float(entry[3]),
            "close": float(entry[4]),
            "volume": float(entry[5])
        }
        candlesticks.append(candlestick)
    
    return candlesticks

# Set your Binance API credentials
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

# Get the last 12 five-minute candlesticks for BTC
symbol = "BTCUSDT"
interval = "5m"
limit = 1200

candlesticks = get_candlestick_data(symbol, interval, limit)

for idx, candle in enumerate(candlesticks, start=1):
    timestamp = datetime.fromtimestamp(candle['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
    volume = candle['volume']
    print(f"Candle {idx} - Timestamp: {timestamp}, Volume: {volume}")
