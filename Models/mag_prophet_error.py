import magnitude_data_cleaning
from magnitude_data_cleaning import *
from prophet import Prophet
from sklearn.metrics import mean_squared_error
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow import keras



df_mag = df_mag.reset_index()

df_mag.head()

df_mag = df_mag.rename(columns={'time':'ds', 'mag':'y'})

import datetime
df_mag['ds'] = [datetime.datetime.date(d) for d in df_mag['ds']]

df_mag.head()



def mag_mse_prophet():
    m = Prophet()
    m.fit(df_mag)

    future = m.make_future_dataframe(periods=100)
    forecast = m.predict(future)
    metric_df = forecast.set_index('ds')[['yhat']].join(df_mag.set_index('ds').y).reset_index()

    # metric_df.head()

    # metric_df.isnull().sum()

    metric_df.dropna(inplace=True)

    # metric_df.tail()

    # metric_df.isnull().sum()

    mag_mse_pro = round(mean_squared_error(metric_df.y, metric_df.yhat), 2)
    return mag_mse_pro







