import pandas as pd
import streamlit as st


# df = pd.DataFrame({
#     'Name': ['Arianita', 'Festa','Gresa'],
#     'Age': [23, 23, 21],
#     'City': ['Pristine', 'Prizren', 'Vushtrri']
# })
#
# df

books_df = pd.read_cvs('eda-amazon-top-50-bestselling-books.ipynb')

st.title("Bestselling books in amazon")
st.write("This app analyzes the amazon top selling books")

st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name']
avg_rating = books_df['User Rating']
avg_price = books_df['Price']

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total books", total_books)
col2.metric("Unique titles", unique_titles)
col3.metric("Average Rating", avg_rating)
col4.metric("Average Price", avg_price)

st.subheader("Dataset Preview")
st.write(books_df.head())
