import streamlit as st
import pandas as pd


st.title("Aplikasi Penyewaan Sepeda")


@st.cache_data
def load_data():
    data = pd.read_csv('data/all_data.csv')
    return data


all_data = load_data()



st.write(all_data.columns.tolist())


if 'dteday' in all_data.columns:
    all_data['dteday'] = pd.to_datetime(all_data['dteday'])  
    all_data['weekday'] = all_data['dteday'].dt.dayofweek  

    
    st.write("Data Penyewaan Sepeda:")
    st.dataframe(all_data)

    
    st.subheader("Jumlah Penyewaan Sepeda per Hari dalam Seminggu")
    count_per_weekday = all_data['weekday'].value_counts().sort_index()
    st.bar_chart(count_per_weekday)
else:
    st.error("Kolom 'dteday' tidak ditemukan dalam data.")
