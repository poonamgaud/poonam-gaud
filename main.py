import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
st.title("Poonam gaud")
st.header("Python")
st.write("MSC DSAi")
df=pd.read_csv("17_Crime_by_place_of_occurrence_2013.csv")

df
st.write(df.head())

# df.tail()
# df.describe()
# df.corr()

# st.bar_chart(sns.barplot(df["RESIDENTIAL PREMISES - Dacoity"].value_counts(), df['HIGHWAYS - Robbery']))
fig=px.bar(x=df["RESIDENTIAL PREMISES - Dacoity"],y=df['STATE/UT'])
st.plotly_chart(fig)
fig=px.line(x=df["RESIDENTIAL PREMISES - Dacoity"],y=df['STATE/UT'])
st.plotly_chart(fig)

fig=px.scatter(df["HIGHWAYS - Dacoity"])
st.plotly_chart(fig)

fig=px.histogram(x=df["RESIDENTIAL PREMISES - Theft"])
st.plotly_chart(fig)
