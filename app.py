import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Meu Aplicativo Streamlit')

car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão
     
if hist_button: # se o botão for clicado
         # escrever uma mensagem
         st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um histograma
         fig = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)


# Lendo os dados
car_data = pd.read_csv('vehicles_us.csv')

# Criando botões para diferentes tipos de gráficos
hist_button = st.button('Criar histograma')
scatter_button = st.button('Criar gráfico de dispersão')

# Verificando qual botão foi clicado
if hist_button:
    # Escrevendo uma mensagem
         st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # Criando um histograma
         fig = px.histogram(car_data, x="odometer")
    
    # Exibindo um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    # Escrevendo uma mensagem
         st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # Criando um gráfico de dispersão
         fig = px.scatter(car_data, x="year", y="price", color="manufacturer", size="odometer", hover_name="model", title="Car Price vs Year")
    
    # Exibindo um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)         