from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle

filename = "model_diabete_predictor.hd5"

#data
diabete_db = pd.read_csv('diabetes.csv')

#standarisation of the series
X=diabete_db.drop("Outcome",axis=1).values
standard=StandardScaler()
X_s=standard.fit_transform(X)
breakpoint()

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

#predict
def predict(data):        
    y_preds = loaded_model.predict(data)

    for i,val in enumerate(y_preds[0:20]):
        if val == 1:
            print(f"{i}-Diabetique")
        else:
            print(f"{i}-Pas diabetique")

predict(data=X_s)