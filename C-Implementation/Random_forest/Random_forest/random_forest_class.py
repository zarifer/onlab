import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

dataset_mw = pd.read_csv('/home/nimda/Documents/outputs/malset1/dataset_mw.csv')
dataset_bn = pd.read_csv('/home/nimda/Documents/outputs/malset1/dataset_bn.csv')
dataset_mw["Hit"] = 1
dataset_bn["Hit"] = 0
#Concat merge together the two database
dataset = pd.concat([dataset_mw, dataset_bn])
print(dataset.head())
#print(dataset_mw.head())
#print(dataset_bn.head())

X = dataset.iloc[:, 0:24].values
Y = dataset.iloc[:, 24].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

#sc = StandardScaler()
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)
#Y_train = sc.fit_transform(Y_train)
#Y_test = sc.transform(Y_test)

clf = RandomForestClassifier(n_estimators=20, random_state=0)
#print(X_train)
#print(Y_train)

clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)

print('Accuracy score: ', metrics.accuracy_score(Y_test, Y_pred))
print('Confusion matrix: ')
print(metrics.confusion_matrix(Y_test, Y_pred))
print('Classification report: ')
print(metrics.classification_report(Y_test, Y_pred))

dataset_merged = pd.read_csv('/home/nimda/Documents/outputs/malset1/dataset_merged.csv')
merged_pred = clf.predict(dataset_merged)
print('Prediction for merge file: \n', merged_pred)
