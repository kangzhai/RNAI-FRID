# RNAI-FRID
The related data and scoure codes of RNAI-FRID are provided by Q. Kang.

The latest version is updated on January 11, 2022.

The complete codes will to be released before January 12, 2022.

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
--tv_set: Path of dataset for training and validation and default is "Example\TrainingValidationSet.fasta". It must be a path.

--test_set: Path of dataset for test and default is "None". It must be a path or "None". "None" means only training and validation without test. When it is not "None", the features of testset can be output.

--all_feature: Output all complex features without ranking. It must be "True" or "False".

--ranked_feature: Output ranked complex features. It must be "True" or "False".

--retained_feature: Output retained complex features. It must be "True" or "False".

# Reference
If you use the codes, please cite the reference as below.

The paper has been submitted. Please wait for updating.
