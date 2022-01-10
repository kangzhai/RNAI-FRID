# RNAI-FRID
A novel feature representation method to generate the complex complex with information enhancement and dimension reduction for representing RNA-RNA interaction.

# Usage
An example of command:

python RNAI-FRID.py --tv_set Example\TrainingValidationSet.fasta --test_set Example\TestSet.fasta --all_feature False --ranked_feature False --retained_feature True

python RNAI-FRID.py: execute RNAI-FRID.py file

--tv_set: Path of dataset for training and validation and default is "Example\TrainingValidationSet.fasta". It must be a path.

--test_set: Path of dataset for test and default is "None". It can be a path or "None". "None" means only training and validation without test. When it is not "None", the features of testset will be output.

--all_feature: Output all complex features without ranking. It must be "True" or "False".

--ranked_feature: Output ranked complex features. It must be "True" or "False".

--retained_feature: Output retained complex features. It must be "True" or "False".

# The complete codes and usage are updating now.
