#!/usr/bin/python

import MySQLdb

#db = MySQLdb.connect("localhost","root","fan","mysql")
db = MySQLdb.connect("localhost","root","fan","data")

cursor = db.cursor()

sql = """create table fan (
	frist_name char(20) not null,
	last_name char(20),
	age int,
	sex char(1),
	income float ) """


cursor.execute(sql)


#cursor.execute("select version()")
#cursor.execute("select * from user")

#data = cursor.fetchone()

#print "Database version :: %s" %data
#print data

db.close()
