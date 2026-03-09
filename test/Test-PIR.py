# Usar backend rpigpio para evitar el aviso "Falling back from lgpio" (lgpio no disponible en Python 3.13)
import os
os.environ.setdefault("GPIOZERO_PIN_FACTORY", "rpigpio")

from gpiozero import MotionSensor
from signal import pause

# Cambia el 4 por el número de GPIO que hayas usado
pir = MotionSensor(17)

print("Esperando movimiento...")

pir.when_motion = lambda: print("¡Movimiento detectado!")
pir.when_no_motion = lambda: print("Todo tranquilo...")

pause()