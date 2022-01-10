# Feature processing

import numpy as np
import re
import math
from sklearn import ensemble
np.random.seed(1337) # random seed

separator, Sequencekmertotal, SequenceGgaptotal, Structurekmertotal, StructureGgaptotal = ' ', 3, 3, 3, 3

def SequencekmerExtract(sequence, totalkmer):
    sequence = sequence.replace('U', 'T')
    character = 'ATCG'
    sequencekmer = ''
    for k in range(totalkmer):
        kk = k + 1
        sk = len(sequence) - kk + 1
        wk = 1 / (4 ** (totalkmer - kk))
        # 1-mer
        if kk == 1:
            for char11 in character:
                s1 = char11
                f1 = wk * sequence.count(s1) / sk
                string1 = str(f1) + separator
                sequencekmer = sequencekmer + string1
        # 2-mer
        if kk == 2:
            for char21 in character:
                for char22 in character:
                    s2 = char21 + char22
                    numkmer2 = 0
                    for lkmer2 in range(len(sequence) - kk + 1):
                        if sequence[lkmer2] == s2[0] and sequence[lkmer2 + 1] == s2[1]:
                            numkmer2 = numkmer2 + 1
                    f2 = wk * numkmer2 / sk
                    string2 = str(f2) + separator
                    sequencekmer = sequencekmer + string2
        # 3-mer
        if kk == 3:
            for char31 in character:
                for char32 in character:
                    for char33 in character:
                        s3 = char31 + char32 + char33
                        numkmer3 = 0
                        for lkmer3 in range(len(sequence) - kk + 1):
                            if sequence[lkmer3] == s3[0] and sequence[lkmer3 + 1] == s3[1] and sequence[lkmer3 + 2] == s3[2]:
                                numkmer3 = numkmer3 + 1
                        f3 = wk * numkmer3 / sk
                        string3 = str(f3) + separator
                        sequencekmer = sequencekmer + string3
        # 4-mer
        if kk == 4:
            for char41 in character:
                for char42 in character:
                    for char43 in character:
                        for char44 in character:
                            s4 = char41 + char42 + char43 + char44
                            numkmer4 = 0
                            for lkmer4 in range(len(sequence) - kk + 1):
                                if sequence[lkmer4] == s4[0] and sequence[lkmer4 + 1] == s4[1] and sequence[lkmer4 + 2] == s4[2] and sequence[lkmer4 + 3] == s4[3]:
                                    numkmer4 = numkmer4 + 1
                            f4 = wk * numkmer4 / sk
                            string4 = str(f4) + separator
                            sequencekmer = sequencekmer + string4
        # 5-mer
        if kk == 5:
            for char51 in character:
                for char52 in character:
                    for char53 in character:
                        for char54 in character:
                            for char55 in character:
                                s5 = char51 + char52 + char53 + char54 + char55
                                numkmer5 = 0
                                for lkmer5 in range(len(sequence) - kk + 1):
                                    if sequence[lkmer5] == s5[0] and sequence[lkmer5 + 1] == s5[1] and sequence[lkmer5 + 2] == s5[2] and sequence[lkmer5 + 3] == s5[3] and sequence[lkmer5 + 4] == s5[4]:
                                        numkmer5 = numkmer5 + 1
                                f5 = wk * numkmer5 / sk
                                string5 = str(f5) + separator
                                sequencekmer = sequencekmer + string5
        # 6-mer
        if kk == 6:
            for char61 in character:
                for char62 in character:
                    for char63 in character:
                        for char64 in character:
                            for char65 in character:
                                for char66 in character:
                                    s6 = char61 + char62 + char63 + char64 + char65 + char66
                                    numkmer6 = 0
                                    for lkmer6 in range(len(sequence) - kk + 1):
                                        if sequence[lkmer6] == s6[0] and sequence[lkmer6 + 1] == s6[1] and sequence[lkmer6 + 2] == s6[2] and sequence[lkmer6 + 3] == s6[3] and sequence[lkmer6 + 4] == s6[4] and sequence[lkmer6 + 5] == s6[5]:
                                            numkmer6 = numkmer6 + 1
                                    f6 = wk * numkmer6 / sk
                                    string6 = str(f6) + separator
                                    sequencekmer = sequencekmer + string6
    return sequencekmer

