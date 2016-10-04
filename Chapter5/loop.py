#!/usr/bin/python

from math import sqrt

for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root) and n != 81:
	print n
	break
else:
    print  "Not Found!"


while True:
    word = raw_input('Please input one world: ')
    if not word: break
    print 'The word was '+ word

