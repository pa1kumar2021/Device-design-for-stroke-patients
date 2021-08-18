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
import time


a = True
cnt = 0
plt.close("all")

talkWithCom = serial.Serial("COM5", 1200)
plt.ion()
i = 0

def makeFig():
    plt.plot(list)
    #plt.xlim(left=max(0, i-50), right=i+10)
    plt.grid()
    
def signal_handler(signal,frame):
    talkWithCom.close()
    print("Recording Completed Sucessfully")
    sys.exit()
    
signal.signal(signal.SIGINT, signal_handler)

list = []
cohortData = []

try:
    print("Recording Started")
    while a == True:
        if talkWithCom.inWaiting()>0:
                data = talkWithCom.readline()
                print(data.decode("utf-8"))
                list.append(int(data.decode("utf-8")))
                cohortData.append(int(data.decode("utf-8")))
                drawnow(makeFig)
                plt.pause(0.000001)
                #time.sleep(0.000001)
                #i = i+1
                cnt = cnt+1
                if cnt>100:
                    list.pop(0)

                
except KeyboardInterrupt:
    sys.exit()
    talkWithCom.close()
    print("Recording Completed Sucessfully")


    


# =============================================================================
# except KeyboardInterrupt:
#      print("Recording Completed Sucessfully")
#      talkWithCom.close()
#      sys.exit()
# 
# =============================================================================

