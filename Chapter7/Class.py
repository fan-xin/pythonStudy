#! /bin/usr/python

__metaclass__ = type


class Person:

    def setName(self, name):
	self.name = name
    
    def getName(self):
	return self.name

    def greet(self):
	print "Hello, world ! I am %s" % self.name


foo = Person()
bar = Person()
foo.setName("Luke")
bar.setName("Alex")
foo.greet()
bar.greet()
