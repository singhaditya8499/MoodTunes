import streamlit as st
import psycopg2
import json
import matplotlib.pyplot as plt

st.title("MoodTunes")
st.subheader("This page is only a representation. This kind of data will be utilised to make further decisions on recommendations")

db_params = {
    "dbname": "defaultdb",
    "user": "aditya",
    "password": "xxx",
    "host": "xxxx",
    "port": "26257",
}

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    
    # Define Streamlit app

   
    # Execute SQL query to fetch data from the database
    cursor.execute('SELECT * FROM cockroach_example_history')
    data = cursor.fetchall()
    print(data[0])
    cursor.close()
    conn.close()

except Exception as e:
    st.error(f"Error connecting to the database: {str(e)}")
st.set_option('deprecation.showPyplotGlobalUse', False)
def plot_line_graph(data, entity1, entity2, title):
    # Parse the data
    _, date_data, _ = data
    date_data = json.loads(date_data)

    # Extract dates and values for the two entities
    dates = list(date_data.keys())
    values_entity1 = [date_data[date].get(entity1, 0) for date in dates]
    values_entity2 = [date_data[date].get(entity2, 0) for date in dates]

    # Create a line graph
    plt.figure(figsize=(10,6))
    plt.plot(dates, values_entity1, marker='o', label=entity1)
    plt.plot(dates, values_entity2, marker='o', label=entity2)
    plt.title(title)
    plt.xlabel("Dates")
    plt.ylabel("Values")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    st.pyplot()

# Example usage
for i in range(1,len(data)):
    data_ind = data[i]
    entity1 = "196a5924-ed8d-434c-ab1d-820894a908e2"
    entity2 = "1b54b33e-f187-4650-b9f1-822c414cd69d"
    title = "Id of user: " + data_ind[2]
    plot_line_graph(data_ind, entity1, entity2, title)
