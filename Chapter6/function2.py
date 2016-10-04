#!/usr/bin/python


def change(n):
    'Change the first name to Mr. Fan .'
    n[0] = 'Mr. Fan'

names= ['Mrs. Zhang','Miss Fan']
print "Before Change: ", names

change(names)

print "After Change: ", names

print "Docmentation String is " + change.__doc__


def hello3(greeting= 'Hello', name = 'world'):
    print '%s, %s!' % (greeting, name)

hello3()
hello3('Fan')
hello3('Fan','Xin')
