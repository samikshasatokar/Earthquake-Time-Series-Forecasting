import magnitude_data_cleaning
from depth_data_cleaning import *
from prophet import Prophet
import datetime
import streamlit as st
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import mean_squared_error
import numpy as np


df_dep = df_dep.reset_index()

df_dep.head()

#!pip install prophet

df_dep = df_dep.rename(columns={'time':'ds', 'depth':'y'})


df_dep['ds'] = [datetime.datetime.date(d) for d in df_dep['ds']]

#df_dep.head()

def dep_mse_prophet():
    m = Prophet()
    m.fit(df_dep)

    future = m.make_future_dataframe(periods=100)
    forecast = m.predict(future)
    metric_df = forecast.set_index('ds')[['yhat']].join(df_dep.set_index('ds').y).reset_index()

    # metric_df.head()

    # metric_df.isnull().sum()

    metric_df.dropna(inplace=True)

    # metric_df.tail()

    # metric_df.isnull().sum()
    dep_mse_pro = round(mean_squared_error(metric_df.y, metric_df.yhat), 2)
    return dep_mse_pro




