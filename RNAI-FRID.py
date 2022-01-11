# Main processing

import argparse
import numpy as np
from FeatureProcessing import FeatureConstruction, FeatureConversion, FeatureRanking, FeatureSelection
from ModelProcessing import Test, CrossValidation
np.random.seed(1337) # random seed

def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--tv_set',
        type=str,
        default='Example\\TrainingValidationSet.fasta',
        help='path of the Training-Validation Set'
    )
    parser.add_argument(
        '--test_set',
        type=str,
        # default='None',
        default='Example\\TestSet.fasta',
        help='path of Test Set'
    )
    parser.add_argument(
        '--all_feature',
        type=str,
        default="False",
        help='Features without ranking'
    )
    parser.add_argument(
        '--ranked_feature',
        type=str,
        default="False",
        help='Ranked features'
    )
    parser.add_argument(
        '--retained_feature',
        type=str,
        default="True",
        help='Retained features'
    )
    parser.add_argument(
        '--rf',
        type=str,
        default="False",
        help='Random Forest'
    )
    parser.add_argument(
        '--svm',
        type=str,
        default="False",
        help='Support Vector Machine'
    )
    parser.add_argument(
        '--lr',
        type=str,
        default="False",
        help='Logistic Regression'
    )
    parser.add_argument(
        '--gb',
        type=str,
        default="False",
        help='Gradient Boosting'
    )
    parser.add_argument(
        '--knn',
        type=str,
        default="False",
        help='K-Nearest Neighbour'
    )
    parser.add_argument(
        '--nb',
        type=str,
        default="False",
        help='Gaussian Naive Bayes'
    )
    parser.add_argument(
        '--dt',
        type=str,
        default="False",
        help='Decision Tree'
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

def ResultOutput(bol, mod, TPR, PPV, ACC, F1, MCC, AUC):
    R = []
    if bol == True: # Test
        R.append(mod + " Test Results \n")
        R.append("TPR: " + str(TPR) + '\n')
        R.append("PPV: " + str(PPV) + '\n')
        R.append("ACC: " + str(ACC) + '\n')
        R.append("F1: " + str(F1) + '\n')
        R.append("MCC: " + str(MCC) + '\n')
        R.append("AUC: " + str(AUC) + '\n')
    else: # Cross-Validation
        R.append(mod + " 10-fold Cross Validation Results \n")
        for it in range(10):
            R.append("The " + str(it + 1) + "-fold \n")
            R.append("TPR: " + str(TPR[it]) + '\n')
            R.append("PPV: " + str(PPV[it]) + '\n')
            R.append("ACC: " + str(ACC[it]) + '\n')
            R.append("F1: " + str(F1[it]) + '\n')
            R.append("MCC: " + str(MCC[it]) + '\n')
            R.append("AUC: " + str(AUC[it]) + '\n')
        R.append("The average results \n")
        R.append("TPR: " + str(np.mean(TPR)) + '\n')
        R.append("PPV: " + str(np.mean(PPV)) + '\n')
        R.append("ACC: " + str(np.mean(ACC)) + '\n')
        R.append("F1: " + str(np.mean(F1)) + '\n')
        R.append("MCC: " + str(np.mean(MCC)) + '\n')
        R.append("AUC: " + str(np.mean(AUC)) + '\n')
    return R

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
    if args.all_feature == "True":
        w1 = open('Complex Features without Ranking (TrainingValidationSet).fasta', 'w')
        w1.writelines(cf_tv_set)
        w1.close()
        if cf_test_set is not "None":
            w2 = open('Complex Features without Ranking (TestSet).fasta', 'w')
            w2.writelines(cf_test_set)
            w2.close()
    # output ranked complex features
    if args.ranked_feature == "True":
        w3 = open('Ranked Complex Features (TrainingValidationSet).fasta', 'w')
        w3.writelines(rcf_tv_set)
        w3.close()
        if rcf_test_set is not "None":
            w4 = open('Ranked Complex Features (TestSet).fasta', 'w')
            w4.writelines(rcf_test_set)
            w4.close()
    # output retained complex features
    if args.retained_feature == "True":
        w5 = open('Retained Complex Features (TrainingValidationSet).fasta', 'w')
        w5.writelines(scf_tv_set)
        w5.close()
        if scf_test_set is not "None":
            w6 = open('Retained Complex Features (TestSet).fasta', 'w')
            w6.writelines(scf_test_set)
            w6.close()
    # Training and Prediction
    Res = []
    # Random Forest predicting
    if args.rf == "True":
        if args.test_set is not "None":
            TPR, PPV, ACC, F1, MCC, AUC = Test(X_train, y_train, X_test, y_test, "rf")
            Res = ResultOutput(True, "Random Forest", TPR, PPV, ACC, F1, MCC, AUC)
        else:
            TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum = CrossValidation(X_train, y_train, "rf")
            Res = ResultOutput(False, "Random Forest", TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum)
    # Support Vector Machine predicting
    if args.svm == "True":
        if args.test_set is not "None":
            TPR, PPV, ACC, F1, MCC, AUC = Test(X_train, y_train, X_test, y_test, "svm")
            Res = ResultOutput(True, "Support Vector Machine", TPR, PPV, ACC, F1, MCC, AUC)
        else:
            TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum = CrossValidation(X_train, y_train, "svm")
            Res = ResultOutput(False, "Support Vector Machine", TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum)
    # Logistic Regression predicting
    if args.lr == "True":
        if args.test_set is not "None":
            TPR, PPV, ACC, F1, MCC, AUC = Test(X_train, y_train, X_test, y_test, "lr")
            Res = ResultOutput(True, "Logistic Regression", TPR, PPV, ACC, F1, MCC, AUC)
        else:
            TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum = CrossValidation(X_train, y_train, "lr")
            Res = ResultOutput(False, "Logistic Regression", TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum)
    # Gradient Boosting predicting
    if args.gb == "True":
        if args.test_set is not "None":
            TPR, PPV, ACC, F1, MCC, AUC = Test(X_train, y_train, X_test, y_test, "gb")
            Res = ResultOutput(True, "Gradient Boosting", TPR, PPV, ACC, F1, MCC, AUC)
        else:
            TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum = CrossValidation(X_train, y_train, "gb")
            Res = ResultOutput(False, "Gradient Boosting", TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum)
    # K-Nearest Neighbour predicting
    if args.knn == "True":
        if args.test_set is not "None":
            TPR, PPV, ACC, F1, MCC, AUC = Test(X_train, y_train, X_test, y_test, "knn")
            Res = ResultOutput(True, "K-Nearest Neighbour", TPR, PPV, ACC, F1, MCC, AUC)
        else:
            TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum = CrossValidation(X_train, y_train, "knn")
            Res = ResultOutput(False, "K-Nearest Neighbour", TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum)
    # Gaussian Naive Bayes predicting
    if args.nb == "True":
        if args.test_set is not "None":
            TPR, PPV, ACC, F1, MCC, AUC = Test(X_train, y_train, X_test, y_test, "nb")
            Res = ResultOutput(True, "Naive Bayes", TPR, PPV, ACC, F1, MCC, AUC)
        else:
            TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum = CrossValidation(X_train, y_train, "nb")
            Res = ResultOutput(False, "Naive Bayes", TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum)
    # Decision Tree predicting
    if args.dt == "True":
        if args.test_set is not "None":
            TPR, PPV, ACC, F1, MCC, AUC = Test(X_train, y_train, X_test, y_test, "dt")
            Res = ResultOutput(True, "Decision Tree", TPR, PPV, ACC, F1, MCC, AUC)
        else:
            TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum = CrossValidation(X_train, y_train, "dt")
            Res = ResultOutput(False, "Decision Tree", TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum)
    # Output
    if Res is not []:
        w = open('Prediction Results.fasta', 'w')
        w.writelines(Res)
        w.close()

def main():
    args = args_parser()
    RNAIFRID(args)
    print(args.all_feature)
    print(args.ranked_feature)
    print(args.retained_feature)

if __name__ == '__main__':
    main()
