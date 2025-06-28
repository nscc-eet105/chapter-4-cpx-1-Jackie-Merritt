from adafruit_circuitplayground import cp
import time

def on():
    for num in range(1, 10):
        cp.pixels[num] = (0, 100, 100) #
        #else:sec()

def off():
    for num in range(1, 10):
        cp.pixels[num] = (0, 0, 0)

while True:
    if cp.touch_A1:
        on()
    else:
        off()






