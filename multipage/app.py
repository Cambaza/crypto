import streamlit as st
from multiapp import MultiApp
from apps import graph, data, additional_info # import your app modules here

app = MultiApp()


# Add all your application here
app.add_app("Data", data.app)
app.add_app("Graphs", graph.app)
app.add_app("Additional Information", additional_info.app)
# The main app
app.run()