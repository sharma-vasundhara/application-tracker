import streamlit as st
from functions import connections, load_config

st.set_page_config(layout="wide")

def fetch_all_job_applications(config):
    # Establish a connection to the Azure SQL Server database
    conn = connections.get_connection_details()

    # Define the SQL query to retrieve all records from JobApplications table


    # Execute the query to fetch all job applications
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute(config["queries"]["all_applications"])
        result = cursor.fetchall()

    # Close the database connection
    connections.close_connection(conn)
    return result


def display_job_applications_table(job_applications):
    # Display the job applications in a table
    st.table(job_applications)

def main():
    st.title("All Job Applications")

    # Load configuration
    config = load_config.load_config()

    # Button to fetch and display all job applications
    if st.button("Fetch All Job Applications"):
        # Call a function to fetch all job applications
        all_job_applications = fetch_all_job_applications(config)

        # Display the job applications in a table
        display_job_applications_table(all_job_applications)

if __name__ == "__main__":
    main()