def SequenceGgapExtract(sequence, totalGgap):
    sequence = sequence.replace('U', 'T')
    character = 'ATCG'
    sequenceGgap = ''
    for k in range(totalGgap):
        kk = k + 1
        sk = len(sequence) - kk + 1
        wk = 1 / (4 ** (totalGgap - kk))
        if kk == 1:
            for char11 in character:
                for char12 in character:
                    num1 = 0
                    for l1 in range(len(sequence) - kk - 1):
                        if sequence[l1] == char11 and sequence[l1 + kk + 1] == char12:
                            num1 = num1 + 1
                    f1 = wk * num1 / sk
                    string1 = str(f1) + separator
                    sequenceGgap = sequenceGgap + string1
        if kk == 2:
            for char21 in character:
                for char22 in character:
                    num2 = 0
                    for l2 in range(len(sequence) - kk - 3):
                        if sequence[l2] == char21 and sequence[l2 + kk + 1] == char22:
                            num2 = num2 + 1
                    f2 = wk * num2 / sk
                    string2 = str(f2) + separator
                    sequenceGgap = sequenceGgap + string2
        if kk == 3:
            for char31 in character:
                for char32 in character:
                    num3 = 0
                    for l3 in range(len(sequence) - kk - 3):
                        if sequence[l3] == char31 and sequence[l3 + kk + 1] == char32:
                            num3 = num3 + 1
                    f3 = wk * num3 / sk
                    string3 = str(f3) + separator
                    sequenceGgap = sequenceGgap + string3
        if kk == 4:
            for char41 in character:
                for char42 in character:
                    num4 = 0
                    for l4 in range(len(sequence) - kk - 3):
                        if sequence[l4] == char41 and sequence[l4 + kk + 1] == char42:
                            num4 = num4 + 1
                    f4 = wk * num4 / sk
                    string4 = str(f4) + separator
                    sequenceGgap = sequenceGgap + string4
        if kk == 5:
            for char51 in character:
                for char52 in character:
                    num5 = 0
                    for l5 in range(len(sequence) - kk - 3):
                        if sequence[l5] == char51 and sequence[l5 + kk + 1] == char52:
                            num5 = num5 + 1
                    f5 = wk * num5 / sk
                    string5 = str(f5) + separator
                    sequenceGgap = sequenceGgap + string5
    return sequenceGgap

