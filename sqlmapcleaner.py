__author__ = 'mohammed'
import os
import shutil

path = '/usr/share/sqlmap/output/'
dir = os.listdir(path)
for d in dir:
    print "Checking "+d+" ..."
    if os.path.isdir(path+d):
        if not os.path.isdir(path+d+"/dump"):
            print "Removing "+d+" ..."
            shutil.rmtree(path+d)
