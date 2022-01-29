# ProyectoCapstone
## Titulo: Sistema de monitoreo de variables fisicoquímicas aplicadas a un sistema agrícola con tecnología IoT

### Justificación:
El desarrollo tecnológico y su implementaccón para la resolución de problemas de la vida cotidiana ha ido creciendo de manera más acelerada en los ultimos años. A pesar de ello, es evidente que este avance no sido gradual para todos los sectores; La agricultura hoy es uno de los casmpos con mayor potencial de desarrollo del mundo. Por un lado, la creciente demanda originada en el crecimiento poblacional y en la mejora alimentaria en el consumo humano.
Las Naciones Unidas proyectan un importante crecimiento poblacional que llevaria a la población mundial a mas de nueve mil millones de personas en 2050 (Zlotnik 2009) y se observa una oocidentalización en el perfil del consumo humano, este hecho implica uno de los mayores retos al conllevar un incremento en la demanda de insumos y derivados.

La posibilidad de la incorporación de las tecnologias relacionadas con el internet de las cosas (IoT), la recolección de información, el monitoreo y la evaluación de un sistema de cultivo, resulta determinante para una afectiva toma de decisiones, mejor corrección de la producción para alcanzar el necesario abastecimiento mundial. Los cultivos protegidos dan la oportunidad de controlar el clima y los aspectos físicos-químicos para lograr una optimización agricola.

### Objetivos generales: 

•	Desarrollar un prototipo básico de internet de las cosas donde se pueda integrar sensores para el envío de información en tiempo real de variables como: Temperatura, Humedad, PH, Altitud, Presión y Temperatura Barométrica

### Objetivos específicos 

•Aplicar los conocimientos adquiridos a lo largo de diplomado para la construcción e implementación de un sistema de monitoreo IoT.

•Generar una alternativa sustentable y ruptura de paradigma para que la población pueda optar por una integración de mejores perfiles alimenticios y autoconsumo.

•	Analizar y gestionar la información recolectada, de tal forma que pueda ser reutilizada para el buen manejo dentro del sector agrícola y/o agroindustrial.  

### Materiales:

### Raspberry Pi 3 Model B+

