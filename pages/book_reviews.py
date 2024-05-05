import streamlit as st
import pandas as pd

# Configuração da página para um layout amplo
st.set_page_config(layout="wide")

# Leitura dos dados das planilhas Excel
df_reviews = pd.read_excel("C:\\Users\\Ander\\OneDrive\\Área de Trabalho\\datasets\\customer-reviews.xlsx")
df_top100_books = pd.read_excel("C:/Users/Ander/OneDrive/Área de Trabalho/datasets/Top-100-Trending-Books.xlsx")

# Extração dos nomes únicos dos livros
books = df_top100_books["book title"].unique()

# Seleção do livro através de um seletor na barra lateral
book = st.sidebar.selectbox("Livros", books)

# Filtragem do DataFrame para exibir informações do livro selecionado
df_book = df_top100_books[df_top100_books["book title"] == book]

# Filtro das revisões para o livro selecionado
df_reviews_f = df_reviews[df_reviews["book name"] == book]

# Extrair informações específicas do livro selecionado
book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

# Exibição do título do livro
st.title(book_title)
# Exibição da avaliação do livro
st.subheader(book_rating)

# Exibição de informações do livro em formato de métricas
col1, col2, col3 = st.columns(3)
col1.metric("Preço", book_price)
col2.metric("Avaliação", book_rating)
col3.metric("Ano de Publicação", book_year)

# Adicionar uma linha divisória
st.divider()

# Exibição das revisões para o livro selecionado
for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])

# Exibição das informações do livro
df_book




