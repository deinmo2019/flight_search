import streamlit as st
from streamlit_option_menu import option_menu

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
#st.logo("image/logo.jpg")
image = "image/rewards_log.png"
#st.logo(image)
EXAMPLE_NO = 1

student_page = st.Page(
    "home/home_rewards.py",
    title='Home',
    icon=":material/home:",
    default=True
)

with st.sidebar:
    #pg= st.navigation(pages=[student_page, nursery_page, primary_page, secondary_page])
    pg= st.navigation(
        {
            "info": [student_page],
            #"Levels": [student_page],
        }
    )

pg.run()

