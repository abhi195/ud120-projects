#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# <--No of Features and size of enron dataset--> #
# print len(enron_data['METTS MARK'])

# <--No of poi's in enron dataset--> #
# poino=0
# for i in enron_data:
# 	if enron_data[i]['poi']==True:
# 		poino+=1
# print poino

noPayments=0
pois=0
for i in enron_data:
	if enron_data[i]['poi']==True:
		pois+=1
		if enron_data[i]['total_payments']=='NaN':
			noPayments+=1
print noPayments
print pois

# print enron_data["LAY KENNETH L"]["total_payments"]

# print enron_data["FASTOW ANDREW S"]["total_payments"]

# print enron_data["SKILLING JEFFREY K"]["total_payments"]