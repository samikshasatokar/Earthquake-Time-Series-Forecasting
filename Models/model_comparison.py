import pandas as pd
from mag_prophet_error import *
from dep_lstm_error import *
from dep_prophet_error import *
from mag_lstm_error import *
from mag_reg_error import *
from dep_reg_error import *

def compare_mag_models():
    mag_mse_pro = mag_mse_prophet()
    mag_mse_ls = mag_mse_lstm()
    mag_reg_key, mag_mse_re = mag_mse_reg()

    mag_data = [['Facebook Prophet', mag_mse_pro], ['Long Short-Term Memory Network', mag_mse_ls], [mag_reg_key, mag_mse_re]]
    mag_comp_df = pd.DataFrame(mag_data, columns=['Algorithm', 'Mean Squared Error'])
    st.table(mag_comp_df)
    fig = px.line(mag_comp_df, x="Algorithm", y="Mean Squared Error", title='Comparison of Algorithms',
                  template="plotly_dark")
    st.plotly_chart(fig)
    mag_comp_dict = {'Facebook Prophet': mag_mse_pro, 'Long Short-Term Memory Network': mag_mse_ls,
                     mag_reg_key: mag_mse_re}
    best_mag_model = min(mag_comp_dict, key=mag_comp_dict.get)
    mag_min_mse = min(mag_comp_dict.keys(), key=(lambda x: mag_comp_dict[x]))
    st.write(
        best_mag_model + " appears to be the best model producing the lowest mean squared error value of",
        mag_comp_dict[mag_min_mse])

def compare_dep_models():
    dep_mse_pro = dep_mse_prophet()
    dep_mse_ls = dep_mse_lstm()
    dep_reg_key, dep_mse_re = dep_mse_reg()
    data = [['Facebook Prophet', dep_mse_pro], ['Long Short-Term Memory Network', dep_mse_ls], [dep_reg_key, dep_mse_re]]
    dep_comp_df = pd.DataFrame(data, columns=['Algorithm', 'Mean Squared Error'])
    st.table(dep_comp_df)
    fig = px.line(dep_comp_df, x="Algorithm", y="Mean Squared Error", title='Comparison of Algorithms',
                  template="plotly_dark")
    st.plotly_chart(fig)
    dep_comp_dict = {'Facebook Prophet': dep_mse_pro, 'Long Short-Term Memory Network': dep_mse_ls,
                     dep_reg_key: dep_mse_re}
    best_dep_model = min(dep_comp_dict, key=dep_comp_dict.get)
    dep_min_mse = min(dep_comp_dict.keys(), key=(lambda x: dep_comp_dict[x]))
    st.write(
        best_dep_model + " appears to be the best model producing the lowest mean squared error value of",
        dep_comp_dict[dep_min_mse])
