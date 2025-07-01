from adafruit_circuitplayground import cp
import time

def on():
    for num in range(0, 10):
        cp.pixels[num] = (0, 100, 100)

def off():
    for num in range(0, 10):
        cp.pixels[num] = (0, 0, 0)

while True:
    if cp.touch_A1:
        on()
    else:
        off()


