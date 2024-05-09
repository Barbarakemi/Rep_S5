import os
import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Meu Aplicativo Streamlit')

car_data = pd.read_csv('vehicles.csv')  # lendo os dados

# Criando botões para diferentes tipos de gráficos
hist_button = st.button('Criar histograma', key= "hist_button")
scatter_button = st.button('Criar gráfico de dispersão', key= "scatter_button")

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
    fig = px.scatter(car_data, x="model_year", y="price", color="manufacturer", size="odometer", hover_name="model",
                     title="Car Price vs Year")

    # Exibindo um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Adicionando a funcionalidade para excluir arquivos
delete_button = st.button('Excluir arquivo', key= "delete_button")

if delete_button:
    file_to_delete = st.text_input('Digite o nome do arquivo a ser excluído:', value='nome_do_arquivo.csv')
    
    # Verificando se o arquivo existe
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
        st.write(f'O arquivo "{file_to_delete}" foi excluído com sucesso!')
    else:
        st.write(f'O arquivo "{file_to_delete}" não foi encontrado.')