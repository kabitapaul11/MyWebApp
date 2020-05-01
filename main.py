from flask import Flask, render_template, request, url_for
import random
import pickle
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def predict():
    # unpickle model for use
    model = pickle.load(open('outputfiles/rf_model.pk1','rb'))

    # the random forest model use a list of features to predict whether cereal is healthy or not. 
    # We don't want to ask users to input values for all these values. so we will randomly generate values for some of the features.
    # the front end will ask users to input values for calories, fiber and sugar in grams for their cereal.

    protein = random.uniform(1,5)
    fat =  random.uniform(1,5)
    sodium = random.uniform(0,5)
    carbohydrates= random.uniform(1,30)
    potassium = random.uniform(0,5)
    vitamins = random.uniform(1,50)

    #dictionary for df1
    dict_1 ={'protein':protein,'fat':fat,'sodium':sodium,'carbohydrates':carbohydrates,'potassium':potassium,'vitamins':vitamins}

    #add values to dataframe
    df1= pd.DataFrame(dict_1, index=[0])


    if request.method == 'POST':
        calories = request.form['calories']
        fiber = request.form['fiber']
        sugars = request.form['sugars']

        dict_2 = {'calories':calories, 'fiber':fiber,'sugars':sugars }
        df2= pd.DataFrame(dict_2,index=[0])
        data = pd.concat([df2,df1], axis=1)
        my_prediction = model.predict(data)
    return render_template('results.html', prediction=my_prediction, comment='')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
