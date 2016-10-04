#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect("localhost","root","fan","mysql")

cursor = db.cursor()

db_name = """create database data;"""

cursor.execute(db_name)


#cursor.execute("select version()")
#cursor.execute("select * from user")

#data = cursor.fetchone()

#print "Database version :: %s" %data
#print data

db.close()
