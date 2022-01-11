# Model processing

import numpy as np
from sklearn import linear_model, neighbors, ensemble, svm, naive_bayes, tree
from sklearn.metrics import recall_score, precision_score, accuracy_score, f1_score, matthews_corrcoef, roc_auc_score
from keras.utils import np_utils
np.random.seed(1337) # random seed

def SupportVectorMachine(X_train, y_train):
    SVMStruct = svm.SVC(probability=True)
    SVMStruct.fit(X_train, y_train)
    # # save model
    # SVMname = 'SVM.pkl'
    # joblib.dump(SVMStruct, SVMname)
    return SVMStruct

def LogisticRegression(X_train, y_train):
    LRStruct = linear_model.LogisticRegression()
    LRStruct.fit(X_train, y_train)
    # # save model
    # LRname = 'LR.pkl'
    # joblib.dump(LRStruct, LRname)
    return LRStruct

def RandomForest(X_train, y_train):
    RFStruct = ensemble.RandomForestClassifier()
    RFStruct.fit(X_train, y_train)
    # # save model
    # RFname = 'RF.pkl'
    # joblib.dump(RFStruct, RFname)
    return RFStruct

def GradientBoosting(X_train, y_train):
    GBStruct = ensemble.GradientBoostingClassifier()
    GBStruct.fit(X_train, y_train)
    # # save model
    # GBname = strain + '-GB.pkl'
    # joblib.dump(GBStruct, GBname)
    return GBStruct

def KNearestNeighbour(X_train, y_train):
    KNNStruct = neighbors.KNeighborsClassifier()
    KNNStruct.fit(X_train, y_train)
    # # save model
    # KNNname = strain + '-KNN.pkl'
    # joblib.dump(KNNStruct, KNNname)
    return KNNStruct

def GaussianNaiveBayes(X_train, y_train):
    NBStruct = naive_bayes.GaussianNB()
    NBStruct.fit(X_train, y_train)
    # # save model
    # NBname = strain + '-NB.pkl'
    # joblib.dump(NBStruct, NBname)
    return NBStruct

def DecisionTree(X_train, y_train):
    DTStruct = tree.DecisionTreeClassifier()
    DTStruct.fit(X_train, y_train)
    # # save model
    # DTname = strain + '-DT.pkl'
    # joblib.dump(DTStruct, DTname)
    return DTStruct

def ModelTraining(X_train, y_train, Model):
    if Model == "svm":
        Struct = SupportVectorMachine(X_train, y_train)
    elif Model == "lr":
        Struct = LogisticRegression(X_train, y_train)
    elif Model == "rf":
        Struct = RandomForest(X_train, y_train)
    elif Model == "gb":
        Struct = GradientBoosting(X_train, y_train)
    elif Model == "knn":
        Struct = KNearestNeighbour(X_train, y_train)
    elif Model == "nb":
        Struct = GaussianNaiveBayes(X_train, y_train)
    elif Model == "dt":
        Struct = DecisionTree(X_train, y_train)
    else:
        return
    return Struct

def ResultEvaluation(y_test, group, score):
    TPR = recall_score(y_test, group)
    PPV = precision_score(y_test, group)
    ACC = accuracy_score(y_test, group)
    F1 = f1_score(y_test, group)
    MCC = matthews_corrcoef(y_test, group)
    AUC = roc_auc_score(y_test, score)
    return TPR, PPV, ACC, F1, MCC, AUC

def Test(X_train, y_train, X_test, y_test, Model):
    y_test = np.array(y_test).astype('int').reshape(-1, 1)
    y_test = np_utils.to_categorical(y_test, num_classes=2)
    Struct = ModelTraining(X_train, y_train, Model)
    group = Struct.predict(X_test)
    score = Struct.predict_proba(X_test)
    TPR, PPV, ACC, F1, MCC, AUC = ResultEvaluation(y_test, group, score)
    return TPR, PPV, ACC, F1, MCC, AUC

def CrossValidation(X, y, Model):
    TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum = [], [], [], [], [], []
    strKFold = StratifiedKFold(n_splits=10, shuffle=False, random_state=0)
    for index, (train_index, test_index) in enumerate(strKFold.split(X, y)):
        X_train, X_test, y_train, y_test = np.array(X)[train_index], np.array(X)[test_index], np.array(y)[train_index], np.array(y)[test_index]
        Struct = ModelTraining(X_train, y_train, Model)
        group = Struct.predict(X_test)
        score = Struct.predict_proba(X_test)
        TPR, PPV, ACC, F1, MCC, AUC = ResultEvaluation(y_test, group, score)
        TPRsum.append(TPR)
        PPVsum.append(PPV)
        ACCsum.append(ACC)
        F1sum.append(F1)
        MCCsum.append(MCC)
        AUCsum.append(AUC)
    return TPRsum, PPVsum, ACCsum, F1sum, MCCsum, AUCsum