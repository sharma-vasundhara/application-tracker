import streamlit as st
from functions import connections, load_config

st.set_page_config(layout="wide", page_title="My Application Journey")


def get_home_page_content(config):
    conn = connections.get_connection_details()
    with conn.cursor() as cursor:
        cursor.callproc(config["queries"]["home_page_content"])

    connections.close_connection(conn)
    return None


def main():
    pass


if __name__ == "__main__":
    main()
