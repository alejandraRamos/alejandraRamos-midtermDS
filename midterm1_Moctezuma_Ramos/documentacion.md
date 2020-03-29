## Primer Parcial

- Alejandra Ramos Vélez - A00310480
- Juan Camilo Moctezuma - A00

El objetivo de esta activida es crear un ambiente donde sea posible transmitir mensajes desde un host a disfrentes hosts, dependiendo de la instrucción.

Para la realización de este, se crearon 4 máquinas virtuales: la primera, para el productor que es quien se encargará de ser la máquina que origina los mensajes; la segunda, para el broker rabitmq que se encargará de re dirigir los mensajes dependiendo de la instrucción recibida; la tercera, para el consumidor 1 que es quien estará escuchando para recibir los mensajes enviados por el productor; y por último, la cuarta máquina que será el consumidor 2 que hará lo mismo que el consumidor 1.

El direccionamiento para la creación de las máquinas fue la siguiente:

- _Productor: 192.168.56.2_
- _Broker RabitMQ: 192.168.56.3_
- _Consumidor1: 192.168.56.4_
- _Consumidor2: 192.168.56.5_

En la siguente figura se muestran la caracteristicas con las que fueron creadas cada máquina:

![image](https://drive.google.com/uc?export=view&id=1amQ8jSHA79Sl7eCoWVfRvDOx9kNPoPyS)
