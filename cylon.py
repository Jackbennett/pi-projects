#!/usr/bin/env python

from time import sleep
import piface.pfio as io

io.init()
Leds = []
count = True

for i in range(1,9):
	Leds.append(io.LED(i))

def toggle(light):
	light.turn_on()
	sleep(.05)
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
