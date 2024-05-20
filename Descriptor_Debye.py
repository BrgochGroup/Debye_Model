# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:00:41 2024

@author: Amit Kumar, University of Houston

"""
# To run this code, you need c_ponds.xlsx and elements.xlsx
import pandas as pd
import numpy as np
from pymatgen.core.composition import Composition

class Vectorize_Formula:

    def __init__(self):
        # Read the elements data from Excel
        elem_dict = pd.read_excel(r'elements.xlsx')  # Ensure this file has the correct data
        self.element_df = pd.DataFrame(elem_dict)
        self.element_df.set_index('Symbol', inplace=True)
        self.column_names = []
        for string in ['avg', 'diff', 'max', 'min']:
            for column_name in list(self.element_df.columns.values):
                self.column_names.append(string + '_' + column_name)

    def get_features(self, formula):
        try:
            fractional_composition = Composition(formula).fractional_composition.as_dict()
            element_composition = Composition(formula).element_composition.as_dict()
            avg_feature = np.zeros(len(self.element_df.iloc[0]))
            diff_feature = np.zeros(len(self.element_df.iloc[0]))
            
            for key in fractional_composition:
                try:
                    avg_feature += self.element_df.loc[key].values * fractional_composition[key]
                    diff_feature = self.element_df.loc[list(fractional_composition.keys())].max() - self.element_df.loc[list(fractional_composition.keys())].min()
                except Exception as e:
                    print(f'The element: {key}, Formula: {formula}, Error: {e}')
                    return np.array([np.nan] * len(self.element_df.iloc[0]) * 5)

            max_feature = self.element_df.loc[list(fractional_composition.keys())].max()
            min_feature = self.element_df.loc[list(fractional_composition.keys())].min()
           

            features = np.concatenate([avg_feature, diff_feature, np.array(max_feature), np.array(min_feature)])
            return features.transpose()
        except Exception as e:
            print(f'There was an error with the Formula: {formula}, Error: {e}')
            return [np.nan] * len(self.element_df.iloc[0]) * 5

gf = Vectorize_Formula()

composition_df = pd.read_excel('c_pounds.xlsx', sheet_name='Sheet1', usecols="A")

# Ensure the 'Formula' column exists

features = []
for formula in composition_df['Formula']:
    features.append(gf.get_features(formula))

X = pd.DataFrame(features, columns=gf.column_names)

composition = pd.DataFrame(composition_df['Formula'], columns=['Formula'])
predicted = pd.concat([composition, X], axis=1)

predicted.to_excel('to_predict_Debye_T.xlsx', index=False)


file_path = 'to_predict_Debye_T.xlsx'
df = pd.read_excel(file_path)

# Display the shape of the DataFrame
print(df.shape)
