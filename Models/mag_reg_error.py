import magnitude_data_cleaning
import matplotlib.pyplot as plt
import seaborn as s
import pandas as pd
import plotly.express as px
import streamlit as st
from magnitude_data_cleaning import *
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
import xgboost
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error


def mag_mse_reg():
    """# Time Series as Regression of Lag values"""

    df['lag1'] = df['mag'].shift(1)
    df['lag2'] = df['mag'].shift(2)
    df['lag3'] = df['mag'].shift(3)
    df['lag4'] = df['mag'].shift(4)
    df['lag5'] = df['mag'].shift(5)

    # df.columns

    lag_df = df.dropna()

    # lag_df.shape

    lag_df = lag_df[['mag', 'lag1', 'lag2', 'lag3', 'lag4', 'lag5']]

    # lag_df.shape

    """# X & Y Split

    """

    X = lag_df.drop("mag", axis=1)
    Y = lag_df['mag']

    # X.shape,Y.shape

    """# Train Test Split"""

    # train size 90%
    train_size = int(0.9 * lag_df['mag'].shape[0])

    X_train = X.iloc[:train_size, :]
    X_test = X.iloc[train_size:, :]
    Y_train = Y.iloc[:train_size]
    Y_test = Y.iloc[train_size:]

    # X_train.shape,X_test.shape,Y_train.shape,Y_test.shape

    """# Apply Regression"""

    lr = LinearRegression()
    svr = SVR()
    dtr = DecisionTreeRegressor()
    rfr = RandomForestRegressor()
    abr = AdaBoostRegressor()
    xbr = XGBRegressor()

    lr.fit(X_train, Y_train)
    svr.fit(X_train, Y_train)
    dtr.fit(X_train, Y_train)
    rfr.fit(X_train, Y_train)
    abr.fit(X_train, Y_train)
    xbr.fit(X_train, Y_train)

    Y_pred_lr = lr.predict(X_test)
    Y_pred_svr = svr.predict(X_test)
    Y_pred_dtr = dtr.predict(X_test)
    Y_pred_rfr = rfr.predict(X_test)
    Y_pred_abr = abr.predict(X_test)
    Y_pred_xbr = xbr.predict(X_test)

    mse_lr = (mean_squared_error(Y_test.values, Y_pred_lr))
    mse_svr = (mean_squared_error(Y_test.values, Y_pred_svr))
    mse_dtr = (mean_squared_error(Y_test.values, Y_pred_dtr))
    mse_rfr = (mean_squared_error(Y_test.values, Y_pred_rfr))
    mse_abr = (mean_squared_error(Y_test.values, Y_pred_abr))
    mse_xbr = (mean_squared_error(Y_test.values, Y_pred_xbr))

    data = [['LinearRegression', mse_lr], ['Support Vector Regressor', mse_svr], ['DecisionTreeRegressor', mse_dtr],
            ['RandomForestRegressor', mse_rfr], ['AdaBoostRegressor', mse_abr], ['XGBRegressor', mse_xbr]]
    reg_df = pd.DataFrame(data, columns=['Regression Algorithm', 'Mean Square Error'])
    #st.table(reg_df)


    mag_reg_dict = {'LinearRegressor': mse_lr, 'Support Vector Regressor': mse_svr, 'DecisionTreeRegressor': mse_dtr,
                    'RandomForestRegressor': mse_rfr, 'AdaBoostRegressor': mse_abr, 'XGBRegressor': mse_xbr}
    mag_key_min = min(mag_reg_dict,
                      key=mag_reg_dict.get)  # https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
    val_min = min(mag_reg_dict.keys(), key=(lambda x: mag_reg_dict[x]))

    mag_reg_key = mag_key_min
    mag_mse_re = round(mag_reg_dict[val_min], 2)
    return mag_reg_key, mag_mse_re



