import streamlit as st
import pandas as pd
import datetime
import plotly.graph_objects as go
from PIL import Image


st.write('''
# Cryptocurrency Dashboard Application
Visually show data on crypto (BTC, ADA & ETH) from **'2019-12-08' to '2021-05-01'**
''')
image = Image.open('8crypto.webp')
st.image(image=image, use_column_width=True)


st.sidebar.header('User input')

def get_input():
    start_date = st.sidebar.text_input('Start Date:', '2020-01-01')
    end_date = st.sidebar.text_input('End Date:', '2020-09-01')
    crypto_symbol = st.sidebar.text_input('Crypto Symbol', 'BTC')
    return start_date, end_date, crypto_symbol


def get_crypto_name(symbol):
    symbol = symbol.upper()
    if symbol == 'BTC':
        return 'Bitcoin'
    elif symbol == 'ETH':
        return 'Ethereum'
    elif symbol == 'ADA':
        return 'Cardano'
    else:
        return None


def get_data(symbol, start, end):
    symbol = symbol.upper()
    if symbol == 'BTC':
        df = pd.read_csv('Binance_BTCUSDT_d.csv')
    elif symbol == 'ETH':
        df = pd.read_csv('Binance_ETHUSDT_d.csv')
    elif symbol == 'BTC':
        df = pd.read_csv('Binance_ADAUSDT_d.csv')
    else:
        df = pd.DataFrame(columns=['date', 'close', 'open', 'Volume', 'Adj. close'])

    #start = pd.to_datetime(start)
    #end = pd.to_datetime(end)
    #between_start_end = (df['date'] >= start) &(df['date'] < end)
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='ignore')
    df = df.set_index(pd.DatetimeIndex(df['date'].values))
    #print(df.head())
    return df[start:end]



start, end, symbol = get_input()
df = get_data(symbol=symbol, start=start, end=end)

crypto_name = get_crypto_name(symbol=symbol)

fig = go.Figure(
            data=[go.Candlestick(x=df.index,open=df.open, 
                                high=df.high, low=df.low, 
                                close=df.close, increasing_line_color='green', 
                                decreasing_line_color='red'
        )
    ]
)


st.header(crypto_name+' Data')
st.write(df)

st.header(crypto_name+' Data Statistics')
st.write(df.describe())

st.header(crypto_name+' Close Price')
st.line_chart(df['close'])

st.header(crypto_name+' Volume')
st.bar_chart(df['tradecount'])


st.header(crypto_name+' candle stick')
st.plotly_chart(fig)