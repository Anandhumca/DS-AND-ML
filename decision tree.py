import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score

#load the dataset

data=load_iris()
print("data shape:",data.data.shape)
print("classes to predict:",data.target_names)
print("features:",data.feature_names)

#define features and target

X=data.data
y=data.target
print("feature shape:",X.shape)
print("target shape:",y.shape)

#split dataset

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=50,test_size=0.25)

#------------------gini---------------------

clf_gini=DecisionTreeClassifier()
clf_gini.fit(X_train,y_train)
y_pred_gini=clf_gini.predict(X_test)

print("\n-----using gini---------")
print("Accuracy on train data:",accuracy_score(y_train,clf_gini.predict(X_train)))
print("Accuracy on test data:",accuracy_score(y_test,y_pred_gini))

#---------------entropy---------------
clf_entropy=DecisionTreeClassifier(criterion='entropy')
clf_entropy.fit(X_train,y_train)
y_pred_entropy=clf_entropy.predict(X_test)

print("\n-----------using entropy-------")
print("Accuracy on train data:",accuracy_score(y_train,clf_entropy.predict(X_train)))
print("Accuracy on test data:",accuracy_score(y_test,y_pred_entropy))

#------------entropy+min_samples_split------------

clf_entropy_split=DecisionTreeClassifier(criterion='entropy',min_samples_split=50)
clf_entropy_split.fit(X_train,y_train)
y_pred_entropy_split=clf_entropy_split.predict(X_test)

print("\n-----------using entropy with min_samples_split=50-----")
print("Accuracy on train data:",accuracy_score(y_train,clf_entropy_split.predict(X_train)))
print("Accuracy on tes data:",accuracy_score(y_test,y_pred_entropy_split))

#------------visualization----------

plt.figure(figsize=(12,8))
plot_tree(clf_entropy,
          filled=True,
          feature_names=data.feature_names,
          class_names=data.target_names)
plt.title("Decision tree(entropy)")
plt.show()
