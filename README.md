# ProyectoCapstone
## Titulo: Sistema IoT de monitoreo de variables fisicoquímicas aplicadas a un sistema agrícola de limones

### Justificación:
La agricultura es el fundamento de la sociedad como la conocemos, desde tiempos inmemorables hemos buscado la forma de obtener alimentos y producirlos, actualmente los retos van desde la singularidad del individuo por el autoconsumo, hasta el reabastecimiento de insumos en futuros viajes espaciales que buscan el reabastecimiento del astronauta en periodos muy extensos y/o en la capacidad de producir alimento en la expansión humana en otros planetas. 

La producción del limón en México tuvo un cierre preliminar en el año 2021, de 2 millones 965 mil toneladas, 4% más que el año pasado, Veracruz fue la principal entidad productora, contribuyendo con 27.3% del total nacional, correspondiente a 809 mil toneladas, seguido por Michoacán con 27% (800 mil toneladas); Oaxaca con 10.3% (306 mil toneladas); Colima 10.1% (300 mil toneladas); Tamaulipas 4.8% (142 mil toneladas) y Jalisco 3.6% (107mil toneladas). En conjunto, estos estados, aportan 83% de la producción de limón en el país (Véase Anexo 10) (SIAP, 2022). Esta comercialización representa ganancias a nivel nacional de más de $ 5 000 .00 millones de pesos. Este ingreso es un sustento fundamental para el país, y por tanto requiere una exigencia en su cuidado y atención. 

Finalmente, este proyecto puede ser aplicado a pequeños y medianos agricultores, proporcionando un monitoreo constante dentro de sus cultivos, el dispositivo recolectara datos, para después convertirse en información que puede ser consultada, analizada y exportada de acuerdo a los requerimientos de cada agricultor.



### Objetivos generales: 

•	Aplicar los conocimientos adquiridos a lo largo de diplomado para la construcción e implementación de un sistema de monitoreo IoT.

### Objetivos específicos 

•	Implementar IoT para el monitoreo de: Temperatura, Humedad, PH, Altitud y Presión.

•	Desarrollar un dispositivo IoT, para la recolección de datos en tiempo real.

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



### Conversor analógico digital ADC ADS1115


![image](https://user-images.githubusercontent.com/86132543/150584014-96bdc688-a66c-48e1-81a9-b2d64bda35f9.png)


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


