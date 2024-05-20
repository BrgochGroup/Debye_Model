{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "Fnk8aQ6whx0K",
    "outputId": "4c8df21d-9ccd-44e1-a7c4-19f9fb4576b1"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(6, 137)\n"
     ]
    }
   ],
   "source": [
    "# -*- coding: utf-8 -*-\n",
    "\"\"\"\n",
    "Created on Fri May 8 22:00:41 2020\n",
    "\n",
    "@author: Ya Zhuo, University of Houston\n",
    "\"\"\"\n",
    "\n",
    "# Import general python packages and read in the compounds list\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from pymatgen.core.composition import Composition\n",
    "\n",
    "class Vectorize_Formula:\n",
    "\n",
    "    def __init__(self):\n",
    "        # Read the elements data from Excel\n",
    "        elem_dict = pd.read_excel(r'elements.xlsx')  # Ensure this file has the correct data\n",
    "        self.element_df = pd.DataFrame(elem_dict)\n",
    "        self.element_df.set_index('Symbol', inplace=True)\n",
    "        self.column_names = []\n",
    "        for string in ['avg', 'diff', 'max', 'min']:\n",
    "            for column_name in list(self.element_df.columns.values):\n",
    "                self.column_names.append(string + '_' + column_name)\n",
    "\n",
    "    def get_features(self, formula):\n",
    "        try:\n",
    "            fractional_composition = Composition(formula).fractional_composition.as_dict()\n",
    "            element_composition = Composition(formula).element_composition.as_dict()\n",
    "            avg_feature = np.zeros(len(self.element_df.iloc[0]))\n",
    "            diff_feature = np.zeros(len(self.element_df.iloc[0]))\n",
    "            \n",
    "            for key in fractional_composition:\n",
    "                try:\n",
    "                    avg_feature += self.element_df.loc[key].values * fractional_composition[key]\n",
    "                    diff_feature = self.element_df.loc[list(fractional_composition.keys())].max() - self.element_df.loc[list(fractional_composition.keys())].min()\n",
    "                except Exception as e:\n",
    "                    print(f'The element: {key}, Formula: {formula}, Error: {e}')\n",
    "                    return np.array([np.nan] * len(self.element_df.iloc[0]) * 5)\n",
    "\n",
    "            max_feature = self.element_df.loc[list(fractional_composition.keys())].max()\n",
    "            min_feature = self.element_df.loc[list(fractional_composition.keys())].min()\n",
    "           \n",
    "\n",
    "            features = np.concatenate([avg_feature, diff_feature, np.array(max_feature), np.array(min_feature)])\n",
    "            return features.transpose()\n",
    "        except Exception as e:\n",
    "            print(f'There was an error with the Formula: {formula}, Error: {e}')\n",
    "            return [np.nan] * len(self.element_df.iloc[0]) * 5\n",
    "\n",
    "# Instantiate the Vectorize_Formula class\n",
    "gf = Vectorize_Formula()\n",
    "\n",
    "composition_df = pd.read_excel('c_pounds.xlsx', sheet_name='Sheet1', usecols=\"A\")\n",
    "\n",
    "# Ensure the 'Formula' column exists\n",
    "\n",
    "\n",
    "# Empty list for storage of features\n",
    "features = []\n",
    "\n",
    "# Add values to the list using a for loop\n",
    "for formula in composition_df['Formula']:\n",
    "    features.append(gf.get_features(formula))\n",
    "\n",
    "# Feature vectors as DataFrame\n",
    "X = pd.DataFrame(features, columns=gf.column_names)\n",
    "\n",
    "# Combine composition data with features\n",
    "composition = pd.DataFrame(composition_df['Formula'], columns=['Formula'])\n",
    "predicted = pd.concat([composition, X], axis=1)\n",
    "\n",
    "# Export the combined data to an Excel file\n",
    "predicted.to_excel('to_predict_Debye_T.xlsx', index=False)\n",
    "\n",
    "# Read and display the shape of the resulting DataFrame\n",
    "file_path = 'to_predict_Debye_T.xlsx'\n",
    "df = pd.read_excel(file_path)\n",
    "\n",
    "# Display the shape of the DataFrame\n",
    "print(df.shape)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
  "colab": {
   "provenance": []
  },
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
