import argparse
import numpy as np
from FeatureProcessing import FeatureConstruction, FeatureConversion, FeatureRanking, FeatureSelection
# np.random.seed(1337) # random seed

def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--tv_set',
        type=str,
        default='Example\\TrainingValidationSet.fasta',
        help='name of the Training-Validation Set'
    )
    parser.add_argument(
        '--test_set',
        type=str,
        default='None',
        # default='Example\\TestSet.fasta',
        help='name of Test Set'
    )
    parser.add_argument(
        '--all_feature',
        type=bool,
        default=False,
        help='Features without ranking'
    )
    parser.add_argument(
        '--ranked_feature',
        type=bool,
        default=False,
        help='Ranked features'
    )
    parser.add_argument(
        '--retained_feature',
        type=bool,
        default=True,
        help='Retained features'
    )
    args = parser.parse_args()
    return args

def DataLoad(tv_set_path, test_set_path):
    list_tv_set = open(tv_set_path, 'r').readlines()
    list_test_set = open(test_set_path, 'r').readlines() if test_set_path is not "None" else "None"
    return list_tv_set, list_test_set

def ComplexFeatureConstruction(list_tv_set, list_test_set):
    cf_tv_set = FeatureConstruction(list_tv_set)
    cf_test_set = FeatureConstruction(list_test_set) if list_test_set is not "None" else "None"
    return cf_tv_set, cf_test_set

def ComplexFeatureConversion(cf_tv_set, cf_test_set):
    X_train, y_train = FeatureConversion(cf_tv_set)
    if cf_test_set is not "None":
        X_test, y_test = FeatureConversion(cf_test_set)
    else:
        X_test, y_test = "None", "None"
    return X_train, y_train, X_test, y_test

def ComplexFeatureRanking(X_train, y_train, X_test, y_test):
    rcf_tv_set, rcf_test_set, IndicesRF = FeatureRanking(X_train, y_train, X_test, y_test)
    return rcf_tv_set, rcf_test_set, IndicesRF

def ComplexFeatureSelection(X_train, y_train, IndicesRF, rcf_tv_set, rcf_test_set):
    scf_tv_set, scf_test_set = FeatureSelection(X_train, y_train, IndicesRF, rcf_tv_set, rcf_test_set)
    return scf_tv_set, scf_test_set

def RNAIFRID(args):
    # data loading
    list_tv_set, list_test_set = DataLoad(args.tv_set, args.test_set)
    # complex feature constructing
    cf_tv_set, cf_test_set = ComplexFeatureConstruction(list_tv_set, list_test_set)
    # complex feature conversion
    X_train, y_train, X_test, y_test = ComplexFeatureConversion(cf_tv_set, cf_test_set)
    # complex feature ranking
    rcf_tv_set, rcf_test_set, IndicesRF = ComplexFeatureRanking(X_train, y_train, X_test, y_test)
    # complex feature selecting
    scf_tv_set, scf_test_set = ComplexFeatureSelection(X_train, y_train, IndicesRF, rcf_tv_set, rcf_test_set)
    # output all complex features without ranking
    if args.all_feature == True:
        w1 = open('Complex Features without Ranking (TrainingValidationSet).fasta', 'w')
        w1.writelines(cf_tv_set)
        w1.close()
        if cf_test_set is not "None":
            w2 = open('Complex Features without Ranking (TestSet).fasta', 'w')
            w2.writelines(cf_test_set)
            w2.close()
    # output ranked complex features
    if args.ranked_feature == True:
        w3 = open('Ranked Complex Features (TrainingValidationSet).fasta', 'w')
        w3.writelines(rcf_tv_set)
        w3.close()
        if rcf_test_set is not "None":
            w4 = open('Ranked Complex Features (TestSet).fasta', 'w')
            w4.writelines(rcf_test_set)
            w4.close()
    # output retained complex features
    if args.retained_feature == True:
        w5 = open('Retained Complex Features (TrainingValidationSet).fasta', 'w')
        w5.writelines(scf_tv_set)
        w5.close()
        if scf_test_set is not "None":
            w6 = open('Retained Complex Features (TestSet).fasta', 'w')
            w6.writelines(scf_test_set)
            w6.close()

def main():
    args = args_parser()
    RNAIFRID(args)

if __name__ == '__main__':
    main()