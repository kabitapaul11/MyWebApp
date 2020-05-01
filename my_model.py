import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import pickle

# Load csv file.
df_day = pd.read_csv('inputfile/day.csv')


# create add_label function
def add_label(df):
    if df.calories <= 160 and df.fiber >=3 and df.sugars <=4:
        return 1 # healthy cereal
    else:
        return 0 #not healthy cereal


def predict(df)
    
    ### Number of casual riders
    X = df_day.drop(columns =['casual', 'registered', 'cnt','dteday','instant'])
    y = df_day[['casual']]
    #do a train test split, use test_size =0.3
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state= 1)
    #initialize your linear regression model
    lnr = LinearRegression()
    #fit training set to your LR model
    lnr = lnr.fit(X_train, y_train)
    #predict on the test set using your model
    y_pred = lnr.predict(X_test)
    # serialize model to disk
    pickle.dump(lnr,open('outputfiles/rf_model.pk1','wb'))
    return y_pred