import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi
def run_pp_app():
    st.title("RUP Paket Penyedia")

    # Ambil dan olah data
    pp = pd.read_csv("data/pp.csv")
    ppc = pp[pp['statusumumkan'] == 'Terumumkan']

    # Menghitung Total Paket
    totalpaket = format(ppc.shape[0],',d')
    # Menghitung Total Pagu
    #totalpagu = (format(ppc['jumlahpagu'].sum(),',d'))
    totalpagu = ('{:,}'.format(ppc['jumlahpagu'].sum()))
    # Menghitung Jumlah Satker
    satker = ppc['namasatker'].value_counts().shape[0]

    # Tampilkan di Streamlit
    ## Baris Pertama - 3 Kolom
    kol1,kol2,kol3 = st.columns(3)
    kol1.metric("Total Satker", satker)
    kol2.metric("Total Paket", totalpaket)
    kol3.metric("Total Pagu", totalpagu)

    ## Baris Kedua - Grafik
    ppc1 = ppc['metodepengadaan'].value_counts()
    ppc2 = ppc['jenispengadaan'].value_counts()
    graph1,graph2 = st.columns(2)
    graph1.line_chart(ppc1)
    graph2.bar_chart(ppc2)