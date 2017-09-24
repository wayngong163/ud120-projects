
# coding: utf-8

# In[3]:


#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


# In[4]:


from time import time


# In[5]:


from sklearn.tree import DecisionTreeClassifier
t0 = time()
clf = DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train, labels_train)
t1 = time()-t0
print "training time:%.2f s" % t1


# In[6]:


t0 = time()
pred = clf.predict(features_test)
t1 = time()-t0
print "prediction time:%.2f s" % t1


# In[7]:


from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
acc_perc = acc*100
print "accuracy:%.2f%%" % acc_perc


# ### no. of features

# In[8]:


no_features = len(features_train[0])
print "no. of features:%d" % no_features

# In[ ]:




