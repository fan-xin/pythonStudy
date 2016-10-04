#!/usr/bin/python

import csv

#print year and tile
print "print year and title"
for line in open("csv.test"):
    title, year, director = line.split(",")
    print year, title

#using csv module

reader = csv.reader(open("csv.test"))
for title, year, director in reader:
    print year, title
