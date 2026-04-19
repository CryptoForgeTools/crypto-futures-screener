# Crypto Futures Screener

Real-time crypto futures signal screener built with Python, 
Streamlit and ccxt. Scans multiple coins for trading signals 
based on price action and volume.

## Features
- Live price data from Binance Futures
- 24h change and volume tracking
- Automatic signal detection
- Auto-refreshes every 60 seconds
- Clean Streamlit dashboard UI

## Tech Stack
- Python
- Streamlit
- ccxt
- Pandas

## Signals
- 🟢 Long Setup — price up 2%+ with high volume
- 🔴 Short Setup — price down 2%+ with high volume
- ⚪ No Signal — no clear condition met
