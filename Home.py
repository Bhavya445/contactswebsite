import streamlit as st
import pandas
st.set_page_config(layout="wide")
st.title("The Best Company")
content="Hi, this is my first website im building on my own. hopefully its fine. blah blah. lets see some members of the company."
st.write(content)
st.subheader("Our Team")
col1,col2,col3=st.columns(3)
rf=pandas.read_csv("data.csv")
with col1:
    for index,row in rf[:4].iterrows():
        st.subheader((row["first name"]+"  "+row["last name"]).title())
        st.write(row["role"])
        st.image("images/"+row["image"])
with col2:
    for index,row in rf[4:8].iterrows():
        st.subheader((row["first name"]+"  "+row["last name"]).title())
        st.write(row["role"])
        st.image("images/"+row["image"])
with col3:
    for index,row in rf[8:].iterrows():
        st.subheader((row["first name"]+"  "+row["last name"]).title())
        st.write(row["role"])
        st.image("images/"+row["image"])


