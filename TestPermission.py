#!/usr/bin/python

import os, sys


ret = os.access("/home/fan", os.W_OK)
print "W_OK -ruturn value %s" % ret

print sys.argv[1]
