# ProyectoCapstone
## Titulo: Implementación de IoT para el monitorio de cultivos agrícolas

### Justificación:
El desarrollo tecnológico y su implementaccón para la resolución de problemas de la vida cotidiana ha ido creciendo de manera más acelerada en los ultimos años. A pesar de ello, es evidente que este avance no sido gradual para todos los sectores; La agricultura hoy es uno de los casmpos con mayor potencial de desarrollo del mundo. Por un lado, la creciente demanda originada en el crecimiento poblacional y en la mejora alimentaria en el consumo humano.
Las Naciones Unidas proyectan un importante crecimiento poblacional que llevaria a la población mundial a mas de nueve mil millones de personas en 2050 (Zlotnik 2009) y se observa una oocidentalización en el perfil del consumo humano, este echo implica uno de los mayores retos al conllevar un incremento en la demanda de insumos y derivados.

La posibilidad de la incorporación de las tecnologias relacionadas con el internet de las cosas (IoT), la recolección de información, el monitoreo y la evaluación de un sistema de cultivo, resulta determinante para una afectiva toma de decisiones, mejoa corrección de la producción para alcanzar el necesario abastecimiento mundial. Los cultivos protegidos dan la oportunidad de controlar el clima y los aspectos físicos-químicos para lograr una optimización agricola.

### Objetivos: 
1) Desarrollar un módelo básico de internet de las cosas donde se puedan integrar sensores y enviar información sobre las variables de: Temperatura, Humedad, PH, Altitud, Presión y Temperatura Barométrica.

2) Analizar y gestionar la información recolectada de manera eficaz, de manera que esta pueeda ser reutilizada para el buen cuidado del cultivo agricola.

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

sudo raspi-config


- ADAFruit_DHT
- ADAFruit_ADSx15
- Node-red
- Grafana
- Influxdb

