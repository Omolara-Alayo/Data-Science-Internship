# Using Flask to make an AP1 
# Import the necessary libraries and functions
from flask import Flask, jsonify, request
import pickle
import pandas as pd

# Creating a Flask app
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home ():
    if(request.method == 'GET'):
        data = "Hello, this is my first API"
        return jsonify({'data':data})
    


@app.route('/predict/')
def heart_disease_predict():
    model = pickle.load(open('heart_disease_model.pkl', 'rb'))
    age = request.args.get('age')
    sex = request.args.get('sex')
    cp = request.args.get('cp')
    trestbps= request.args.get('trestbps')
    chol = request.args.get('chol')
    fbs = request.args.get('fbs')
    restecg = request.args.get('restecg')
    thalach = request.args.get('thalach')
    exang = request.args.get('exang')
    oldpeak = request.args.get('oldpeak')
    slope  = request.args.get('slope')
    ca = request.args.get('ca')
    thal = request.args.get('thal')

    test_df = pd.DataFrame({'Age':[age], 'Sex':[sex], 'Chest Pain Type':[cp], 'Resting Blood Pressure':[trestbps],
                             'Serum Cholesterol':[chol], 'Fasting Blood Sugar':[fbs], 'Resting electrocardiographic measurement':[restecg], 
                             'Maximum Heart Rate':[thalach], 'Exercise Induce Angina':[exang], 'ST Depression':[oldpeak], 'Slope':[slope],
                             'Blood Vessel':[ca], 'Thalassemia Blood Disorder':[thal]})
    
    pred_heart_disease = model.predict(test_df)
    if pred_heart_disease == 1:
        return jsonify({'Heart Disease Prediction':"Positive"})
    else:
        return jsonify({'Heart Disease Prediction':"Negative"})
   
# Driver function
if __name__ == '__main__':
    app.run(debug=True)



    




