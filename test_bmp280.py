from machine import Pin, SoftI2C
import bmp280
from time import sleep

i2c=SoftI2C(sda=Pin(21), scl=Pin(22), freq=10000)
senzor_bmp280=bmp280.BMP280(i2c)

while True:
    print("T=",round(senzor_bmp280.temperature,2)," ","P=",round(senzor_bmp280.pressure/100,2)," ", end="\r")
    sleep(1)
    
    