import RPi.GPIO as GPIO
import time
import decimal2binary as d2b

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(     GPIO.BCM)
GPIO.setup  (dac, GPIO.OUT)

flag = 1
x = 0

try:
    period = float(input("input: "))

    while True:
        tmp = d2b.decimal2binary(x)

        GPIO.output(dac, tmp)
        print(x)
        if x == 0: 
            flag = 1
    
        elif x == 255:
            flag = 0

        if flag:
            x += 1
        else:
            x -= 1

        time.sleep(period/512)

except ValueError:
    print("incorrect period")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print('end of programm')
