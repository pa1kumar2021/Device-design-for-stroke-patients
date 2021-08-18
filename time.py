# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 13:06:09 2021

@author: Lenovo
"""
a = []

import time

time.sleep(1)

t_end = time.time() + 1

while time.time() < t_end:
    a.append(1)
    time.sleep(1)
       