import streamlit as st
from functions import connections, load_config

st.set_page_config(layout="wide")


def update_job_application_status(job_id, new_status, config):
    conn = connections.get_connection_details()

    with conn.cursor() as cursor:
        cursor.callproc(config["procedures"]["update_stored_procedure"], (job_id, new_status))

    connections.close_connection(conn)
    return None


def search_job_applications_by_role(search_string, config):
    conn = connections.get_connection_details()

    query = config["queries"]["matching_jobs"]

    with conn.cursor(as_dict=True) as cursor:
        cursor.execute(query.replace("<identifier>", search_string.lower()))
        result = cursor.fetchall()

    connections.close_connection(conn)
    return result


if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


def main():
    st.title("Update Job Application Status")
    config = load_config.load_config()

    search_string = st.text_input("Enter Job Role Search String:")
    search_button = st.button("Search Job Applications", key=1001, on_click=click_button())
    if st.session_state.clicked:
        matching_records = search_job_applications_by_role(search_string, config)
        st.table(matching_records)

        record_ids = [record["Id"] for record in matching_records]
        job_roles = [f"{record['Id']} - {record['JobTitle']}" for record in matching_records]

        selected_record_index = st.selectbox("Select a Record:", job_roles, placeholder="None")
        selected_record_id = record_ids[job_roles.index(selected_record_index)]
        new_status = st.text_input("Enter New Status:")

        update_button = st.button("Update Job Status", key=1002, on_click=click_button())
        if update_button:
            if new_status is not None and new_status != "":
                update_job_application_status(selected_record_id, new_status, config)
                st.success(f"Job status updated to {new_status} for Application ID {selected_record_id} successfully!")


if __name__ == "__main__":
    main()