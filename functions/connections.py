import pymssql
import streamlit as st


def get_connection_details():
    server = st.secrets.db_credentials.server
    database = st.secrets.db_credentials.database
    username = st.secrets.db_credentials.username
    password = st.secrets.db_credentials.password

    # Establish a connection to the Azure SQL Server database
    conn = pymssql.connect(server=server, user=username, password=password, database=database)

    return conn


def close_connection(conn):
    conn.commit()
    conn.close()
    return None