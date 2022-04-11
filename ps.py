import pandas as pd
import streamlit as st

# Fungsi
def run_ps_app():
    st.subheader("RUP Paket Swakelola")
    df = pd.read_json("data/ps.json")
    st.dataframe(df)