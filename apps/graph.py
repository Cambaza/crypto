import streamlit as st

import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

def app(params):
    ticker_data = yf.Ticker(params.get('currency', 'BTC-USD'))
    
    if len(params) > 2:
        ticker_df = ticker_data.history(interval=params['interval'], start=params['start_date'], end=params['end_date'])
    else:
        ticker_df = ticker_data.history(period=params['period'])
    fig = go.Figure(
            data=[go.Candlestick(x=ticker_df.index,open=ticker_df.Open, 
                                high=ticker_df.High, low=ticker_df.Low, 
                                close=ticker_df.Close, increasing_line_color='green', 
                                decreasing_line_color='red')
                    ]
                    )
    st.header('Candle stick')
    st.plotly_chart(fig)
    
    st.header('Close Price')
    st.line_chart(ticker_df['Close'])

    st.header('Volume')
    st.bar_chart(ticker_df['Volume'], use_container_width=True, )
    
