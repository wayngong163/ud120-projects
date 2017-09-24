#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop( "TOTAL", 0 )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

salary = [[x[0]] for x in data]
bonus  = [[x[1]] for x in data]

salary_train = salary[:int(0.9*len(salary))]
salary_test  = salary[int(0.9*len(salary)):]
bonus_train  = bonus[:int(0.9*len(bonus))]
bonus_test   = bonus[int(0.9*len(bonus)):]



### your code below
from time import time
from sklearn.linear_model import LinearRegression
t0 = time()
reg = LinearRegression()
reg.fit(salary_train, bonus_train)
t1 = time()
print "training time:%.2fs" % (t1-t0)

print "Training Score:%.4f" % reg.score(salary_train, bonus_train)
print "Test Score:%.4f" % reg.score(salary_test, bonus_test)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()