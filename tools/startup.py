#!/usr/bin/python

print
print "checking for nltk"
try:
    import nltk
except ImportError:
    print "you should install nltk before continuing"

print "checking for numpy"
try:
    import numpy
except ImportError:
    print "you should install numpy before continuing"

print "checking for scipy"
try:
    import scipy
except:
    print "you should install scipy before continuing"

print "checking for sklearn"
try:
    import sklearn
except:
    print "you should install sklearn before continuing"

try:
	import time
except:
	print "import time error"

print
print "downloading the Enron dataset (this may take a while)"
print "to check on progress, you can cd up one level, then execute <ls -lthr>"
print "Enron dataset should be last item on the list, along with its current size"
print "download will complete at about 423 MB"

start_time = time.time()
# temp_size = 0.0
# temp_time = time.time()
def schedule(a,b,c):
	'''
	a: blocks already downloaded
	b: block size
	c: remote file size
	'''
	# speed = (a*b - temp_size) / (time.time()-temp_time)
	# temp_size = a*b
	# temp_time = time.time()
	speed = (a*b)/(time.time()-start_time)
	print "Downloading Speed:\t %f" % speed

import urllib
url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"
urllib.urlretrieve(url, filename="../enron_mail_20150507.tar.gz", reporthook=schedule) 
print "download complete!"


print
print "unzipping Enron dataset (this may take a while)"
import tarfile
import os
os.chdir("..")
tfile = tarfile.open("enron_mail_20150507.tar.gz", "r:gz")
tfile.extractall(".")

print "you're ready to go!"
