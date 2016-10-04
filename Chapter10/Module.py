#!/usr/bin/python

import math
import sys

sys.path.append('/home/fan/work/python/Chapter10')

import Hello3

Hello3.hello()

print math.sin(0)

class Bird():
    def __init__(self):
	self.hungry = True
    def eat(self):
	if self.hungry:
	    print 'Ahhh...'
	    self.hungry = False
	else:
	    print 'No, thanks!'

class SongBird(Bird):
    def __init__(self):
	Bird.__init__(self)
	self.sound = 'Squawk!'
    def sing(self):
	print self.sound

b = Bird()
b.eat()
b.eat()

sb = SongBird()
sb.sing()
sb.eat()
