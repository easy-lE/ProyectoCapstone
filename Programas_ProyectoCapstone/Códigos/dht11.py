import Adafruit_DHT
import time

# Se selecciona el tipo de sensor DHT11,DHT22
sensor = Adafruit_DHT.DHT22


#Pin al que se conecta a la rasp
pin = 23

def lecturaTempHum():
    while True: 
    # Intenta leer el sensor cada 2 segundos e imprime , de lo contrario muestra error
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    
        #if humedad is not None and temperatura is not None:
            #print('Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temperatura, humedad))
       
        #else:
            #print('Error en la lectura!')

        time.sleep(5)
        return temperatura, humedad
