import streamlit as st 
import pandas as pd
import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import tabs_content as t

st.title("NASA Battery Data Analysis App")
st.write("An interactive app for visualizing battery cell cycling data and analyzing degradation behavior")

# Metadata Analysis 
tab1,tab2,tab3, = st.tabs(["Summary","Exploratory Data Analysis","Capacity Computations"])

with tab1:
    t.tab1_render()

with tab2 : 
    t.tab2_render()
    
with tab3 :
    t.tab3_render()    