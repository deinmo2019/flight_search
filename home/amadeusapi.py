from amadeus import Client, ResponseError
import mysql.connector
import streamlit as st
import pandas as pd
import numpy as np
mydb = mysql.connector.connect(
    host=st.secrets["host"], 
    user=st.secrets["user"], 
    password=st.secrets["password"], 
    database=st.secrets["database"]
    )
# create an object to show databases
c = mydb.cursor()

amadeus = Client(
    client_id=st.secrets["client_id"],
    client_secret=st.secrets["client_secret"]
)

try:
    def apicr(ord, des, depd, adult):
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=ord,
            destinationLocationCode=des,
            departureDate=depd,
            adults=adult,
            max=7)
        #response1 = amadeus.reference_data.airlines.get(airlineCodes='BA')
        body = {
        "originDestinations": [
            {
                "id": "1",
                "originLocationCode": ord,
                "destinationLocationCode": des,
                "departureDateTime": {
                    "date": "2025-01-21"
                }
            }
        ],
        "travelers": [
            {
                "id": "1",
                "travelerType": "ADULT"
            }
        ],
        "sources": [
            "GDS"
        ]
    }
        #response2 = amadeus.shopping.availability.flight_availabilities.post(body)
        #st.write(response.data)
        #response2 = amadeus.shopping.flight_dates.get(origin=ord, destination=des)
        #print(response.data)
        df = pd.DataFrame(response.data)
        st.dataframe(df)
        #df2 = pd.DataFrame(response2.data)
        #for da in response.data:
        #da = response.data
        #st.write(da[0])
        dataN = response.data
        st.write(dataN)
        #for da in dataN:
         #   st.write(da["itineraries"])
except ResponseError as error:
    st.write(error)

def get_code():
    d = []
    c.execute('SELECT IATA, CITY, COUNTRY FROM airportcity')
    data = c.fetchall()
    for da in data:
        da1 = f'{da[0]} {da[1]} {da[2]}'
        d.append(da1)
    return d
