import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)

gp.setup(24, gp.OUT)

while True:
    gp.output(24, 1)
    time.sleep(1)
    gp.output(24, 0)
    time.sleep(1)




