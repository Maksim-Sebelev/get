import RPi.GPIO as gp
import time

#=======================================================================================================

def gpCtor(leds, aux):
    gp.setmode(gp.BCM)
    gp.setup(leds, gp.OUT)
    gp.setup(aux, gp.IN)
    return

#=======================================================================================================

def moveVoltageFromAuxToLeds(led, aux):
    aux_input = gp.input(aux)
    gp.output(led, aux_input)
    return

#=======================================================================================================

def calcTime(start_time):
    now_time = time.time()
    time_diff = now_time - start_time
    return time_diff

#=======================================================================================================

def runProgramm(leds, aux, cyc_size, programm_time):
    start_time = time.time()

    while calcTime(start_time) < programm_time:
        for i in range(0, cyc_size):
            moveVoltageFromAuxToLeds(leds[i], aux[i])

    return

#=======================================================================================================

def EOP(leds):
    gp.output(leds, 0)
    gp.cleanup()
    return

#=======================================================================================================

def main(programm_time):
    gp.cleanup()

    leds = [2,   3,  4, 17, 27, 22, 10,  9]
    aux  = [21, 20, 26, 16, 19, 25, 23, 24]

    cyc_size = 8

    gpCtor(leds, aux)
    runProgramm(leds, aux, cyc_size, programm_time)
    EOP(leds)

#=======================================================================================================

programm_time = 20

main(programm_time)

