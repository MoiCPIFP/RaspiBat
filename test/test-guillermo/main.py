# Librerias a emplear
import time
import board
import adafruit_dht
from gpiozero import MotionSensor
from signal import pause
from picamera2 import Picamera2

# Declarar los periféricos
datosTH = adafruit_dht.DHT22(board.D14)
datosM = MotionSensor(15)
camara = Picamera2()

# Configuración por defecto de la cámara
camara.configure(camara.create_still_configuration())

# Declarar variable para nombre de foto
idFoto = -1

# Declarar que hacer en cada situación (Movimiento)
def movimiento():
    global idFoto
    idFoto += 1
    print("Se ha detectado movimiento")
    # Iniciar la cámara
    camara.start()
    # Capturar y guardar la imagen
    camara.capture_file(f"imagen_test_{idFoto}.jpg")
    # Detener la cámara
    camara.stop()
def noMovimiento():
    print("No se detecta nada")

datosM.when_motion = movimiento
datosM.when_no_motion = noMovimiento

# Bucle de recogida de datos
while True:
    # Comprobar que los datos son correctos
    try:
        temp = datosTH.temperature      # °C
        hum = datosTH.humidity          # %

        if temp is not None and hum is not None:
            print(f"Temp: {temp:.1f} °C  Humedad: {hum:.1f} %")
        # Si no ha tomado algun dato, no mostrarlo
        else:
            print("Lectura no válida")

    # Si el calculo de comprobación de datos sale mal
    except RuntimeError as e:
        print("Error de lectura:", e)

    time.sleep(2)   # mínimo 2 s según el datasheet