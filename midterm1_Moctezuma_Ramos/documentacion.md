## Primer Parcial

- Alejandra Ramos Vélez - A00310480
- Juan Camilo Moctezuma - A00

El objetivo de esta activida es crear un ambiente donde sea posible transmitir mensajes desde un host a disfrentes hosts, dependiendo de la instrucción.

Para la realización de este, se crearon 4 máquinas virtuales: la primera, para el productor que es quien se encargará de ser la máquina que origina los mensajes; la segunda, para el broker rabbitmq que se encargará de re dirigir los mensajes dependiendo de la instrucción recibida; la tercera, para el consumidor 1 que es quien estará escuchando para recibir los mensajes enviados por el productor; y por último, la cuarta máquina que será el consumidor 2 que hará lo mismo que el consumidor 1.

El direccionamiento para la creación de las máquinas fue la siguiente:

- _Productor: 192.168.56.2_
- _Broker RabitMQ: 192.168.56.3_
- _Consumidor1: 192.168.56.4_
- _Consumidor2: 192.168.56.5_

En la siguente figura se muestran la caracteristicas con las que fueron creadas cada máquina, es necesario aclarar que cada una es una ubuntu 18.04, dado que esta ya cuenta con python el cual es fundamental para el desarrollo de la actividad:

![image](https://drive.google.com/uc?export=view&id=1amQ8jSHA79Sl7eCoWVfRvDOx9kNPoPyS)

La forma de aprovisonar cada máquina fue la siguiente:

### **Productor y consumidores**

El funcionamiento del productor y los consumidores se basó en el desarrollo de un programa en python para cada caso, siguiendo la guia presentada por el profesor del curso https://www.rabbitmq.com/tutorials/tutorial-four-python.html , por lo tanto, era necesario obtener las librerias y gestores necesarios por python para realizar el aprovisionaminto de las mpaquinas de forma correcta.

Por ello, el productor y los consumidores solo necesitaron aprovisonarse con Pip y pika, donde **pip** es un sistema de gestión de paquetes que es usado para instalar y administrar lo que python necesite y **pika** es una librería que tiene extenciones de RabbitMQ que permite el envío de mensajes.

En la siguiente figura se muestra como se realizó el aprovisionamiento de estas tres máquinas:

![image](https://drive.google.com/uc?export=view&id=1AdMsVMIwrXWi3ZhlmA_JyOTWUo08PfqC)

Es necesario aclarar que existiran 3 colas para el envío de los mensajes por parte del productor:

- General, la cual envia los mensajes tanto a consumidor1 como a consumidor2
- Grupo01, la cual envia mensajes solo al consumidor1
- Grupo02, la cual envia mensajes solo al consumidor2

Todo ese aprovisionamiento se realiza con el fin de poder hacer uso de los siguiente códigos:

***Código para el productor***

![image](https://drive.google.com/uc?export=view&id=1kPu1tQpx6cebSaVdUJaBYR5r6tCz8Ylm)

En el código del productor se importa la librería pika, la cual nos va a permitir realizar el envio de mesajes.

Consideramos necesario tener credenciales para el productor y que de esta forma el broker reconozca de donde proviene la información que está recibiendo.

El productor enviará una instrucción por el canal creado, si es _Grupo01_ será dirigido a la cola de mensajes del consumidor1, si es _Grupo02_ será dirigido a la cola de mensajes del consumidor2, en caso de que no se envíe ninguna instrucción, se asume que se hará uso de la cola de _General_.

***Código para el consumidor1***

![image](https://drive.google.com/uc?export=view&id=1fvc3G0p5NdmNpwVpKaMHlXfZ5pO-IGME)

***Código para el consumidor2***

![image](https://drive.google.com/uc?export=view&id=1GcJUpRm6aOw5ZE66ONqBF6yR7lWOSHZ4)

Tanto para consumidor1 como para consumidor2, el programa funciona de la misma forma. Ambos están escuchando algún mensaje que les pueda llegar por parte del productor, dependiendo de la cola que provenga.

