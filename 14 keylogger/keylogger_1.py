#!/usr/bin/python

import pynput.keyboard

def process_key_press(key):
	print (key)

keyboard_listener=pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
	keyboard_listener.join()
