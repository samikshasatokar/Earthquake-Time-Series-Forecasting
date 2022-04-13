import streamlit as st


def quote():
    st.markdown('''
        
                    “Once you have been in an earthquake you know, even if you survive without a scratch, that like a stroke in the heart, it remains in the earth's breast, horribly potential, always promising to return, to hit you again, with an even more devastating force. ”
          
                       ― Salman Rushdie, The Ground Beneath Her Feet
    
    ''')
def theory1():
    st.markdown('''  
         
         The data deviates for every tremor that happened to date as per the figures obtained from various sites such as Pacific Earthquake Engineering Research Center (PEER), Quake Watch, USGS Earthquake Hazards Program, etc...  Thousands are deceased and wounded, million get dislocated, while a notable amount goes missing and stray. Earthquake’s linkage with structural impairment and loss of life keeps on persisting and hence is the focal issue of consideration for numerous domains, such as environmental engineering and seismological analysis. 
         
         Consequently, the effects of an earthquake are devastating and are not confined to loss and damage of living as well as nonliving, but it also causes a substantial portion of transformation, from economic and lifestyle to environment. 
        
        To name a few, Shaanxi( China), Port‑au‑Prince(Haiti), Antakya(Turkey), etc.,  have witnessed many devastating tremors, which resulted in plenty of cessations, structural damage, and economic misfortunes.
        
           ''')


def theory2():
    st.markdown('''  

        Incalculable dollars and careers have been devoted to anticipating where and when the upcoming enormous quake will hit.
        Compared to climate forecasting, which has remarkably enhanced with the benefit of more robust mathematical pinnacles and sounder satellites,  tremor foretelling has been tainted by persistent failures due to exceptionally sceptical conditions of the planet and its surroundings.

        As innovation is advancing and assisting people for a remarkably favourable and suitable way of life, the ability to save a life is explored with the assistance of a quick propelling field of Data Science.

        Essentially, data science tools could be deployed into a perpetual ordeal while reckoning such a vital societal peril issue. The yearning of this work is that the data-driven estimation would furnish better insights into the earthquake affair. 

        Thus, prior notice can help people attempt to safeguard themselves from harm and demise; can lessen damage and monetary adversities, and property can be secured.

           ''')


def home_sidebar():
    st.sidebar.markdown(''' 
            This webapp is designed to give insights about Earthquake events around the world.
            It makes use of Time Series to analyse and forecast the magnitude and depth of the future tremors.
            The data comprises earthquake records for period of one month.
            

            The prototype includes following algorithms for modelling the time series :\n
                
                Facebook Prophet\n
                Long Short-Term Memory Network\n
                Regression\n
                


            Designed by: \n
            **Puja Borole** \n
            **Samiksha Satokar**  ''')

    

    st.sidebar.markdown('''This work is specifically intended for project dissertation and has been published for informational use only.''')


def ts_info():
    st.markdown('''
        Time series forecasting is one of the most applied data science techniques in business, finance, supply chain management, production and inventory planning. 
        Many prediction problems involve a time component and thus require extrapolation of time series data, or time series forecasting. 
        Time series forecasting is also an important area of machine learning (ML) and can be cast as a supervised learning problem. 
        Time series forecasting is a technique for the prediction of events through a sequence of time. 
        It predicts future events by analyzing the trends of the past, on the assumption that future trends will hold similar to historical trends.
    ''')

def prophet_info():
    st.markdown('''
        Prophet is an open-source machine learning algorithm developed by Facebook for producing time-series models that utilize a couple of old thoughts for certain new twists.
        It is a methodology for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, and holiday influences. It works best with time series having vigorous seasonal effects and several seasons of historical data.   
             ''')


def reg_info():
    st.markdown('''
        Regression analysis is a set of statistical methods used for the estimation of relationships between a dependent variable and one or more independent variables. It can be utilized to assess the strength of the relationship between variables and for modelling the future relationship between them.
            ''')

def lstm_info():
    st.markdown('''
        The Long Short-Term Memory network, or LSTM network, is a recurrent neural network that is trained using Backpropagation Through Time and overcomes the vanishing gradient problem.

        As such, it can be used to create large recurrent networks that in turn can be used to address difficult sequence problems in machine learning and achieve state-of-the-art results.
            ''')

def compare_info():
    st.subheader("Comparing Machine Learning Algorithms")
    st.markdown('''
            Comparing machine learning algorithms is an important task in itself to accomplish goals such as better performance, easier retraining, speedy production, etc...
            The comparable parameter used in this work is the Mean Squared Error, which measures the average of the squares of the errors or deviations, i.e. the difference between the estimated and true value. 
            It aids in imposing higher weights on outliers, thus reducing the issue of overfitting.  
            
    ''')


