import streamlit as st
import pandas as pd
import plotly.express as px

# Configura a página do Streamlit para utilizar o layout 'wide', expandindo o conteúdo para usar mais espaço horizontal na tela.
st.set_page_config(layout="wide")

# Leitura dos dados das planilhas Excel de revisões e dos 100 livros mais populares.
df_reviews = pd.read_excel("C:\\Users\\Ander\\OneDrive\\Área de Trabalho\\datasets\\customer-reviews.xlsx")
df_top100_books = pd.read_excel("C:/Users/Ander/OneDrive/Área de Trabalho/datasets/Top-100-Trending-Books.xlsx")

# Função max(), varre os preços e retorna o maior dentre eles.
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

# Slider na barra lateral para selecionar faixa de preço dos livros.
max_price = st.sidebar.slider("Faixa de preço", price_min, price_max, price_max)

# Filtragem dos livros com preço até o valor selecionado.
df_books = df_top100_books[df_top100_books["book price"] <= max_price]

# Criação de um gráfico de barras mostrando a contagem de livros publicados por ano.
fig = px.bar(df_books["year of publication"].value_counts())

# Criação de um histograma para visualizar a distribuição de preços dos livros.
fig2 = px.histogram(df_books["book price"])

# Função "st.columns" imprime um gráfico ao lado do outro.
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
