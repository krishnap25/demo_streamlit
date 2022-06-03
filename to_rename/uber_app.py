import streamlit as st
import pandas as pd
import numpy as np

# Demo available at https://docs.streamlit.io/library/get-started/create-an-app
# Just giving a quick tour of it here

st.title('Uber pickups in NYC')

# Load the data, can use @st.cache to keep in memory the output of this function for the same input
# @st.cache
def load_data(nrows):
    data = pd.read_csv('https://s3-us-west-2.amazonaws.com/'
                       'streamlit-demo-data/uber-raw-data-sep14.csv.gz', nrows=nrows)
    data['Date/Time'] = pd.to_datetime(data['Date/Time'])
    return data


data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done!")

# Whether to show the whole data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Show the number of pickups by hour (static)
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data['Date/Time'].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Select an hour to filter the data
hour_to_filter = st.slider('Hour', 0, 23, 17)
filtered_data = data[data['Date/Time'].dt.hour == hour_to_filter]

# Display the pick-ups on a map
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# (Needs keys of dataframe to be lowercase...)
lowercase = lambda x: str(x).lower()
to_plot = filtered_data.rename(lowercase, axis='columns')
st.map(to_plot)
