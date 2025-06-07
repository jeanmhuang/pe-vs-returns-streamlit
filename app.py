import streamlit as st
import yfinance as yf
import plotly.express as px

st.set_page_config(page_title="Market Pulse", layout="wide")
st.title("📈 Market Pulse: Stock Dashboard")

ticker = st.sidebar.selectbox("Choose a stock", ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "JPM", "XOM", "WMT", "JNJ"])

data = yf.download(ticker, period="1y")
info = yf.Ticker(ticker).info

st.subheader(f"{ticker} Price Chart (1 Year)")
fig = px.line(data, x=data.index, y="Close", title=f"{ticker} Closing Price")
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 🔍 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("1-Year Return", f"{((data['Close'][-1] / data['Close'][0] - 1)*100):.2f}%")
col2.metric("P/E Ratio", info.get("trailingPE", 'N/A'))
col3.metric("Market Cap", f"{info.get('marketCap', 0):,}")
