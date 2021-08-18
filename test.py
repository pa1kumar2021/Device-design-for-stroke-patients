# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial
import signal
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *
import sys
a = True
cnt = 0

talkWithCom = serial.Serial("COM5", 1200)
plt.ion()

def makeFig():
    plt.plot(list)

list = []

try:
    print("Recording Started")
    while a == True:
        if talkWithCom.inWaiting()>0:
                data = talkWithCom.readline()
                print(data.decode("utf-8"))
                list.append(int(data.decode("utf-8")))
                drawnow(makeFig)
                plt.pause(0.000001)
                cnt = cnt+1
                if cnt>50:
                    list.pop(0)
                
except KeyboardInterrupt:
    a = False
    talkWithCom.close()
    print("Recording Completed Sucessfully")


# =============================================================================
# except KeyboardInterrupt:
#      print("Recording Completed Sucessfully")
#      talkWithCom.close()
#      sys.exit()
# 
# =============================================================================

