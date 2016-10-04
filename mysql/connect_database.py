#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect("localhost","root","fan","mysql")

cursor = db.cursor()

cursor.execute("select version()")
cursor.execute("select * from user")

data = cursor.fetchone()

#print "Database version :: %s" %data
print data

db.close()
