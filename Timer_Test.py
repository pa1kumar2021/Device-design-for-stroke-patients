from pyfirmata import Arduino, util
import time
from datetime import datetime



board = Arduino("COM5")
a = []
analogPin0 = board.get_pin("a:0:i")

iterator_thread = util.Iterator(board)

iterator_thread.start()


for i in range(0,600):
    analogPin0.enable_reporting()
    time.sleep(0.0001)
    test = analogPin0.read()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time = ", current_time)
    a.append(test)
    print(test)
    i = i+1

board.exit()