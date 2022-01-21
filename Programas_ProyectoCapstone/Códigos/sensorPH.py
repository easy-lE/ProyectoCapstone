import time
import board
import busio
##from board import *     ###
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def lecturaPH():
    # Se inicializa el canal donde se va a leer el voltaje de la turbidez
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    
    # Se lee el canal en donde esta conectado el sensor de PH, en este caso es el A1 del ADS1115
    channel = AnalogIn(ads, ADS.P1)
    voltaje = 0.0
    # Se hacen 5 lecturas al canal analógico del ADS1115
    for x in range(3):
        time.sleep(0.1)
        voltaje = voltaje + channel.voltage

    # Se obtiene su promedio
    voltaje = voltaje / 3
    # Se redondea a 2 cifras significativas
    voltaje = round(voltaje, 3)
    #print("voltaje: ", voltaje)

    # Ecuación de la recta
    ph = round((voltaje * (-5.7 )+ 11.34), 0)
    #print("v:",voltaje, "ph:", ph)
    #print("ph:", ph)

    time.sleep(2)
    # Se regresa el valor obtenido de Ph
  
    return ph
 
