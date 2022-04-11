# Core PKGS
import pandas as pd
import streamlit as st

#from Project.rup.ps import run_ps_app
#from Project.rup.pp import run_pp_app

# Import Function Penyedia dan Swakelola
from pp import run_pp_app
from ps import run_ps_app

def main():
    #st.title("Dashboard RUP")

    # Sidebar
    menu = ["Home", "Penyedia", "Swakelola"]
    pilih = st.sidebar.selectbox("Pilih Paket RUP :", menu)

    # Content
    if pilih == "Home":
        st.subheader("Home")
    elif pilih == "Penyedia":
        run_pp_app()
    else:
        run_ps_app()

if __name__ == '__main__':
    main()
