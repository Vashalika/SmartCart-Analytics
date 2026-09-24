import sqlite3
import pandas as pd
import streamlit as st


DATABASE_FILE = "smartcart.db"


@st.cache_resource
def get_connection():
    return sqlite3.connect(
        DATABASE_FILE,
        check_same_thread=False
    )


@st.cache_data
def load_products():

    conn = get_connection()

    query = """
    SELECT *
    FROM products
    """

    df = pd.read_sql_query(query, conn)

    return df