def StructurekmerExtract(structure, totalkmer):
    character = ').'
    structurekmer = '' # 特征

    sp = structure.split()
    ssf = sp[0]
    ssf = ssf.replace('(', ')')
    for k in range(totalkmer):
        kk = k + 1
        sk = len(ssf) - kk + 1
        wk = 1 / (2 ** (totalkmer - kk))
        # 1-mer
        if kk == 1:
            for char11 in character:
                s1 = char11
                f1 = wk * ssf.count(s1) / sk
                string1 = str(f1) + separator
                structurekmer = structurekmer + string1
        # 2-mer
        if kk == 2:
            for char21 in character:
                for char22 in character:
                    s2 = char21 + char22
                    numkmer2 = 0
                    for lkmer2 in range(len(ssf) - kk + 1):
                        if ssf[lkmer2] == s2[0] and ssf[lkmer2 + 1] == s2[1]:
                            numkmer2 = numkmer2 + 1
                    f2 = wk * numkmer2 / sk
                    string2 = str(f2) + separator
                    structurekmer = structurekmer + string2
        # 3-mer
        if kk == 3:
            for char31 in character:
                for char32 in character:
                    for char33 in character:
                        s3 = char31 + char32 + char33
                        numkmer3 = 0
                        for lkmer3 in range(len(ssf) - kk + 1):
                            if ssf[lkmer3] == s3[0] and ssf[lkmer3 + 1] == s3[1] and ssf[lkmer3 + 2] == s3[2]:
                                numkmer3 = numkmer3 + 1
                        f3 = wk * numkmer3 / sk
                        string3 = str(f3) + separator
                        structurekmer = structurekmer + string3
        # 4-mer
        if kk == 4:
            for char41 in character:
                for char42 in character:
                    for char43 in character:
                        for char44 in character:
                            s4 = char41 + char42 + char43 + char44
                            numkmer4 = 0
                            for lkmer4 in range(len(ssf) - kk + 1):
                                if ssf[lkmer4] == s4[0] and ssf[lkmer4 + 1] == s4[1] and ssf[lkmer4 + 2] == s4[2] and ssf[lkmer4 + 3] == s4[3]:
                                    numkmer4 = numkmer4 + 1
                            f4 = wk * numkmer4 / sk
                            string4 = str(f4) + separator
                            structurekmer = structurekmer + string4
        # 5-mer
        if kk == 5:
            for char51 in character:
                for char52 in character:
                    for char53 in character:
                        for char54 in character:
                            for char55 in character:
                                s5 = char51 + char52 + char53 + char54 + char55
                                numkmer5 = 0
                                for lkmer5 in range(len(ssf) - kk + 1):
                                    if ssf[lkmer5] == s5[0] and ssf[lkmer5 + 1] == s5[1] and ssf[lkmer5 + 2] == s5[2] and ssf[lkmer5 + 3] == s5[3] and ssf[lkmer5 + 4] == s5[4]:
                                        numkmer5 = numkmer5 + 1
                                f5 = wk * numkmer5 / sk
                                string5 = str(f5) + separator
                                structurekmer = structurekmer + string5
    return structurekmer

def StructureGgapExtract(structure, totalGgap):
    character = ').'
    structureGgap = ''
    sp = structure.split()
    ssf = sp[0]
    ssf = ssf.replace('(', ')')
    for k in range(totalGgap):
        kk = k + 1
        sk = len(ssf) - kk + 1
        wk = 1 / (2 ** (totalGgap - kk))
        if kk == 1:
            for char11 in character:
                for char12 in character:
                    for char13 in character:
                        for char14 in character:
                            num1 = 0
                            for l1 in range(len(ssf) - kk - 3):
                                if ssf[l1] == char11 and ssf[l1 + 1] == char12 and ssf[l1 + kk + 2] == char13 and ssf[l1 + kk + 3] == char14:
                                    num1 = num1 + 1
                            f1 = wk * num1 / sk
                            string1 = str(f1) + separator
                            structureGgap = structureGgap + string1
        if kk == 2:
            for char21 in character:
                for char22 in character:
                    for char23 in character:
                        for char24 in character:
                            num2 = 0
                            for l2 in range(len(ssf) - kk - 3):
                                if ssf[l2] == char21 and ssf[l2 + 1] == char22 and ssf[l2 + kk + 2] == char23 and ssf[l2 + kk + 3] == char24:
                                    num2 = num2 + 1
                            f2 = wk * num2 / sk
                            string2 = str(f2) + separator
                            structureGgap = structureGgap + string2
        if kk == 3:
            for char31 in character:
                for char32 in character:
                    for char33 in character:
                        for char34 in character:
                            num3 = 0
                            for l3 in range(len(ssf) - kk - 3):
                                if ssf[l3] == char31 and ssf[l3 + 1] == char32 and ssf[l3 + kk + 2] == char33 and ssf[l3 + kk + 3] == char34:
                                    num3 = num3 + 1
                            f3 = wk * num3 / sk
                            string3 = str(f3) + separator
                            structureGgap = structureGgap + string3
        if kk == 4:
            for char41 in character:
                for char42 in character:
                    for char43 in character:
                        for char44 in character:
                            num4 = 0
                            for l4 in range(len(ssf) - kk - 3):
                                if ssf[l4] == char41 and ssf[l4 + 1] == char42 and ssf[l4 + kk + 2] == char43 and ssf[l4 + kk + 3] == char44:
                                    num4 = num4 + 1
                            f4 = wk * num4 / sk
                            string4 = str(f4) + separator
                            structureGgap = structureGgap + string4
        if kk == 5:
            for char51 in character:
                for char52 in character:
                    for char53 in character:
                        for char54 in character:
                            num5 = 0
                            for l5 in range(len(ssf) - kk - 3):
                                if ssf[l5] == char51 and ssf[l5 + 1] == char52 and ssf[l5 + kk + 2] == char53 and ssf[l5 + kk + 3] == char54:
                                    num5 = num5 + 1
                            f5 = wk * num5 / sk
                            string5 = str(f5) + separator
                            structureGgap = structureGgap + string5
    return structureGgap

