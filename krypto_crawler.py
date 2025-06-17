import requests
import pandas as pd
import datetime
import time
import matplotlib.pyplot as plt


# CoinGecko API URL 
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {
    "vs_currency": "usd",
    "days": "300",  # Vergangene 30 Tage
    "interval": "daily"
}

response = requests.get(url, params=params)
data = response.json()

# Timestamps in lesbare Form bringen
prices = [
    {
        "date": datetime.datetime.fromtimestamp(p[0]/1000).strftime("%Y-%m-%d"),
        "price": p[1]
    }
    for p in data["prices"]
]

market_caps = [
    {
        "date": datetime.datetime.fromtimestamp(m[0]/1000).strftime("%Y-%m-%d"),
        "market_cap": m[1]
    }
    for m in data["market_caps"]
]

# Zusammenführen zu DataFrame
df_prices = pd.DataFrame(prices)
df_market = pd.DataFrame(market_caps)
df = pd.merge(df_prices, df_market, on="date")

# Speichern als CSV
df.to_csv("bitcoin_data.csv", index=False)
print("Daten gespeichert!")

# Visualisierung
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))

df.plot(x="date", y="price", ax=axes[0], title="Bitcoin Preis")
df.plot(x="date", y="market_cap", ax=axes[1], title="Bitcoin Market Cap")

plt.tight_layout()
plt.show()

