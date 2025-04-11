from machine import Pin, SoftI2C
from time import sleep

import BME280

i2c=SoftI2C(sda=Pin(21), scl=Pin(22), freq=10000)
senzor_bme280=BME280.BME280(i2c=i2c)

while True:
    print("T=",senzor_bme280.temperature," ","P=",senzor_bme280.pressure," ","H=",senzor_bme280.humidity," ", end="\r")
    sleep(1)
    
    