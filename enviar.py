import time

import RPi.GPIO as GPIO
from codigos import  *


ENV=4
CLOCK=17

GPIO.setmode(GPIO.BCM)
GPIO.setup(ENV, GPIO.OUT)
GPIO.setup(CLOCK, GPIO.OUT)

def enviar(dato):
    cod=Codigos()
    first, second, third, fourth=cod.getCodigoSecuencia(dato)
    if first == "0":
        GPIO.output(ENV, GPIO.LOW)
        print("envio 0")
    else:
        GPIO.output(ENV, GPIO.HIGH)
        print("envio 1")
    GPIO.output(CLOCK, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(CLOCK, GPIO.LOW)
    if second == "0":
        GPIO.output(ENV, GPIO.LOW)
        print("envio 0")
    else:
        GPIO.output(ENV, GPIO.HIGH)
        print("envio 1")
    GPIO.output(CLOCK, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(CLOCK, GPIO.LOW)
    if third == "0":
        GPIO.output(ENV, GPIO.LOW)
        print("envio 0")
    else:
        GPIO.output(ENV, GPIO.HIGH)
        print("envio 1")
    GPIO.output(CLOCK, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(CLOCK, GPIO.LOW)
    if fourth == "0":
        GPIO.output(ENV, GPIO.LOW)
        print("envio 0")
    else:
        GPIO.output(ENV, GPIO.HIGH)
        print("envio 1")
    GPIO.output(CLOCK, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(CLOCK, GPIO.LOW)







while True:


    ## Python 2.7 raw_input
    ## Python 3 input
    dato=str(raw_input("introducir dato (a,b,c,d) fin=fin -> "))
    ##dato = str(input("introducir dato (a,b,c,d) fin=fin -> "))

    if dato == "fin":
        break
    if dato in ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"):
        enviar(dato)
    else:
        print("Introducir hasta la p")


GPIO.cleanup()