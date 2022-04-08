import streamlit as st

def sources():
    st.header("Sources")
    cola, colb = st.columns(2)
    with cola:
        st.header("Dataset")
        st.write("USGS Earthquake Hazard Program's Earthquake Catalog")

    with colb:
        st.header("Dataset Link")
        st.write("https://earthquake.usgs.gov/earthquakes/search/")

    col1, col2 = st.columns(2)
    with col1:
        st.header("Image")
        st.write("Earthquake")
        st.write("The deadliest Shaanxi(China) Earthquake, 1556.")
        st.write("The deadliest Loma Prieta(San Francisco) Earthquake, 1989.")

    with col2:
        st.header("Source Links")
        st.write("https://bit.ly/3sDSVtG")
        st.write("https://bit.ly/3sDUKa0")
        st.write("https://nbcnews.to/36QGT7A")

def ref():
    st.header("References")
    st.subheader("API Documentations")
    col1, col2 = st.columns(2)
    with col1:
        st.header("API")
        st.write("Auto ARIMA")
        st.write("Matplotlib")
        st.write("Facebook Prophet")
        st.write("Pandas")
        st.write("Plotly Express")
        st.write("Python")
        st.write("Seaborn")
        st.write("Scikit-Learn")
        st.write("Streamlit")

    with col2:
        st.header("Reference Links")
        st.write("https://bit.ly/3Mowpwq")
        st.write("https://bit.ly/35NNqzF")
        st.write("https://bit.ly/371TMvQ")
        st.write("https://bit.ly/3CdGW9g")
        st.write("https://bit.ly/3tt4DGL")
        st.write("https://bit.ly/34hNszm")
        st.write("https://bit.ly/3twtp8D")
        st.write("https://bit.ly/3hHCaao")
        st.write("https://bit.ly/35vdfV5")


def other_links():
    st.header("Other References")
    link1 = '[What were the world’s deadliest earthquakes?](https://ourworldindata.org/the-worlds-deadliest-earthquakes)'
    link2 = '[10 Deadliest Earthquakes in History](https://www.aa.com.tr/en/americas/10-deadliest-earthquakes-in-history/1078343)'
    link3 = '[The 6 Deadliest Earthquakes since 1950](https://www.britannica.com/list/6-deadliest-earthquakes)'
    link4 = '[Link Redirection in Streamlit](https://discuss.streamlit.io/t/a-link-which-will-re-direct-to-another-webpage-in-streamlit/8947)'
    link5 = '[Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)'
    link6 = '[ARIMA Model – Complete Guide to Time Series Forecasting in Python](https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/)'
    link7 = '[Time Series Forecasting With Prophet in Python](https://machinelearningmastery.com/time-series-forecasting-with-prophet-in-python/)'
    link8 = '[Build Your First Data Visualization Web App in Python Using Streamlit](https://towardsdatascience.com/build-your-first-data-visualization-web-app-in-python-using-streamlit-37e4c83a85db)'
    link9 = '[What is time series forecasting?](https://www.influxdata.com/time-series-forecasting-methods/)'
    st.markdown(link1, unsafe_allow_html=True)
    st.markdown(link2, unsafe_allow_html=True)
    st.markdown(link3, unsafe_allow_html=True)
    st.markdown(link4, unsafe_allow_html=True)
    st.markdown(link5, unsafe_allow_html=True)
    st.markdown(link6, unsafe_allow_html=True)
    st.markdown(link7, unsafe_allow_html=True)
    st.markdown(link8, unsafe_allow_html=True)
    st.markdown(link9, unsafe_allow_html=True)



