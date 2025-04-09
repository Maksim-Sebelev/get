import RPi.GPIO as gp
import time


gp.setmode(gp.BCM)

gp.setup(24, gp.OUT)
gp.setup(19, gp.IN)


inp = gp.input(19)

gp.output(24, inp)

time.sleep(2)