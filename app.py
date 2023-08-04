# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 22:54:40 2023

@author: abish
"""
from flask import Flask, request, render_template
import joblib

app=Flask(__name__)
model=joblib.load(open('C:\\Users\\abish\\OneDrive\\Documents\\Project\\gas.joblib','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    
    x_test=[[int(x) for x in request.form.values()]]
    prediction=model.predict(x_test)
    print(prediction)
    pred=prediction[[0]]
    return render_template('index.html',prediction_text='Gas Price is {} Dollars'.format(pred))

if __name__=='__main__':
    app.run(debug=True)