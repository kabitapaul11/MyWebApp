import numpy as np
from datetime import date, datetime
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict, GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import metrics
import pandas as pd
import pickle

# Load csv file.
df_cereals = pd.read_csv('inputfile/cereal_mg_to_g.csv')


df_cereals.rename(columns={'protein(g)': 'protein', 'fat(g)': 'fat', 'sodium(g)': 'sodium', 'fiber(g)': 'fiber',
                           'carbo(g)': 'carbohydrates', 'sugars(g(': 'sugars', 'potass(g)': 'potassium', 'vitamins(%)': 'vitamins'}, inplace=True)

df_cereals.carbohydrates =df_cereals.carbohydrates.astype('float')
print(df_cereals.info())
# create add_label function
def add_label(df):
    if df.calories <= 160 and df.fiber >=3 and df.sugars <=4:
        return 1 # healthy cereal
    else:
        return 0 #not healthy cereal


# add a healthy_label column to dataframe
df_cereals['health_label']= df_cereals.apply(add_label,axis=1)

print(df_cereals[df_cereals.health_label==1])

# define Y variable and feature set
Y= df_cereals['health_label']
features= df_cereals.loc[:,'calories':'vitamins']

X_train, X_test, Y_train, Y_test = train_test_split(features, Y,random_state=42)

##########################################
# Random Forest classifier Model
###########################################

#build grid-search to get best estimators
#print(X_train.shape)

gr = GridSearchCV(
        estimator=RandomForestClassifier(),
        param_grid={
            'max_depth': range(3,7),
            'n_estimators': np.arange(10,100,10),
            'max_features': np.arange(3,6,1)
        }, cv=5, verbose=0)
    
grid_result = gr.fit(X_train, Y_train)
best_params = grid_result.best_params_ #{'max_depth': 6, 'max_features': 16, 'n_estimators': 50}

print(best_params) #{'max_depth': 3, 'max_features': 5, 'n_estimators': 50}

rf_classify = RandomForestClassifier(n_estimators=5,max_depth=3, max_features=5,random_state=15,oob_score=True)

#train random forest classifier
rf_classify.fit(X_train, Y_train)

# serialize model to disk
pickle.dump(rf_classify,open('outputfiles/rf_model.pk1','wb'))

rf_classify.score(X_train, Y_train)
Y_prd=prd=rf_classify.predict(X_test)

accuracy = metrics.accuracy_score(Y_test,Y_prd)
print("Accuracy:",accuracy)
