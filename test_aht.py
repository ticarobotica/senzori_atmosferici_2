from machine import Pin, SoftI2C
from time import sleep
import aht

i2c=SoftI2C(sda=Pin(21), scl=Pin(22), freq=100000)
senzor_aht=aht.AHT2x(i2c)

while True:
    if senzor_aht.is_ready:
        print("Temp=", round(senzor_aht.temperature,2)," ", "Humi=", round(senzor_aht.humidity,2)," ", end="\r")
        sleep(1)
        
