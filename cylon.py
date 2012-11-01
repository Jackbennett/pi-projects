#!/usr/bin/env python

import time
import piface.pfio
from array import *

piface.pfio.init()
Leds = []

for i in range(1,9):
	Leds.append(piface.pfio.LED(i))

def toggle(light):
	light.turn_on()
	time.sleep(.1)
	light.turn_off()

while True:
	for n in Leds:
		toggle(n)

# vim:ts=2:sw=2:sts=2:et:ft=python
