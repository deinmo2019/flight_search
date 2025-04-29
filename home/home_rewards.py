import datetime
import time
import mysql.connector
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from amadeus import Client, ResponseError
from streamlit_option_menu import option_menu
from home.amadeusapi import apicr, get_code

mydb = mysql.connector.connect(host='localhost', user='root', password='2023', database='aviationcity')
# create an object to show databases
c = mydb.cursor()

t = str(time.asctime()).split()
mo = t.__getitem__(1)
day = int(t.__getitem__(2))
yr = int(t.__getitem__(4))

col1, col2 = st.columns(2)
img = Image.open('images/rewards_log.jpeg')
col1.image(img, width=50)
st.subheader("REWARDS TRAVELS & TOURS LTD")

#st.image("rewards_log.jpg", caption="REWARDS TRAVELS & TOURS LTD")

def date_():
    t = str(time.asctime()).split()
    dat = f'{t.__getitem__(0)} {t.__getitem__(2)}-{t.__getitem__(1)}-{t.__getitem__(4)} {t.__getitem__(3)}'
    return dat

month = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
#st.write(yr, month.get(mo), day)
mot = month.get(mo)
# 2. horizontal menu w/o custom style
selected = option_menu(menu_title=None,  # required
            options=["Flights", "Hotels"],  # required
            icons=["search", "search", "book", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
if selected == "Flights":
    #st.title(f"{selected} Student")
    
    def search1():
        st.session_state.org = ''
        result = f"{st.session_state.org}"


    col1,col2 = st.columns(2)
    #col1.header(':blue[Search Flight]')
    #st.image("rewards_log.jpg", caption="REWARDS TRAVELS & TOURS LTD")

    htst = "<h3> Search for Flight </h3>"
    st.markdown(htst, unsafe_allow_html=True)


    with st.form(key='columns_in_form'):
        c1, c2 = st.columns(2)
        b1, b2 = st.columns(2)
        fnam = ''
        sna = ''
        adm = ''
        with c1:
            #initialInvestment = st.text_input("Starting capital",value=500)
            st.selectbox('Your Location', get_code(), key="org1")
        with c2:
            st.selectbox('Your Destination', get_code(), key="des")
        with b1:
            st.date_input('departure Date', datetime.date(yr, month.get(mo), day), key = 'ddp')
        with b2:
            st.selectbox('Adults', [1, 2, 3, 4, 5, 6, 7, 8, 9], key = 'adu')
        subm = st.form_submit_button(':green[Search]', on_click=search1)
        if subm:
            orgd = str(st.session_state.org1).split()
            detn = str(st.session_state.des).split()
            dpd = st.session_state.ddp
            adul = st.session_state.adu
            try:
                sdetails = apicr(orgd[0], detn[0], dpd, adul)
                #st.write(f'{detn[0]}')
                
            except ResponseError as error:
                st.warning(error)
                #st.warning(f'Hi no internet connection try connecting to the internet')
            

if selected == "Update":
    st.session_state.fname = ''
    st.session_state.da = ''
    