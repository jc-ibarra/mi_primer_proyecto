import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la página
st.title('Análisis de anuncios de vehículos en EE. UU.')

# Visualización 1: Histograma del odómetro
st.header('Histograma del odómetro')
fig = px.histogram(car_data, x='odometer', title='Distribución del odómetro')
st.plotly_chart(fig)

# Visualización 2: Gráfico de dispersión de precio vs. odómetro
st.header('Gráfico de dispersión: Precio vs Odómetro')
fig2 = px.scatter(car_data, x='odometer', y='price', title='Precio vs Odómetro')
st.plotly_chart(fig2)
