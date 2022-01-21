import paho.mqtt.client as mqtt
import time
from sensores import dht11, bmp, sensorPH

broker = "3.65.154.195"

try:
	cliente = mqtt.Client("Equipo_Bellakos")
	cliente.connect(broker)
	print("EL USUARIO CONECTADO")
except:
	print("EL USUARIO NO SE PUDO CONECTAR")
	
topicTemperatura = "ProyectoCapstone/UAM/Sensor/dht11/temperatura"
topicHumedad = "ProyectoCapstone/UAM/Sensor/dht11/humedad"
#topicTempBMP = "ProyectoCapstone/UAM/Sensor/dht11/tempBMP"
topicPresion = "ProyectoCapstone/UAM/Sensor/bmp/presion"
topicAltitud = "ProyectoCapstone/UAM/Sensor/bmp/altitud"
topicPH = "ProyectoCapstone/UAM/Sensor/sensorph/ph"

try: 
	cliente.subscribe(topicTemperatura)
	cliente.subscribe(topicHumedad)
	#cliente.subscribe(topicTempBMP)
	cliente.subscribe(topicPresion)
	cliente.subscribe(topicAltitud)
	cliente.subscribe(topicPH)
	print("SUBSCRIPCIÓNES CORRECTAS")
	print(" ")
except:
	print("NO SE PUDO SUBSCRIBIR")
	print(" ")
	
def main():
        while True:
                Temperatura, Humedad = dht11.lecturaTempHum()
                TempBMP, Presion, Altitud = bmp.readBmp180()
                PH = sensorPH.lecturaPH()
	
                cliente.publish(topicTemperatura, Temperatura)
                cliente.publish(topicHumedad, Humedad)
                cliente.publish(topicPresion, Presion)
                cliente.publish(topicAltitud, Altitud)
                cliente.publish(topicPH, PH)
                
                print("Temperatura: ", Temperatura, "Humedad: ", Humedad)
                print("Presión: ", Presion, "Altitud: ", Altitud)
                print("PH: ", PH)
                print("DATOS PUBLICADOS")
                print(" ")
                time.sleep(10)
                
if __name__ == '__main__':
        main()
