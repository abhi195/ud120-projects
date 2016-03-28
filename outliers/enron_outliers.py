#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

###<---myCode--->
###for identifying key
for i in data_dict:
	if data_dict[i]['salary']==26704229 and data_dict[i]['bonus']==97343619:
		name=i
		print "Name of outlier:",i
###deleting outlier from dict
#data_dict.pop('TOTAL',0)
data_dict.pop(name,0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

###determining max salary and bonus related to outlier
# max1=0
# max2=0
# for i in data:
# 	if i[0]>max1:
# 		max1=i[0]
# 	if i[1]>max2:
# 		max2=i[1]
# print "Salary of outlier:",max1
# print "Bonus of outlier:",max2

###determining two more outlier after removing TOTAL
for i in data_dict:
	if data_dict[i]['salary']!='NaN' and data_dict[i]['bonus']!='NaN':
		if data_dict[i]['salary']>1000000 and data_dict[i]['bonus']>5000000:
			print i

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()