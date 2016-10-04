#! /bin/usr/python

import exceptions

print dir(exceptions)

try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print x/y
except ZeroDivisionError:
    print "Some Errors Happened."
except TypeError:
    print "Emm... TypeEoor"