def ArithmeticLevel(feature1, feature2):
    fpair = ''
    if feature1 != '' and feature2 != '':
        f1, f2 = feature1.strip().split(' '), feature2.strip().split(' ')
        for i in range(len(f1)):
            a = float(f1[i])
            b = float(f2[i])
            c = 50 * (a + b) / 2
            fpair += str(c) + separator
    return fpair

def FeatureConstruction(ListPair):
    ComplexFeatureVector = []
    for LinePair in ListPair:
        RNAiname, RNAjname, RNAisequence, RNAjsequence, RNAistructure, RNAjstructure, label = LinePair.strip().split(',')
        # RNAi sequence k-mer
        SequenceRNAikmer = SequencekmerExtract(RNAisequence, Sequencekmertotal)
        # RNAi sequence g-gap
        SequenceRNAiGgap = SequenceGgapExtract(RNAisequence, SequenceGgaptotal)
        # RNAi structure k-mer
        StructureRNAikmer = StructurekmerExtract(RNAistructure, Structurekmertotal)
        # RNAi structure g-gap
        StructureRNAiGgap = StructureGgapExtract(RNAistructure, StructureGgaptotal)
        # RNAj sequence k-mer
        SequenceRNAjkmer = SequencekmerExtract(RNAjsequence, Sequencekmertotal)
        # RNAj sequence g-gap
        SequenceRNAjGgap = SequenceGgapExtract(RNAjsequence, SequenceGgaptotal)
        # RNAj structure k-mer
        StructureRNAjkmer = StructurekmerExtract(RNAjstructure, Structurekmertotal)
        # RNAj structure g-gap
        StructureRNAjGgap = StructureGgapExtract(RNAjstructure, StructureGgaptotal)
        # Complex Feature
        sequencekmer = ArithmeticLevel(SequenceRNAikmer, SequenceRNAjkmer)
        sequenceGgap = ArithmeticLevel(SequenceRNAiGgap, SequenceRNAjGgap)
        structurekmer = ArithmeticLevel(StructureRNAikmer, StructureRNAjkmer)
        structureGgap = ArithmeticLevel(StructureRNAiGgap, StructureRNAjGgap)
        # Fusion
        FeatureLine = sequencekmer + sequenceGgap + structurekmer + structureGgap + label + '\n'
        ComplexFeatureVector.append(FeatureLine)
    return ComplexFeatureVector

def FeatureConversion(ListPair):
    NumberRow = len(ListPair)
    NumberColumn = len(ListPair[0].split()) - 1
    X = [([0] * NumberColumn) for p in range(NumberRow)]
    y = [([0] * 1) for p in range(NumberRow)]
    for IndexData in range(NumberRow):
        Line = ListPair[IndexData]
        SetData = re.split(r'\s', Line)
        for ItData in range(len(SetData) - 1):
            if ItData < len(SetData) - 2:
                X[IndexData][ItData] = float(SetData[ItData])
            else:
                y[IndexData][0] = float(SetData[ItData])
    return X, y

