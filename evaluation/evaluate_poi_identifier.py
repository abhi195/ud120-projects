#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


### your code goes here 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score
from sklearn import cross_validation

features_train,features_test,labels_train,labels_test = cross_validation.train_test_split(features,labels,test_size=0.3,random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)

pred = clf.predict(features_test)
print "predictions_labels_test:",pred
print "acutal_labels_test:",labels_test

print clf.score(features_test,labels_test)

print "precision_score:",precision_score(pred,labels_test)
print "recall_score:",recall_score(pred,labels_test)

predicted_poi_testset=0
for poi in labels_test:
	if poi==1.0:
		predicted_poi_testset+=1
print "predicted_poi_testset:",predicted_poi_testset
print "total_test_people_count:",len(labels_test)

print "total_train_people_count",len(labels_train)

# hypothetical test set
predictions = [0., 1., 1., 0., 0., 0., 1., 0., 1., 0., 0., 1., 0., 0., 1., 1., 0., 1., 0., 1.] 
true_labels = [0., 0., 0., 0., 0., 0., 1., 0., 1., 1., 0., 1., 0., 1., 1., 1., 0., 1., 0., 0.]
print "hypothetical_test_set_precision_score",precision_score(predictions,true_labels)
print "hypothetical_test_set_recall_score",recall_score(predictions,true_labels)