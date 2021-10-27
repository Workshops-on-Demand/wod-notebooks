import os
import sys 
import json
import requests
import tensorflow as tf
from time import sleep


'''
Pregnancies - Number of times pregnant 
Glucose — The blood plasma glucose concentration after a 2 hour oral glucose tolerance test.
BloodPressure — Diastolic blood pressure (mm/HG).
SkinThickness — Skinfold thickness of the triceps (mm).
Insulin — 2 hour serum insulin (mu U/ml).
BMI — Body mass index (kg/m squared)
DiabetesPedigreeFunction — A function that determines the risk of type 2 diabetes based on family history, the larger the function, the higher the risk of type 2 diabetes.
Age.

Example input 
{ 
	"use_scoring": true, 
	"scoring_args": {
		"NumPreg" : 8.0, 
		"Glucose" : 183.0, 
		"BloodPressure" : 64.0, 
		"SkinThick" : 0.0, 
		"Insulin" : 0.0, 
		"BMI" : 23.3, 
		"DiabetesPedFunc" : 0.672, 
		"Age" : 32.0
	}
}

'{"NumPreg":1.0,"Glucose":85.0,"BloodPressure":66.0,"SkinThick":29.0,"Insulin":0.0,"BMI":26.6,"DiabetesPedFunc":0.351,"Age":35.0}'

'''

## Set the project repo 
def ProjectRepo(path):
    ProjectRepo = "/bd-fs-mnt/project_repo/"
    return ProjectRepo + '/' + path

cli_input = json.loads(sys.argv[1])

input_data = [] 
col_names = ["NumPreg", "Glucose", "BloodPressure", "SkinThick", "Insulin", "BMI", "DiabetesPedFunc", "Age"]
for i in col_names:
	input_data.append(cli_input[i])

model = tf.keras.models.load_model(ProjectRepo('models/Diabetes_Prediction/db_remote.h5'))
predictions = model.predict([input_data])
print("Diabetes chance: ", round(predictions[0][0],2))
