import RPi.GPIO as GPIO
import time
import decimal2binary as d2b


GPIO.setwarnings(False)

dac = []

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

inc_flag = 1
t = 0 
x = 0

try:
    period = float(input("Type a period for sygnal: "))

    while True:
        GPIO.output(dac, d2b.decimal2binary(x))

        if x == 0: 
            inc_flag = 1
    
        elif x == 255:
            inc_flag = 0

        x = x + 1 if inc_flag == 1 else x - 1

        time.sleep(period/512)
        t += 1

except ValueError:
    print("Inapropriate period!")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")