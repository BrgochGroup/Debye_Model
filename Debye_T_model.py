# -*- coding: utf-8 -*-
"""
Created on Fri May  20 15:58:52 2024

@author: Amit Kumar, University of Houston

"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


DE = pd.read_excel('Debye_T_Training_Set.xlsx')
array = DE.values
X = array[:, 2:160]
Y = array[:, 1]

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=15, shuffle=True)

# Data transformation
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# SVR model construction
SVM = SVR(kernel='rbf', C=10**3.2, epsilon=0.1, gamma=0.0032).fit(X_train, Y_train)

# Predict on test data
y_pred = SVM.predict(X_test)
Y_train_pred = SVM.predict(X_train)
r2_test = r2_score(Y_test, y_pred)
print("R^2 score on test data:", r2_test)

# Load new data for prediction
new_data = pd.read_excel('to_predict_Debye_T.xlsx')
new_data_array = new_data.values
X_new = new_data_array[:, 1:160]  # Adjust indices if necessary
X_new_scaled = scaler.transform(X_new)
new_predictions = SVM.predict(X_new_scaled)
new_data['Predicted Debye T'] = new_predictions
output_data = new_data[['Formula', 'Predicted Debye T']]

# Save the new data with predictions to a new Excel file
output_data.to_excel('Predicted_debye.xlsx', index=False)
print("Predictions on new data saved to 'Predicted_Debye.xlsx'")
