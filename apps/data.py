import pandas as pd
import yfinance as yf  
import streamlit as st
import base64 

def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
        href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File</a>'
        return href

def app(params):
    ticker_data = yf.Ticker(params.get('currency', 'BTC-USD'))
    
    if len(params) > 2:
        ticker_df = ticker_data.history(interval=params['interval'], start=params['start_date'], end=params['end_date'])
    else:
        ticker_df = ticker_data.history(period=params['period'])

    st.header('Data')
    st.dataframe(ticker_df)
    
    st.markdown(filedownload(ticker_df), unsafe_allow_html=True)


    st.header('Data Statistics')
    st.dataframe(ticker_df.describe())
    st.markdown(filedownload(ticker_df.describe()), unsafe_allow_html=True)

    