#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

### finding max and min in 'exercised_stock_options' or 'salary'
import sys
max=-(sys.maxsize)
min=sys.maxsize
for key in data_dict:
    if data_dict[key]['salary']!='NaN':
        if data_dict[key]['salary']>max:
            max=data_dict[key]['salary']
        elif data_dict[key]['salary']<min:
            min=data_dict[key]['salary']
print "Max:",max
print "Min:",min


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
### adding 3rd feature
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
### changing for three features
for f1, f2, _ in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans
clf=KMeans(n_clusters=3)
clf.fit(finance_features)
pred=clf.predict(finance_features)

###Lesson-9 mini-project Scaling
from sklearn.preprocessing import MinMaxScaler

rescaled_salary=numpy.empty(shape=(len(finance_features),1))
rescaled_exercised_stock_options=numpy.empty(shape=(len(finance_features),1))
j=0
for f1,f2,_ in finance_features:
    rescaled_salary[j][0]=f1
    rescaled_exercised_stock_options[j][0]=f2
    j+=1

scaler = MinMaxScaler()
rescaled_salary=scaler.fit_transform(rescaled_salary)
rescaled_exercised_stock_options=scaler.fit_transform(rescaled_exercised_stock_options)

# print rescaled_salary
# print rescaled_exercised_stock_options


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
### changing name parameter for new pdf file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="3clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
