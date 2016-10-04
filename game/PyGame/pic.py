#!/usr/bin/python

import pygame
from pygame.locals import *
from sys import exit


pygame.init()

screen = pygame.display.set_mode((500,500),0,32)

while True:
    for event in pygame.event.get():
	if event.type == QUIT:
	    exit()

    pygame.display.update()
