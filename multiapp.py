"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
import pandas as pd

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })


    def run(self):
        # app = st.sidebar.radio(
        app = st.sidebar.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])
        tickers = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'BCH-USD', 'ADA-USD', 'DOT-USD','LTC-USD', 'XEM-USD', 'XLM-USD', 'EOS-USD', 'SOL-USD']
        curr = st.sidebar.selectbox('Currency', tickers)
        option = st.sidebar.radio('Select option', ['1d','5d','1mo','6mo','1y','ytd','max', 'custom'], index=3)
        custom = dict()
        if option=='custom':
            start_date = st.sidebar.date_input('Start Date:', value=pd.to_datetime("2021-01-31", format="%Y-%m-%d"))
            end_date = st.sidebar.date_input('End Date:', value=pd.to_datetime("today", format="%Y-%m-%d"))
            
            interv = st.sidebar.selectbox('Select Interval', ['1h','1d','1wk','1mo','3mo' ])
            custom = {'start_date': start_date, 'end_date': end_date, 'currency': curr, 'interval': interv}

        params = {'period': option, 'currency': curr}
        
        params.update(custom)

        
        app['function'](params)
