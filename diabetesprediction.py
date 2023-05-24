# -*- coding: utf-8 -*-
"""DiabetesPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S7slfNhmsGAIFOZMDiqmY4FmxOQi0EZ8

Importing the libararies, i.e, Dependencies for the project
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection & Analysis
 
PIMA Diabetes Dataset
"""

# loading the diabetes dataset to a pandas DataFrame
diabetes_dataset = pd.read_csv('/content/diabetes.csv')

#printing the first 5 rows of the dataset
diabetes_dataset.head()

#number of rows & columns in this dataset
diabetes_dataset.shape

# getting the statistical measures of the data
diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""0 --> Non-Diabetic

1 --> Diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

# seperating data & labels
X = diabetes_dataset.drop(columns = 'Outcome', axis = 1)
Y = diabetes_dataset['Outcome']

print(X)

print(Y)

"""DATA Standardization"""

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']

"""Split the Data into Training & Testing Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state = 2)

print(X.shape, X_train.shape, X_test.shape)

"""TRAINING THE MODEL"""

classifier = svm.SVC(kernel='linear')

#training the SVM Classifier
classifier.fit(X_train, Y_train)

"""EVALUTE OUR MODEL"""

# ACCURACY SCORE on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy Score of the Training Data : ', training_data_accuracy)

"""Testing the Testing DATA"""

# ACCURACY SCORE on the testing data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy Score of the Testing Data : ', test_data_accuracy)

"""Making a Predictive System

"""

input_data = (4, 110, 92, 0, 0, 37.6, 0.191, 30)

#change the input_data to a numPy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

#standardized the given
std_data = scaler.transform(input_data_reshaped)

print('The Standardized data is: ', std_data) 

#lets make the prediction
prediction = classifier.predict(std_data)

print('The Prediction is: ', prediction)

if(prediction[0] == 0):
  print('The Person is not Diabetic')
else:
  print('The Person is Diabetic')