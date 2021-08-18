import serial as sr
import matplotlib.pyplot as plt
import numpy as np

s = sr.Serial("COM5",115200);
# plt.close("all")
# plt.figure()
# plt.ion()
# plt.show()

data = np.array([]);

i = 0
while True:
    a = s.readline()
    a = a.decode()
    print(a)
    #b = float(a)
    data = np.append(data,a)
    # plt.cla()
    # plt.plot(data)
    # plt.pause(0.01)
    #i = i+1

s.close()

