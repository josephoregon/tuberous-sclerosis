"""
@Author: Joseph Rosas ꐠ
Create Date: Apr. 14st 2021
"""

import streamlit as st

from functions import read_markdown_file

st.set_page_config(
    page_title='For Maui.',
    layout='centered',
    page_icon='🔬'
)

# TITLE & INFO
st.title("Tuberous Sclerosis—Nutritional Assistance ☤")
st.write('_Research dedicated to my son, Maui ꐠ — and others affected by TS._')
st.markdown("[_by Joseph Rosas, Data Scientist_]" "(https://www.linkedin.com/in/josephrosas/)")

# intro_markdown = read_markdown_file("info.md")
# st.markdown(intro_markdown, unsafe_allow_html=True)

# HARD CODED LISTS
nutrient_list = ['B Vitamins', 'Vitamin D', 'Magnesium', 'Omega-3']
signs_list = ['Seizures', 'Cognitive Disabilities',
              'Behavior Problems', 'Skin Abnormalities',
              'Kidney Problems', 'Lung Lesions']

# SIDEBAR INPUTS
nutrient_input = st.sidebar.multiselect('Nutrients', nutrient_list)
effect_input = st.sidebar.multiselect('Signs & Symptoms', signs_list)

st.markdown("---")
