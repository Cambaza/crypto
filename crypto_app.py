import yfinance as yf
import streamlit as st 
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from PIL import Image


image = Image.open('Bike-Europe-Stock-Chart.jpeg')
image.thumbnail((200, 200)) 
st.image(image=image, use_column_width=True)

st.write('''
# Stock & Crypto price app
## 
''')
def get_input():
    start_date = st.sidebar.date_input('Start Date:', value=pd.to_datetime("2021-01-31", format="%Y-%m-%d"))
    end_date = st.sidebar.date_input('End Date:', value=pd.to_datetime("today", format="%Y-%m-%d"))
    option = st.sidebar.radio('Choose asset', options=['Stocks', 'Crypto'])
    if option == 'Stocks':
        drop = ['AAPL', 'MSFT', 'GOOG', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'NVDA', 'BRK.B', 'BRK.A']
    elif option == 'Crypto':
        drop = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'BCH-USD', 'ADA-USD', 'DOT-USD','LTC-USD', 'XEM-USD', 'XLM-USD', 'EOS-USD', 'SOL-USD']
    drop = st.sidebar.selectbox(options=drop, label='Select asset')
    
    
    return option, drop, start_date, end_date

option, drop, start_date, end_date = get_input()

st.header(option)
ticker_symbol = drop
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(interval='1d', start=start_date, end=end_date)

fig = go.Figure(
            data=[go.Candlestick(x=ticker_df.index,open=ticker_df.Open, 
                                high=ticker_df.High, low=ticker_df.Low, 
                                close=ticker_df.Close, increasing_line_color='green', 
                                decreasing_line_color='red'
        )
    ]
)


st.header('Data')
st.write(ticker_df)

st.header('Data Statistics')
st.write(ticker_df.describe())

st.header('Close Price')
st.line_chart(ticker_df['Close'])

st.header('Volume')
st.bar_chart(ticker_df['Volume'])


st.header('Candle stick')
st.plotly_chart(fig)


