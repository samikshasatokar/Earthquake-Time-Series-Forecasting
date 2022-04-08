import streamlit as st

def readme_1():
    st.header("World's Deadliest Tremors")

    st.markdown('*****Sumatra, Indonesia – 2004*****')
    col1, col2 = st.columns(2)
    col1.metric("Magnitude", "9.1")
    col2.metric("Estimated Death Toll", "227,899")

    st.markdown('***Gansu, China – 1920***')
    col1, col2 = st.columns(2)
    col1.metric("Magnitude", "8.3")
    col2.metric("Estimated Death Toll", "200,000")

    st.markdown('***Shaanxi, China – 1556***')
    col1, col2 = st.columns(2)
    col1.metric("Magnitude", "8")
    col2.metric("Estimated Death Toll", "830,000")

    st.markdown('***Kashmir, India – 2005***')
    col1, col2 = st.columns(2)
    col1.metric("Magnitude", "7.6")
    col2.metric("Estimated Death Toll", "79,000")

    st.markdown('***Port-au-Prince, Haiti – 2010***')
    col1, col2 = st.columns(2)
    col1.metric("Magnitude", "7")
    col2.metric("Estimated Death Toll", "316,000")
