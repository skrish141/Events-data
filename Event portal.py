import streamlit as st
import pandas as pd
import numpy as np
import requests
import csv
import time
import base64
timestr = time.strftime("%Y%m%d-%H%M%S")







st.title("Upcoming events Data")

dataset_name = st.sidebar.selectbox("Select Country", ('Germany', 'France', 'Italy', 'The Netherlands', 'Switzerland', 'Poland', 'Greece', 'Sweden', 'Austria', 'Spain', 'Russia', 'China', 'India', 'Australia', 'Malaysia', 'Japan', 'South Korea', 'United Arab Emirates', 'Turkey', 'Brazil', 'United States of America', 'Canada', 'Mexico'))

if dataset_name == 'Germany':

    st.subheader("""
    Explore upcoming Events in Germany
    """)
    df = pd.read_csv("Germany.csv")
    st.dataframe(df)


    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Germany.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)


elif dataset_name == 'France':
    st.subheader("""
    Explore Upcoming Events in France""")
    df = pd.read_csv("France.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in France.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'Italy':
    st.subheader("""
    Explore Upcoming Events in Italy""")
    df = pd.read_csv("Italy.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Italy.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'The Netherlands':
    st.subheader("""
    Explore Upcoming Events in The Netherlands""")
    df = pd.read_csv("Netherlands.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in The Netherlands.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'Switzerland':
    st.subheader("""
    Explore Upcoming Events in Switzerland""")
    df = pd.read_csv("Switzerland.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Switzerland.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'Poland':
    st.subheader("""
    Explore Upcoming Events in Poland""")
    df = pd.read_csv("Poland.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Poland.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'Greece':
    st.subheader("""
    Explore Upcoming Events in Greece""")
    df = pd.read_csv("Greece.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Greece.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'Sweden':
    st.subheader("""
    Explore Upcoming Events in Sweden""")
    df = pd.read_csv("Sweden.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Sweden.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'Austria':
    st.subheader("""
    Explore Upcoming Events in Austria""")
    df = pd.read_csv("Austria.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Austria.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)


elif dataset_name == 'Spain':
    st.subheader("""
    Explore Upcoming Events in Spain""")
    df = pd.read_csv("Spain.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Spain.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'Russia':
    st.subheader("""
    Explore Upcoming Events in Russia""")
    df = pd.read_csv("Russia.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Russia.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'China':
    st.subheader("""
    Explore Upcoming Events in China""")
    df = pd.read_csv("China.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in China.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'India':
    st.subheader("""
    Explore Upcoming Events in India""")
    df = pd.read_csv("India.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in India.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)


elif dataset_name == 'Australia':
    st.subheader("""
    Explore Upcoming Events in Australia""")
    df = pd.read_csv("Australia.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Australia.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)


elif dataset_name == 'Malaysia':
    st.subheader("""
    Explore Upcoming Events in Malaysia""")
    df = pd.read_csv("Malaysia.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Malaysia.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'Japan':
    st.subheader("""
    Explore Upcoming Events in Japan""")
    df = pd.read_csv("Japan.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Japan.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'South Korea':
    st.subheader("""
    Explore Upcoming Events in South Korea""")
    df = pd.read_csv("South_korea.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in South Korea.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)


elif dataset_name == 'United Arab Emirates':
    st.subheader("""
    Explore Upcoming Events in United Arab Emirates""")
    df = pd.read_csv("U.A.E.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in UAE.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'Turkey':
    st.subheader("""
     Explore Upcoming Events in Turkey""")
    df = pd.read_csv("Turkey.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Turkey.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'Brazil':
    st.subheader("""
    Explore Upcoming Events in Brazil""")
    df = pd.read_csv("Brazil.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Brazil.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'Canada':
    st.subheader("""
    Explore Upcoming Events in Canada""")
    df = pd.read_csv("Canada.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Canada.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)

elif dataset_name == 'Mexico':
    st.subheader("""
    Explore Upcoming Events in Mexico""")
    df = pd.read_csv("Mexico.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in Mexico.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)


elif dataset_name == 'United States of America':
    st.subheader("""
    Explore Upcoming Events in United States of America""")
    df = pd.read_csv("Events_USA.csv")
    st.dataframe(df)
    def csv_downloader(data):
        csvfile = data.to_csv()
        b64 = base64.b64encode(csvfile.encode()).decode()
        new_filename = "Upcoming Events in USA.csv".format(timestr)
        st.markdown("#### Download File ####")
        href = f'<a href="data:file/csv;base64, {b64}" download = "{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)
    csv_downloader(df)