def RFFeatureRanking(X_train, y_train):
    clf = ensemble.RandomForestClassifier()
    clf.fit(X_train, y_train)
    importance = clf.feature_importances_
    indices = np.argsort(importance)[::-1]
    # score = clf.feature_importances_[indices]
    return indices

def ETFeatureRanking(X_train, y_train):
    clf = ensemble.ExtraTreesClassifier()
    clf.fit(X_train, y_train)
    importance = clf.feature_importances_
    indices = np.argsort(importance)[::-1]
    # score = clf.feature_importances_[indices]
    return indices, importance

def GBFeatureRanking(X_train, y_train):
    clf = ensemble.GradientBoostingClassifier()
    clf.fit(X_train, y_train)
    importance = clf.feature_importances_
    indices = np.argsort(importance)[::-1]
    # score = clf.feature_importances_[indices]
    return indices, importance

def FeatureRanking(X_train, y_train, X_test, y_test):
    indices = RFFeatureRanking(X_train, y_train)
    TVRankedFeature = []
    for IndexSample in range(len(X_train)):
        Feature = list(map(str, X_train[IndexSample]))
        Label = str(int(y_train[IndexSample][0]))
        String = ''
        for ind in indices:
            String = String + Feature[ind] + ' '
        String = String + Label + '\n'
        TVRankedFeature.append(String)
    if X_test is not "None":
        TestRankedFeature = []
        for IndexSample2 in range(len(X_test)):
            Feature2 = list(map(str, X_test[IndexSample2]))
            Label2 = str(int(y_test[IndexSample2][0]))
            String2 = ''
            for ind2 in indices:
                String2 = String2 + Feature2[ind2] + ' '
            String2 = String2 + Label2 + '\n'
            TestRankedFeature.append(String2)
    else:
        TestRankedFeature = "None"
    return TVRankedFeature, TestRankedFeature, indices

def FeatureSelection(X_train, y_train, IndicesRF, rcf_tv_set, rcf_test_set):
    NumberFeature = len(IndicesRF)
    p = 0.05
    Threshold = 1 / NumberFeature * math.e * p * 0.5
    IndicesET, ImportanceET = ETFeatureRanking(X_train, y_train)
    IndicesGB, ImportanceGB = GBFeatureRanking(X_train, y_train)
    IndicesET = list(map(int, IndicesET))
    IndicesGB = list(map(int, IndicesGB))
    count = 0
    for num in range(NumberFeature):
        ind = IndicesRF[num]
        iET, iGB = IndicesET.index(ind) + 1, IndicesGB.index(ind) + 1
        ins = ((ImportanceET[ind] + ImportanceGB[ind]) / 2) * (((NumberFeature - iET) / NumberFeature + (NumberFeature - iGB) / NumberFeature) / 2)
        if ins < Threshold:
            count += 1
        if count >= p * (num + 1) and num + 1 >= 10:
            num += 1
            break
    TVSelectedFeature = []
    for Line in rcf_tv_set:
        string = ''
        sample = Line.strip().split(' ')
        label = sample[-1]
        for j in range(num):
            string = string + sample[j] + ' '
        string = string + label + '\n'
        TVSelectedFeature.append(string)
    if rcf_test_set is not "None":
        TestSelectedFeature = []
        for Line2 in rcf_test_set:
            string2 = ''
            sample2 = Line2.strip().split(' ')
            label2 = sample2[-1]
            for j2 in range(num):
                string2 = string2 + sample2[j] + ' '
            string2 = string2 + label2 + '\n'
            TestSelectedFeature.append(string2)
    else:
        TestSelectedFeature = "None"
    return TVSelectedFeature, TestSelectedFeature
