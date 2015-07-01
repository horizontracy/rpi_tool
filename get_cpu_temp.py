#!/usr/bin/python

import commands

def get_cpu_temp():
	tempFile = open("/sys/class/thermal/thermal_zone0/temp")
	cpu_temp = tempFile.read()
	tempFile.close()
	return float(cpu_temp)/1000

if __name__ == '__main__':
	print(get_cpu_temp())
