#!/usr/bin/python

import MySQLdb

#db = MySQLdb.connect("localhost","root","fan","mysql")
db = MySQLdb.connect("localhost","root","fan","data")

cursor = db.cursor()

#sql = """create table fan ( frist_name char(20) not null,last_name char(20), age int,sex char(1),income float ) """
sql = "delete from fan where age > '%d'" %(29)
try:
	cursor.execute(sql)
	db.commit()

except:
	print "Error"
	#Rollback in case there is any error
	db.rollback()


#cursor.execute("select version()")
#cursor.execute("select * from user")

#data = cursor.fetchone()

#print "Database version :: %s" %data
#print data

db.close()
