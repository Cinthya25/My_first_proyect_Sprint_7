import streamlit as st
import pandas as pd
import plotly.express as px
vehicles_df= pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma') 
dispertion_button= st.button('Gráfico de dispersión')
        
if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(vehicles_df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if dispertion_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig= px.scatter(vehicles_df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

