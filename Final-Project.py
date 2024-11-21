"""
Brandon Wong
CS230-6
Fortune 500 Companies
URL:

The purpose of this program is to take streamlit inputs about different ways to filter the data such as state, industry,
types of data, and how many companies they would like to see. Then the program will present that data in both tables and charts.
Finally, there will be a map that has an interactive map style and tooltips.
"""

import streamlit as st

#Set up the multiple page Application
st.set_page_config(page_title="My Multi-Page App", page_icon=":tada:")

#Title of Website
st.title("Welcome to Website about Fortune 500 Companies!")
st.sidebar.success("Select a page above.") #[ST4] Customized page design features (sidebar, fonts, colors, images,navigation)


