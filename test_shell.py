import serial
import signal
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *
import sys

cnt = 0
plt.close("all")
talkWithCom = serial.Serial("COM5", 1200)
plt.ion()


def makeFig():
    plt.plot(list)
    
def signal_handler(signal,frame):
    talkWithCom.close()
    print("Recording Completed Sucessfully")
    sys.exit(0)
    
list = []
cohortData = []

signal.signal(signal.SIGINT, signal_handler)

while True:
    if talkWithCom.inWaiting()>0:
            data = talkWithCom.readline()
            print(data.decode("utf-8"))
            list.append(int(data.decode("utf-8")))
            cohortData.append(int(data.decode("utf-8")))
            drawnow(makeFig)
            plt.pause(0.000001)
            cnt = cnt+1
            if cnt>50:
                list.pop(0)
