import streamlit as st

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

