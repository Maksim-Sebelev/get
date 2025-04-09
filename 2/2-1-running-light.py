import RPi.GPIO as gp
import time

gp.cleanup()
leds = [2, 3, 4, 17, 27, 22, 10, 9]

gp.setmode(gp.BCM)
gp.setup(leds, gp.OUT)


cyc_size   = 3
lamp_quant = len(leds)


for i in range(0, cyc_size):
    for j in range(0, lamp_quant):
        gp.output(leds[j], 1)
        time.sleep(0.2)
        gp.output(leds[j], 0)

# gp.cleanup()