![image](https://user-images.githubusercontent.com/86132543/150583668-6d0e242f-4d02-4de8-8769-a506dce822ae.png)

### Trajeta Gpio extensión Raspberry Pi + 

![image](https://user-images.githubusercontent.com/86132543/150583804-1c4a76ab-5fd0-499c-8647-a415a0a6b313.png)

### Sensor de presión barometrica BMP180

![image](https://user-images.githubusercontent.com/86132543/150583077-4830507c-8181-4b40-9f66-9bcded1cb031.png)

### Sensor de temperatura y humedad DHT11

![image](https://user-images.githubusercontent.com/86132543/150583271-769c3733-029b-49e7-936e-5516bc4bdd1b.png)

### Sensor de PH con modulo E201-BNC

![image](https://user-images.githubusercontent.com/86132543/150583444-ffda412d-c8a7-4f3e-924d-2ff0ae8ac2de.png)

### Convertidor DC-DC step-down

![image](https://user-images.githubusercontent.com/86132543/150584368-88b5dc12-c552-475b-828c-ed6f5b4e4116.png)

### Conversor analógico digital ADC ADS1115


![image](https://user-images.githubusercontent.com/86132543/150584014-96bdc688-a66c-48e1-81a9-b2d64bda35f9.png)

### Bateria de 12 volts

![image](https://user-images.githubusercontent.com/86132543/150584256-e410aa02-e999-41c8-9f51-4022bd126f0c.png)



## Circuito:

El siguiente esquematico muestra el armado del circuito con los sensores integrados.

![image](https://user-images.githubusercontent.com/86132543/150582433-729285b0-3ac3-4e2a-bc26-b99467194b26.png)


### Interfaces necesarias 

- Comunicación i2c 
Este bus de comunicación funciona de manera bidireccional con una línea de datos (SDA) y una líunea de reloj (SCL). Para instalarlo debemos dirigrnos a la sección de configuración de la Raspberry. Esta acción se puede realizar con el siguiente comando:

```
pi@raspberrypi:~$ sudo raspi-config
```

Seleccionamos *Interfacing Opstions*

![image](https://user-images.githubusercontent.com/86132543/150589149-68b547f5-8c61-49fc-9eac-d260059794ea.png)

Seleccionamos *P5*

![image](https://user-images.githubusercontent.com/86132543/150589274-681b0424-d171-443e-be55-053a3a43978b.png)

Confimamos la habilitación del interfaz

![image](https://user-images.githubusercontent.com/86132543/150589354-9b8fbb8c-03e9-4ed5-8b9c-e952e905ef7b.png)

Confirmamos de enterado selleccionando la opción *<ok>*
 
  ![image](https://user-images.githubusercontent.com/86132543/150589462-b3a5dd70-10da-495c-a53c-a7ab839b7208.png)

  Para que los cambios a la configuración tengan efecto, debemos reiniciar el sistema selleccionando opción de *<Yes>*. Una vez que el sistema se reinicie, podemos usas la comunicación I2C.
  
  ![image](https://user-images.githubusercontent.com/86132543/150589654-255d4d0b-f0b6-4f02-8f1b-4106c4abd309.png)

  
- ADAFruit_DHT  
Para instalar esta extensión, debemos de intalar el controlador de Python proporcionado por Adafruit. Para esto ejecutamos las siguientes líneas de comandos.

```
sudo apt-get update 
sudo apt-get install build-essential python-dev
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install 
```
  
- ADAFruit_ADSx15
 Para instalar esta libreria necesitamos ejecutar la siguiente instrucción en la ventana de comandos.
  
  ```
  sudo pip3 install adafruit-circuitpython-ads1x15
  ```
  
- Node-red
 Esta intercace te permite definir graficamente flujos de servicioas a través de protocolos estándares como REST, MQTT, Websocket, AMQP.
 Node-red ya viene preinstalado en la Raspberry Pi, solo tenemos que abrir una terminal y ejecutar el siguiente comando.
  
  ```
  bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)
  ```
 
 Para encender el Node-red, debemos ejecutar el siguiente comando en nuestra terminal.
 ```
 node-red
 ```
- Grafana
 Esta interfaz nos permitira analizar y visializar las datos recolectados.
 Para instlar grafana en la Raspberry, primero debemos ejecutar el siguiente comando de descarga:
             
  ```
  wget https://dl.grafana.com/oss/release/grafana_5.4.0_armhf.deb
  ```           
  Más adelante debemos intalar el paquete de grafana con el siguiente comando:
  
  ```
  sudo dpkg -i grafana_5.4.0_armhf.deb
  ```
  
  Posteriormente debemos habilitar el servicio de Grafana:
  
  ```
  sudo /bin/systemctl enable grafana-server 
  ```
 
  Y por ultimo arrancar el servicio:
 
  ```            	
  sudo /bin/systemctl start grafana-server
  ```    
- Influxdb
Para instalar localmente el interfaz de Influxdb, debemos de ejecutar las sigueintes líneas de código en nuestra terminal.
 
 ``` 
sudo apt install influxdb
sudo apt install influxdb-client
sudo service influxdb start
 
 ```             
Poseteriormente debemos modificar una parte de influx, escribiendo el siguiente comando:
```
sudo nano /etc/influxdb/influxdb.conf
```              
              
Por ultimo debemos de reiniciar la consola para poder usar influxdb
```
sudo service influxdb restart
```
- MQTT broker
Para poder utilizar MQTT, debemos de instalar y habilitar con las siguientes lineas de intrucciones:
              
  ```
  sudo apt install mosquitto mosquitto-clients

  sudo systemctl enable mosquitto
  ```
 Para aceder a la interfaz debemos de abrir la siguiente dirección en cualquier navegador: **127.0.0.1:1880**


