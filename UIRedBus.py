# importing libraries
import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time

# Chandigarh bus
lists_CH=[]
df_CH=pd.read_csv("CH_routes_detail.csv")
for i,r in df_CH.iterrows():
    lists_CH.append(r["route"])

#UP bus
lists_UP=[]
df_UP=pd.read_csv("UP_routes_detail.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["route"])

#Bihar bus
lists_BH=[]
df_BH=pd.read_csv("BH_routes_detail.csv")
for i,r in df_BH.iterrows():
    lists_BH.append(r["route"])

#West bengal bus
lists_WB=[]
df_WB=pd.read_csv("WB_routes_detail.csv")
for i,r in df_WB.iterrows():
    lists_WB.append(r["route"])

#Punjab bus
lists_PB=[]
df_PB=pd.read_csv("PB_routes_detail.csv")
for i,r in df_PB.iterrows():
    lists_PB.append(r["route"])


# Rajasthan bus 
lists_RJ=[]
df_RJ=pd.read_csv("RJ_routes_detail.csv")
for i,r in df_RJ.iterrows():
    lists_RJ.append(r["route"])

# Himachal Pradesh bus
lists_HM=[]
df_HM=pd.read_csv("HM_routes_detail.csv")
for i,r in df_HM.iterrows():
    lists_HM.append(r["route"])

#Assam bus
lists_AS=[]
df_AS=pd.read_csv("AS_routes_detail.csv")
for i,r in df_AS.iterrows():
    lists_AS.append(r["route"])

#Sikkim bus
lists_SK=[]
df_SK=pd.read_csv("SK_routes_detail.csv")
for i,r in df_SK.iterrows():
    lists_SK.append(r["route"])

#Megalaya bus
lists_MG=[]
df_MG=pd.read_csv("MG_routes_detail.csv")
for i,r in df_MG.iterrows():
    lists_MG.append(r["route"])

#setting up streamlit page
slt.set_page_config(layout="wide")

web=option_menu(menu_title="🚌OnlineBus",
                options=["Home","📍States and Routes"],
                icons=["house","info-circle"],
                orientation="horizontal"
              )

def type_and_fare_T(bus_type, fare_range, route_name):
        conn = mysql.connector.connect(host="localhost", user="root", password="Rn@9867908494", database="RED_Final_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000  

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_details 
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{route_name}"
            AND {bus_type_condition} AND Start_time>='{TIME}'
            ORDER BY Price and Start_time DESC
        '''
        my_cursor.execute(query)
        out = my_cursor.fetchall()
        conn.close()

        print(out)
        df = pd.DataFrame(out, columns=[
            "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
            "Price", "Seats_Available", "Ratings", "Route_link", "Route_name", "State"
            ])
        return df
     
# Home page setting
if web=="Home":
    #slt.image("t_500x300.jpg",width=200)
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":Red[Domain:]  Transportation")
    slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.")
    slt.subheader(":Red[Overview:]") 
    slt.markdown("Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages, to collect the desired data...")
    slt.markdown('''Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
                    Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis.''')
    slt.markdown('''MySQL: With help of SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
                    and the data was efficiently inserted into relevant tables for storage and retrieval.''')
    slt.markdown("Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
    slt.subheader(":Red[Skill-take:]")

# States and Routes page setting
if web == "📍States and Routes":
    S = slt.selectbox("Lists of States", ["Chandigarh", "Uttar Pradesh", "Bihar", "West Bengal", "Punjab", 
                                          "Rajasthan", "Himachal Pradesh", "Assam", "Sikkim", "Megalaya"])
    
    col1,col2=slt.columns(2)
    with col1:
        select_type = slt.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
    with col2:
        select_fare = slt.radio("Choose bus fare range", ("50-1000", "1000-2000", "2000 and above"))
    TIME=slt.time_input("select the time")

    # Chandigarh bus fare filtering
    if S == "Chandigarh":
        CH = slt.selectbox("List of routes",lists_CH)

        df_result = type_and_fare_T(select_type, select_fare, CH)
        slt.dataframe(df_result)

    # UP bus fare filtering
    if S=="Uttar Pradesh":
        UP=slt.selectbox("list of routes",lists_UP)

        df_result = type_and_fare_T(select_type, select_fare, UP)
        slt.dataframe(df_result)
          

    # Bihar bus fare filtering
    if S=="Bihar":
        BH=slt.selectbox("list of routes",lists_BH)

        df_result = type_and_fare_T(select_type, select_fare, BH)
        slt.dataframe(df_result)

    # WB bus fare filtering
    if S=="West Bengal":
        WB=slt.selectbox("list of routes",lists_WB)
        
        df_result = type_and_fare_T(select_type, select_fare, WB)
        slt.dataframe(df_result)

    # Punjab bus fare filtering
    if S=="Punjab":
        PB=slt.selectbox("list of routes",lists_PB)

        df_result = type_and_fare_T(select_type, select_fare, PB)
        slt.dataframe(df_result)
          

    # Rajasthan bus fare filtering       
    if S=="Rajasthan":
        RJ=slt.selectbox("list of rotes",lists_RJ)

        df_result = type_and_fare_T(select_type, select_fare, RJ)
        slt.dataframe(df_result)
    
    # Himachal Pradesh bus fare filtering
    if S=="Himachal Pradesh":
        HM=slt.selectbox("list of rotes",lists_HM)

        df_result = type_and_fare_T(select_type, select_fare, HM)
        slt.dataframe(df_result)


    # Assam bus fare filtering
    if S=="Assam":
        AS=slt.selectbox("list of rotes",lists_AS)

        df_result = type_and_fare_T(select_type, select_fare, AS)
        slt.dataframe(df_result)

    # Sikkim bus fare filtering
    if S=="Sikkim":
        SK=slt.selectbox("list of rotes",lists_SK)

        df_result = type_and_fare_T(select_type, select_fare, SK)
        slt.dataframe(df_result)

    # Megalaya bus fare filtering
    if S=="Megalaya":
        MG=slt.selectbox("list of rotes",lists_MG)

        df_result = type_and_fare_T(select_type, select_fare, MG)
        slt.dataframe(df_result)



