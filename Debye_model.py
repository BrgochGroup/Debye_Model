{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "R^2 score on test data: 0.8924475691058944\n",
      "Predictions on new data saved to 'Predicted_debye.xlsx'\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn import preprocessing\n",
    "from sklearn.svm import SVR\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import r2_score\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "DE = pd.read_excel('Debye_T_Training_Set.xlsx')\n",
    "array = DE.values\n",
    "X = array[:, 2:160]\n",
    "Y = array[:, 1]\n",
    "\n",
    "# Train-test split\n",
    "X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=15, shuffle=True)\n",
    "\n",
    "# Data transformation\n",
    "scaler = preprocessing.StandardScaler().fit(X_train)\n",
    "X_train = scaler.transform(X_train)\n",
    "X_test = scaler.transform(X_test)\n",
    "\n",
    "# SVR model construction\n",
    "SVM = SVR(kernel='rbf', C=10**3.2, epsilon=0.1, gamma=0.0032).fit(X_train, Y_train)\n",
    "\n",
    "# Predict on test data\n",
    "y_pred = SVM.predict(X_test)\n",
    "\n",
    "# Calculate R^2 score on training data\n",
    "Y_train_pred = SVM.predict(X_train)\n",
    "r2_train = r2_score(Y_train, Y_train_pred)\n",
    "\n",
    "# Calculate R^2 score on test data\n",
    "r2_test = r2_score(Y_test, y_pred)\n",
    "print(\"R^2 score on test data:\", r2_test)\n",
    "\n",
    "# Plot predictions vs actual values\n",
    "\n",
    "\n",
    "# Load new data for prediction\n",
    "new_data = pd.read_excel('to_predict_Debye_T.xlsx')\n",
    "new_data_array = new_data.values\n",
    "X_new = new_data_array[:, 1:160]  # Adjust indices if necessary\n",
    "\n",
    "# Preprocess new data using the same scaler\n",
    "X_new_scaled = scaler.transform(X_new)\n",
    "\n",
    "# Make predictions on new data\n",
    "new_predictions = SVM.predict(X_new_scaled)\n",
    "\n",
    "# Add predictions to the new data DataFrame\n",
    "new_data['Predicted Debye T'] = new_predictions\n",
    "\n",
    "# Select only 'Composition' and 'Predicted' columns\n",
    "output_data = new_data[['Formula', 'Predicted Debye T']]\n",
    "\n",
    "# Save the new data with predictions to a new Excel file\n",
    "output_data.to_excel('Predicted_debye.xlsx', index=False)\n",
    "\n",
    "print(\"Predictions on new data saved to 'Predicted_debye.xlsx'\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
