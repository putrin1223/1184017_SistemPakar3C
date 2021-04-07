# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:07:18 2021

@author: Putri Nella
"""

import pandas as pd
import numpy as np
import math
from scipy.sparse import *
from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from pandas import DataFrame

trainData = pd.read_csv('train.data', sep=' ',header=None,names=['docId','wordId','count'])
trainLabels = pd.read_csv('train.label')

testData = pd.read_csv('test.data', sep=' ',header=None,names=['docId','wordId','count'])
testLabels = pd.read_csv('test.label')



df = pd.DataFrame(data=0, index = np.arange(11268), columns = np.arange(53976))

length=0
inner=0
index=0
Doclength = len(set(trainData.wordId))
for i in range (11267):
    df.set_value([trainData.docId[i]], [trainData.wordId[i]], 1)  
    

model = DecisionTreeClassifier()
model.fit(df,trainLabels)
print("Model is -")
print("Prediction is - ")

testData = testData[(testData.wordId.isin(trainData.wordId))]
trainData=None
trainLabels=None
testLabels=None
df=None
del index
del length
del testLabels
ef=pd.DataFrame(data=0, index = np.arange(11268), columns = np.arange(53976))


for j in range(11267):
    ef.set_value([j],[testData.wordId[j]],1)
from sklearn.naive_bayes import BernoulliNB
bernaulli = BernoulliNB()
bernaulli.fit(df, trainLabels)
BernoulliNB(alpha=0.0, binarize=0.0, class_prior=None, fit_prior=True)
print(clf.predict(ef))