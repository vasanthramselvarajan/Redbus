import streamlit as st
import pymysql
import pandas as pd
import numpy as np

# Establish a connection to the MySQL database
def get_connection():
    return pymysql.connect(host='127.0.0.1',user='root',password='admin2212',database='redbus')

# Load data from the selected table
def load_data(table_name):
    connection = get_connection()
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df

data=["Home","Redbus project","Last page"]
page = st.sidebar.selectbox("welcome...!!",data)

if page=="Home":
    st.header("Redbus scraping")
    st.image('C:/Users/HP/Downloads/redbus-logo.jpng.webp',width=300)
    st.write('To visit the site click redbus below:')
    st.markdown('[redbus](https://www.redbus.in/)')
    # Streamlit header
    
    st.markdown('''
### In this project
*Initially, I scraped data from the redbus.in website using Selenium to automate the extraction of bus-related information from 10 different states.
Once the data was collected, I stored it in an MySQL database for storage and retrieval.
 Finally, I displayed the data using Streamlit to create an interactive and user-friendly web application, allowing for dynamic querying and visualization of bus schedules and fares.*
''')
    

elif page=="Redbus project":
    # State selection
    table_name = st.selectbox(
        "Select a State",
        ('andhra_pradesh', 'assam', 'bihar', 'chandigarh', 'himachal_pradesh', 'kerala', 'rajasthan', 'south_bengal', 'telangana', 'utter_pradesh'))
    st.success(f"{table_name} state has been selected")
    # Load data based on the selected table
    df = load_data(table_name)
    df['departure'] = pd.to_datetime(df['departure'], format='%H:%M').dt.time
    df['arrival'] = pd.to_datetime(df['arrival'], format='%H:%M').dt.time
    df['busfare']=df['busfare'].astype(float)

    # filter heading
    st.subheader("Filter")
    if st.checkbox('All buses'):
        st.dataframe(df)

    if st.checkbox('filter'):
        if not df.empty and 'busroute' in df.columns:
            #tuple of all routes
            routes = df['busroute'].unique().tolist()
            #dropbox for routes
            route_name = st.multiselect(
            "Route name",
            routes)
        if route_name:
            route_filter = df[df['busroute'].isin(route_name)]
            st.write("All buses from :")
            for i in route_name:
                st.write(i)
        else:
            route_filter = df 

        min_time=min(df["departure"])
        max_time=max(df["departure"])
        time = st.slider(
        "Choose time",
        value=min_time,
        min_value=min_time,
        max_value=max_time,
        format="HH:mm")
        st.success(f"buses after {time}")

        max_price=max(df["busfare"])
        fare=st.number_input(f"buses above price",min_value=0.0,max_value=max_price,step=50.0)
        st.success(f"buses above price {fare}")

        rating=st.number_input(f"buses above rating",min_value=0.0,max_value=5.0,step=0.5)
        st.success(f"buses above rating {rating}")

        result=route_filter[(route_filter["departure"]>=time) & (route_filter["busfare"]>=int(fare)) & (route_filter["busrating"]>=rating)]
        st.dataframe(result)

else:
    st.markdown('''
### skills
''')
    st.write("python")
    st.write("mysql")
    st.write("selenium")
    st.write("streamlit")





















