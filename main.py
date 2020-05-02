from flask import Flask, render_template, request, url_for
import random
import pickle
import pandas as pd
from my_model import Predict_rider

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def predict():
    # unpickle model for use
    # model = pickle.load(open('outputfiles/rf_model.pk1','rb'))

    # the random forest model use a list of features to predict whether cereal is healthy or not. 
    # We don't want to ask users to input values for all these values. so we will randomly generate values for some of the features.
    # the front end will ask users to input values for calories, fiber and sugar in grams for their cereal.

    mnth = random.uniform(1,12)
    yr =  random.uniform(0,1)
    weekday = random.uniform(0,6)
    workingday= random.uniform(0,1)

    #dictionary for df1
    dict_1 ={'mnth':mnth,'yr':yr,'weekday':weekday,'workingday':workingday}

    #add values to dataframe
    df1= pd.DataFrame(dict_1, index=[0])


    if request.method == 'POST':
        mnth = request.form['mnth']
        yr = request.form['yr']
        weekday = request.form['weekday']
        season = request.form['season']
        holiday = request.form['holiday']
        workingday = request.form['workingday']

        dict_2 = {'mnth':mnth,'yr':yr,'weekday':weekday,'season':season,'holiday': holiday,'workingday':workingday,
        'temp': 0.34 ,'weathersit':2,'atemp':0.37,'hum': 0.37,'windspeed':0.1}
        df2= pd.DataFrame(dict_2,index=[0])
        data = pd.concat([df2,df1], axis=1)
        my_prediction = Predict_rider(df2)
    return render_template('results.html', prediction=my_prediction, comment='')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
