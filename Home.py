import streamlit as st
from functions import connections, load_config

st.set_page_config(layout="wide", page_title="My Application Journey", page_icon=":briefcase:")


def main():
    st.image("images/app-header.jpg", caption="***", use_column_width=True)


if __name__ == "__main__":
    main()
