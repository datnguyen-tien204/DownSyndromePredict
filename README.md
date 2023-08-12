# Down Syndrome Prediction

## What's in this repo?
Dataset is divided into 2 sets "train.csv" and "test.csv". With a ratio of 9/1
```train.csv``` is the training set. In this training set, the data will be further separated into 80% Training and 20% Validation

```test.csv``` is the test set. It is used to check the model data after training is complete

```*.sav``` are files to save the model after training. Used for loading data for prediction in the application. It saves with standard SPSS

```*.pkl``` are files to save the model after training. Used for loading data for prediction in the application. It saves with standard Pickle

## Installation

The code requires `python>=3.7`, `Scikit Learn>=1.0` ,`joblib>=1.1` and `XGBoost`. Please follow the instructions [here](https://scikit-learn.org/stable/index.html) to install both PyTorch and TorchVision dependencies.

## Dataset Introduce
- age_me_new: The mother's age at pregnancy, is important information regarding the age of the fetus and the risk of having a baby with Down syndrome.
- age_thai_new: The age of the fetus, usually calculated from the time of the beginning of pregnancy. This age may be related to fetal growth and the risk of Down syndrome.
- tiensusinhconhoichungdown: Information about any development related to Down syndrome during pregnancy, such as laboratory results or clinical signs.
- chieudaidaumong: Measurement of fetal head and rump length, used to assess fetal development status.
- dau_duong Kinhluongdinh: Measure the size of the amniotic fluid index (AFI) during pregnancy, used to assess the health of the fetus and pregnant woman.
- dau_chuvidau: Measurement of fetal head circumference, this information is also related to fetal development status.
- mat_moimui: Records of fetal eye, nose, and mouth signs, which can be used to check for abnormalities related to Down syndrome.
- Nguc_nhiptimthai: Measure the size of the chest and heart of the fetus, this information can reflect the health status of the fetus.
- d_mom_pappa: Information related to the fulcrum in the family. Does anyone in your family have Down syndrome?
- d_mom_hcgb: The level of beta hCG hormone in the mother's blood, often used to assess the risk of Down syndrome in the fetus.
- d_khoangsangsaugay: Results of measuring the distance from the embryonic membrane to the top of the head muscles (cervical length) during pregnancy, related to the risk of preterm birth or not.
- ketluan_hoichungdown: Conclusion about the possibility of the fetus having Down syndrome or not, usually based on the results of tests and assessment of the health of the fetus during pregnancy.

  ## Result

  ### Logistic Regression: 93.08%
  <p float="left">
  <img src="assets/masks1.png?raw=true" width="37.25%" />
</p>
  ### 
  
