# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 12:32:44 2021

@author: Lenovo
"""

from pyfirmata import Arduino, util
import time

board = Arduino("COM5", baudrate=9600)

a = []
pin = board.get_pin("a:0:i")

iterator = util.Iterator(board)
iterator.start()

time.sleep(1)

t_end = time.time() + 1
while time.time() < t_end:
    analog_value = pin.read()
    a.append(analog_value)
    
board.exit()
