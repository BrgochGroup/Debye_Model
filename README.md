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
- [XGBoost](https://xgboost.readthedocs.io/en/latest/#)
- [scikit-learn](http://scikit-learn.org/stable/)
- [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
- [NumPy](https://docs.scipy.org/doc/numpy/index.html)
- [xlrd](https://xlrd.readthedocs.io/en/latest/index.html)

## Usage


 Define a customized prediction set for relative permittivity

You should create a `.xlsx` file named `c_pounds.xlsx`, in which the compositions that you want to predict are listed in the first column with the header "`Formula`".

There is one [example of customized dataset](/examples) in the repository:`examples/c_pounds.xlsx`.

You can get compositional descriptors by:

```bash
python descriptor_generator.py
```

`descriptor_generator.py` will automatically read `elements.xlsx` and `c_pounds.xlsx` to generate descriptors. After running, you will get a `.xlsx` file named `to_predict_relative_permittivity.xlsx`. In this file, the first column is your composition followed by 85 columns of descriptors.

You also need to append another 13 structural descriptors to the compositional descriptors:
- space group number
- unit cell volume (nm<sup>3</sup>)
- density (Mg/m<sup>3</sup>)
- *a*/*b*
- *b*/*c*
- *c*/*a*
- alpha/beta
- beta/gamma
- gamma/alpha
- existance of inversion center (exist:1; nonexist:0)
- existance of polar axis (exist:1; nonexist:0)
- volume per *Z* (nm<sup>3</sup>)
- volume per atom (nm<sup>3</sup>)

This information could be extracted from crystallographic information files (CIFs) and inorganic cystal databases. There is one [example](/examples) of the final `to_predict_relative_permittivity.xlsx` file in the repository:`examples/to_predict_relative_permittivity.xlsx`.

### 1_2 Predict relative permittivity
Before getting a prediction, you will need to:

- [Prepare a customized dataset](#1_1-define-a-customized-prediction-set-for-relative-permittivity) named after `to_predict_relative_permittivity.xlsx` to store the composition-structure-property relations of interest.

Then, you can predict the relative permittivity by:

```bash
python relative_permittivity_predictor.py
```

`relative_permittivity_predictor.py` will automatically read `relative_permittivity_training_set.xlsx` and `to_predict_relative_permittivity.xlsx` to generate a prediction. You will then get a `predicted_relative_permittivity.xlsx` file in the same directory, in which the predicted relative_permittivity is provided next to the corresponding composition.

### 2 Centroid shift prediction

### 2_1 Define a customized prediction set for centroid shift

You should create a `.xlsx` file named `to_predict_centroid_shift.xlsx` in the format as:

| A | B | C | D | E | F | G | H | I |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Composition | Relative permittivity | Avg. cation electronegativity | Avg. anion polarizability | R<sub>m</sub> | DeltaR (R<sub>m</sub>-R<sub>Ce</sub> | Avg. bond length | Coord. no. | Condensation |

There is one [example of customized dataset](/examples) in the repository:`examples/to_predict_centroid_shift.xlsx`.

### 2_2 Predict centroid shift
Before getting a prediction, you will need to:

- [Prepare a customized dataset](#2_1-define-a-customized-prediction-set-for-centroid-shift) named after `to_predict_centroid_shift.xlsx` to store the composition-structure-property relations of interest.

Then, you can predict the relative permittivity by:

```bash
python centroid_shift_predictor.py
```

`centroid_shift_predictor.py` will automatically read `centroid_shift_training_set.xlsx` and `to_predict_centroid_shift.xlsx` to generate a prediction. You will then get a `predicted_centroid_shift.xlsx` file in the same directory, in which the predicted centroid shift is provided next to the corresponding composition.

## Authors

This software was created by [Ya Zhuo](https://github.com/yzhuo33) who is advised by [Prof. Jakoah Brgoch](https://www.brgochchemistry.com/).
