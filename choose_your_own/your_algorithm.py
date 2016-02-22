#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

###myImports
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

###myCode

#<--RandomForestClassifier-->#
clfrfc=RandomForestClassifier()
clfrfc.fit(features_train, labels_train)
predrfc=clfrfc.predict(features_test)
print "RandomForestClassifier Accuracy:",accuracy_score(predrfc,labels_test)

#<--AdaBoostClassifier-->#
clfada=AdaBoostClassifier()
clfada.fit(features_train,labels_train)
predada=clfada.predict(features_test)
print "AdaBoostClassifier Accuracy:",accuracy_score(predada,labels_test)

#<--KNeighborsClassifier-->#
clfkn=KNeighborsClassifier(n_neighbors=22)
clfkn.fit(features_train,labels_train)
predkn=clfkn.predict(features_test)
print "KNeighborsClassifier Accuracy:",accuracy_score(predkn,labels_test)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
