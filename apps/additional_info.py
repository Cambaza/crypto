import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import yfinance as yf

def app(params):
    st.title('Additional Info')

    st.header('This information about cryptocurrency ' + params.get('currency', 'BTC-USD'))
    inf = yf.Ticker(params.get('currency', 'BTC-USD'))
    st.write(inf.info.get('description'))
    st.header('Info')



    # show major holders
    st.dataframe(inf.major_holders)

    # show institutional holders
    st.write(inf.institutional_holders)


    # show news
    st.header('Latest News')
    for i in inf.news:
        st.markdown(i['title'])
        st.markdown(i['link'])
        st.markdown(i['publisher'])

