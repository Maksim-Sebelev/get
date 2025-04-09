import RPi.GPIO as gp
import time

dac =    [8, 11, 7, 1, 0, 5, 12, 6]
number = [1, 1, 1, 1, 1, 1, 1, 1]


gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)

gp.output(dac, number)


time.sleep(15)


gp.output(dac, 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
gp.cleanup()
