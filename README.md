# RaspiBat
Este proyecto tiene como objetivo el diseño y desarrollo de un sistema de monitorización ambiental para una colonia de murciélagos utilizando una Raspberry Pi Zero

RaspiBat
Proyecto de innovación


Introducción
Este proyecto tiene como objetivo el diseño y desarrollo de un sistema de monitorización ambiental para una colonia de murciélagos utilizando una Raspberry Pi Zero. A través de varios sensores de movimiento, temperatura, humedad y una cámara nocturna, se recolectarán datos en tiempo real que serán visualizados en una página web. Los datos recolectados se mostrarán mediante gráficos interactivos utilizando Chart.js para facilitar el análisis de la actividad de la colonia y sus condiciones ambientales.
Objetivos
Monitorear la actividad de los murciélagos: Detectar su presencia y actividad dentro de su refugio utilizando un sensor de movimiento.


Medir las condiciones ambientales: Controlar la temperatura y humedad dentro del refugio para asegurar su viabilidad y el bienestar de los murciélagos.


Captura nocturna: Usar una cámara compatible con la Raspberry Pi Zero para capturar imágenes o vídeo durante la noche sin interferir con los animales.


Visualización remota de datos: Crear una interfaz web donde se presenten los datos de los sensores y las imágenes capturadas, usando gráficos generados con Chart.js para mostrar las tendencias de temperatura, humedad y actividad a lo largo del tiempo.

Materiales Necesarios
Hardware:


Raspberry Pi Zero: Placa base para el proyecto.


Sensor de movimiento PIR: Detecta la presencia de murciélagos en el refugio.


Sensor de temperatura y humedad (DHT22): Mide las condiciones ambientales dentro del refugio.


Cámara nocturna: Permite la captura de imágenes durante la noche sin alterar el comportamiento de los murciélagos.


Fuente de alimentación: Adaptador de corriente o batería recargable.


Caja protectora: Protege la Raspberry Pi y los componentes de las inclemencias del tiempo.


Software:


Raspberry Pi OS: Sistema operativo para la Raspberry Pi.


Librerías Python:


RPi.GPIO: Para interactuar con los pines GPIO de la Raspberry Pi.


Adafruit_DHT: Para leer los sensores de temperatura y humedad.


OpenCV (opcional, para procesamiento de imágenes en cámara).


Firebase o base de datos en la nube para almacenar los datos de manera segura y en tiempo real.


Frontend Web:


HTML, CSS, JavaScript: Para construir la interfaz de la página web.


Chart.js: Para crear gráficos interactivos con los datos recolectados.






FASES DEL PROYECTO
Instalación y Configuración de la Raspberry Pi:


Preparar la Raspberry Pi Zero con el sistema operativo Raspberry Pi OS. Link


Configurar el acceso a la red Wi-Fi para permitir la subida de datos a la nube.


Interfaz de Sensores:


Conectar y configurar el sensor DHT22 AM2302 de temperatura/humedad. Link
Conectar y configurar el sensor de movimiento PIR . Link


Programar la lectura de datos de los sensores utilizando Python.


Configurar la cámara nocturna para la captura de imágenes y grabaciones en condiciones de baja luz. Link


Base de Datos en la Nube:


Configurar una base de datos en Firebase para almacenar los datos de los sensores en tiempo real.


Asegurar que los datos de temperatura, humedad y movimiento sean actualizados de manera automática cada vez que se registre un cambio.


Desarrollo de la Página Web:


Crear una interfaz web que muestre los datos de los sensores utilizando HTML y CSS.


Usar JavaScript y Chart.js para visualizar los datos históricos en gráficos interactivos.


Implementar un sistema para mostrar las imágenes de la cámara nocturna en la web.


Pruebas y Ajustes:


Realizar pruebas en el refugio para garantizar que los sensores y la cámara funcionan correctamente.


Ajustar la frecuencia de captura y visualización de datos para asegurar un rendimiento óptimo.



Arquitectura del Sistema
Sensores:


Los sensores de temperatura y humedad enviarán sus datos al Raspberry Pi, que los procesará y almacenará en Firebase.


El sensor de movimiento PIR detectará la actividad de los murciélagos y enviará una señal cuando detecte presencia.


La cámara nocturna tomará imágenes o grabaciones y almacenará el resultado en un servidor o base de datos.


Base de Datos:


Los datos de los sensores se almacenarán en Firebase Realtime Database, lo que permite actualizaciones instantáneas.


Firebase actuará como intermediario entre la Raspberry Pi y la aplicación web/móvil, permitiendo la sincronización de los datos en tiempo real.


Aplicación Web:


Frontend: La página web mostrará los datos de los sensores de forma visual mediante Chart.js para gráficos interactivos (temperatura, humedad y actividad).


Los datos históricos y en tiempo real se presentarán con una línea de tiempo o gráficos de barras.


Las imágenes capturadas por la cámara se presentarán como una galería o sección específica en la página.

