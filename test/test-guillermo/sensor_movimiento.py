# Librerias a emplear
from gpiozero import MotionSensor
from signal import pause

# Datos en GPIO15
datos = MotionSensor(15)

# Declarar que hacer en cada situación
def movimiento():
    print("Se ha detectado algo")
def noMovimiento():
    print("No se detecta nada")

# Decir que funcion ejecutar en cada situación
datos.when_motion = movimiento
datos.when_no_motion = noMovimiento

print("Rastreando...")

# Dejar ejecutando "en blucle"
pause()