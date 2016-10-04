#!/usr/bin/python

import sys,os 

print sys.argv[1]

def my_partial_fn(x):
    if x:
        y=10
    return y

my_partial_fn(sys.argv[1])
