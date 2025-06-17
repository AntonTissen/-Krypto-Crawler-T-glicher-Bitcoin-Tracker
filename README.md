# -Krypto-Crawler-T-glicher-Bitcoin-Tracker

Ein einfaches Projekt das ich einfach aus Spaß erstellt habe: 

Ein einfacher Python-Crawler, der **Preis und Marktkapitalisierung anzeigt** über die CoinGecko API abruft und in einer CSV-Datei speichert.

---

## 🚀 Features

- Holt täglich den aktuellen **Bitcoin-Preis** (`USD`) und die **Market Cap**
- Speichert die Daten lokal in einer CSV-Datei (`btc_daily.csv`)
- Fügt **automatisch neue Zeilen** hinzu – **keine Duplikate**
- Einfach erweiterbar für weitere Coins
- Bereit für Automatisierung (z. B. per `cron`)

---

## 🖥️ Beispielausgabe (`btc_daily.csv`)

```csv
date,price_usd,market_cap_usd
2025-06-17,66300.45,1280000000000
2025-06-18,67010.12,1305000000000
