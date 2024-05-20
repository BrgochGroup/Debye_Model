# Debye T predictor
Predict Debye Temperature for inorganic materials



## Table of Contents

- [Citations](#citations)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [Define a customized prediction set](#define-a-customized-prediction-set)
  - [Predict Debye Temperature](#predict-bandgap-energy)
- [Authors](#authors)

## Citations

To cite Debye Temperature predictions, please reference the following work:

Zhuo, Y., Mansouri Tehrani, A., Oliynyk, A. O., Duke, A. C., & Brgoch, J., Identifying an efficient, thermally robust inorganic phosphor host via machine learning, *Nature communications* **2018**, 9, 4377.

##  Prerequisites

This package requires:

- [pymatgen](http://pymatgen.org)
- [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html)
- [scikit-learn](http://scikit-learn.org/stable/)
- [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
- [NumPy](https://docs.scipy.org/doc/numpy/index.html)
- [xlrd](https://xlrd.readthedocs.io/en/latest/index.html)

## Usage


 Define a customized prediction set for relative permittivity

You should create a `.xlsx` file named `c_pounds.xlsx`, in which the compositions that you want to predict are listed in the first column with the header "`Formula`".

There is one [example of customized dataset](/examples) in the repository:c_pounds.xlsx`.

You can get compositional descriptors by:

```bash
Descriptor_Debye.py
```

`descriptor_generator.py` will automatically read `elements.xlsx` and `c_pounds.xlsx` to generate descriptors. After running, you will get a `.xlsx` file named `to_predict_Debye_T.xlsx`. In this file, the first column is your composition followed by 136 columns of descriptors.

You also need to append another 14 structural descriptors to the compositional descriptors:
- Space group number
- Crystal system
- Laue class
- Crystal class
- Inversion center
- Polar axis
- Reduced volume
- Density
- Average anisotropy (average between a/b, b/c, c/a)
- Electron density: number of valence electrons per V per Z
- V per atom
- Electron density (number of valence electrons per V per atom)
- Electron density (Gilman valence per V per atom)
- Electron density (outer shell per V per atom)

This information could be extracted from crystallographic information files (CIFs) and inorganic crystal databases. 
Note: The final training dataset "to_predict_Debye_T.xlsx" will contain 150 descriptors

### Predict Debye T
After preparing `to_predict_Debye_T.xlsx`, you can get the debye temperature prediction by:

```bash
python Debye_T_model.py
```

`Debye_T_model.py` will automatically read `Debye_T_Training_Set.xlsx`,and `to_predict_Debye_T.xlsx` to generate a prediction. After running, you will get a `.xlsx` file named `predicted_debye.xlsx` in the same directory, in which the predicted Debye_T is provided next to the corresponding composition.

## Authors

This software was created by [Amit_Kumar](https://github.com/ak983819) who is advised by [Prof. Jakoah Brgoch](https://www.brgochchemistry.com/).
