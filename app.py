import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf  # Use yfinance instead of pandas_datareader
import keras.model import load_model
import streamlit as st

# Define start and end dates
start = '2010-01-01'
end = '2023-12-31'

st.title('Stock Trend Prediction')

user_input = st.text_input('Enter Stock Ticker', 'AAPL')
# Get data for Apple (AAPL) from Yahoo Finance
df = yf.download('user_input', start=start, end=end)  # Using yfinance's download function

# Describing Data
st.subheader('Data from 2010-2023')
st.write(df.describe())