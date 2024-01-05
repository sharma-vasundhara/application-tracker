import streamlit as st
from functions import connections, load_config

st.set_page_config(layout="wide")


def fetch_all_job_applications(config):
    conn = connections.get_connection_details()

    with conn.cursor(as_dict=True) as cursor:
        cursor.execute(config["queries"]["all_applications"])
        result = cursor.fetchall()

    connections.close_connection(conn)
    return result


def display_job_applications_table(job_applications):
    st.table(job_applications)


def main():
    st.title("All Job Applications")
    config = load_config.load_config()
    if st.button("Fetch All Job Applications"):
        all_job_applications = fetch_all_job_applications(config)
        display_job_applications_table(all_job_applications)


if __name__ == "__main__":
    main()
