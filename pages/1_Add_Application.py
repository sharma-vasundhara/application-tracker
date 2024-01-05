import streamlit as st
from functions import connections, load_config

st.set_page_config(layout="wide")


def insert_job_application(
    company_name, job_role_generic, job_title, status,
    application_link, job_description, notes, config
):

    conn = connections.get_connection_details()

    with conn.cursor() as cursor:
        cursor.callproc(config["procedures"]["insert_stored_procedure"], (
                company_name, job_role_generic, job_title, status,
                application_link, job_description, notes
            ))

    connections.close_connection(conn)
    return None


def main():
    st.title("Job Application Streamlit App")
    config = load_config.load_config()

    company_name = st.text_input("Company Name:")
    job_role_generic = st.text_input("Job Role Generic:")
    job_title = st.text_input("Job Title:")
    status = st.text_input("Status:")
    application_link = st.text_input("Application Link:")
    job_description = st.text_area("Job Description:")
    notes = st.text_area("Notes:")

    if st.button("Submit Job Application"):

        insert_job_application(
            company_name, job_role_generic, job_title, status,
            application_link, job_description, notes, config
        )
        st.success("Job application submitted successfully!")


if __name__ == "__main__":
    main()