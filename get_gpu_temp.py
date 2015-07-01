#!/usr/bin/python

import commands

def get_gpu_temp():
	gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
	return float(gpu_temp)


if __name__ == '__main__':
	print(get_gpu_temp())
