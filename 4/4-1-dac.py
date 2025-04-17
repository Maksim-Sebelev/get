import RPi.GPIO as GPIO
import decimal2binary as d2b

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(     GPIO.BCM)
GPIO.setup  (dac, GPIO.OUT)

try:
    while True:
        num = input("input: ")
        try:
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, d2b.decimal2binary(num))
                voltage = float(num) / 256 * 3.3
                print(f"Vout = {voltage:.4} v")
            else:
                if num < 0:
                    print("input < 0. err.")
                elif num > 255:
                    print("input > 255. err.")  
        except Exception:
            if num == "q": break
            print("inp is not str")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("end of programm")