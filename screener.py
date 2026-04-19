import streamlit as st
import pandas as pd
import ccxt
import time

st.set_page_config(
    page_title="Crypto Futures Screener",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Crypto Futures Screener")
st.caption("Real-time signal scanner for crypto futures")

st.divider()

# Auto refresh every 60 seconds
refresh = st.empty()
refresh.caption("🔄 Refreshing every 60 seconds")

# Connect to Binance futures
exchange = ccxt.binance({
    'options': {
        'defaultType': 'future'
    }
})

# Watchlist
watchlist = [
    'BTC/USDT:USDT',
    'ETH/USDT:USDT',
    'SOL/USDT:USDT',
    'SUI/USDT:USDT',
    '1000PEPE/USDT:USDT'
]

# Fetch prices for all coins
st.subheader("Live Prices")

data = []

with st.spinner("Fetching live data..."):
    for symbol in watchlist:
        try:
            ticker = exchange.fetch_ticker(symbol)
            price = ticker['last']
            change = ticker['percentage']
            volume = ticker['quoteVolume']

            # Signal logic
            if change > 2 and volume > 500_000_000:
                signal = "🟢 Long Setup"
            elif change < -2 and volume > 500_000_000:
                signal = "🔴 Short Setup"
            else:
                signal = "⚪ No Signal"

            data.append({
                "Coin": symbol.replace('/USDT:USDT', ''),
                "Price": f"${price:,.4f}",
                "24h Change": f"{change:.2f}%",
                "24h Volume": f"${volume:,.0f}",
                "Signal": signal,
            })
        except Exception as e:
            data.append({
                "Coin": symbol,
                "Price": "Error",
                "24h Change": "Error",
                "24h Volume": "Error",
                "Signal": "Error",
            })

df = pd.DataFrame(data)

def color_signal(val):
    if "Long" in str(val):
        return 'color: green'
    elif "Short" in str(val):
        return 'color: red'
    return ''

styled_df = df.style.map(color_signal, subset=['Signal'])

st.dataframe(
    styled_df,
    use_container_width=True,
    hide_index=True
)

st.divider()
st.caption(f"Last updated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
time.sleep(60)
st.rerun()