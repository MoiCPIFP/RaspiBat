# Librerias a emplear
from picamera2 import Picamera2

# Declarar la cámara
camara = Picamera2()

# Configuración por defecto de la cámara
camara.configure(camara.create_still_configuration())

# Iniciar la cámara
camara.start()

# Capturar y guardar la imagen
camara.capture_file("imagen_test.jpg")

# Detener la cámara
camara.stop()