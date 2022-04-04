# RNAI-FRID
The related data and scoure codes of RNAI-FRID are provided by Q. Kang.

The latest version is updated on January 11, 2022.

# Introduction
RNAI-FRID is a novel feature representation method, which can generate the complex complex with information enhancement and dimension reduction for representing RNA-RNA interaction.

# Dependency
Windows operating system

Python 3.6.5

Kreas 2.2.4

# Details
### Example folder
The examples of training-validation and test sets.

### RNAI-FRID.py
Python codes of RNAI-FRID for feature representation.

### FeatureProcessing.py
Python codes of function for feature processing.

# Usage
Open the console or powershell in the local folder and copy enter the command against the folling example to run RNAI-FRID. It is also feasible to run the codes using python IDE (such as pyCharm).

### Command (an example):
python RNAI-FRID.py --tv_set Example\TrainingValidationSet.fasta --test_set None --all_feature False --ranked_feature False --retained_feature True

### Explanation:
--tv_set (must be a path): Path of dataset for training and validation and default is "Example\TrainingValidationSet.fasta".

--test_set (must be a path or "None"): Path of dataset for test and default is "None". "None" means only training and validation without test. When it is not "None", the features of testset can be output.

--all_feature (must be "True" or "False"): Output all complex features without ranking and default is "False".

--ranked_feature (must be "True" or "False"): Output ranked complex features and default is "False".

--retained_feature (must be "True" or "False"): Output retained complex features and default is "True".

--rf (must be "True" or "False"): Train a Random Forest model with the generated features and default is "False". If "test_set" is "None", output the 10-fold cross-validation results, otherwise output the test result.

--svm (must be "True" or "False"): Train a Support Vector Machine model with the generated features and default is "False". If "test_set" is "None", output the 10-fold cross-validation results, otherwise output the test result.

--lr (must be "True" or "False"): Train a Logistic Regression model with the generated features and default is "False". If "test_set" is "None", output the 10-fold cross-validation results, otherwise output the test result.

--gb (must be "True" or "False"): Train a Gradient Boosting model with the generated features and default is "False". If "test_set" is "None", output the 10-fold cross-validation results, otherwise output the test result.

--knn (must be "True" or "False"): Train a K-Nearest Neighbour model with the generated features and default is "False". If "test_set" is "None", output the 10-fold cross-validation results, otherwise output the test result.

--nb (must be "True" or "False"): Train a Naive Bayes model with the generated features and default is "False". If "test_set" is "None", output the 10-fold cross-validation results, otherwise output the test result.

--dt (must be "True" or "False"): Train a Decision Tree model with the generated features and default is "False". If "test_set" is "None", output the 10-fold cross-validation results, otherwise output the test result.

In the output feature file, each line represents the feature values of a sample (the last number of each line is the label), and the features are separated by spaces.

# Reference
If you use the codes, please cite the reference as below.

Qiang Kang, Jun Meng, Yushi Luan. RNAI-FRID: novel feature representation method with information enhancement and dimension reduction for RNA-RNA interaction. Briefings in Bioinformatics. 2022. https://doi.org/10.1093/bib/bbac107
