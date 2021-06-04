import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.write("""
# SVM implementation app
 """)

data = {'City_1':(np.random.randint(low=30, high=40, size=12)),
        'City_2':(np.random.randint(low=25, high=38, size=12)),
        'City_3':(np.random.randint(low=20, high=40, size=12))}
df = pd.DataFrame(data,index = ['January','February','March','April','May','June','July','August','September','October','November','December'])
st.dataframe(df)
# Text Input
age = st.text_input("Enter the Age", )
salary = st.text_input("Enter the Salary: (Salary in Rupees)")
gender = st.text_input("Enter the Gender: (1-Male,0-Female)")
submit = st.button("Classify")
