#!/usr/bin/env python

import time
import piface.pfio
from array import *

piface.pfio.init()
Leds = []
count = True

for i in range(1,9):
	Leds.append(piface.pfio.LED(i))

def toggle(light):
	light.turn_on()
	time.sleep(.05)
	light.turn_off()

while True:
	""" Count up the leds """
	if count:
		for n in Leds:
			toggle(n)
		count = False

	"""Count Down the leds"""
	if count == False:
		for n in reversed(Leds):
			toggle(n)
		count = True

# vim:ts=2:sw=2:sts=2:et:ft=python
