"""
RaspiBatCamera.py - Captura de imagen con la cámara de Raspberry Pi (rpicam-still).
Requiere: Raspberry Pi con cámara y rpicam-apps (sudo apt install rpicam-apps).
"""

import subprocess
import os
from datetime import datetime


def capturar_imagen(ruta_salida=None, ancho=1920, alto=1080, tiempo_espera_ms=1000, sin_preview=True):
    """Captura una foto con rpicam-still. Devuelve la ruta del archivo o None si hay error."""
    if ruta_salida is None:
        nombre = f"captura_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        ruta_salida = os.path.join(os.path.dirname(os.path.abspath(__file__)), nombre)

    ruta_salida = os.path.abspath(ruta_salida)
    directorio = os.path.dirname(ruta_salida)
    if directorio and not os.path.isdir(directorio):
        os.makedirs(directorio, exist_ok=True)

    comando = [
        "rpicam-still",
        "-o", ruta_salida,
        "--width", str(ancho),
        "--height", str(alto),
        "--timeout", str(tiempo_espera_ms),
    ]
    if sin_preview:
        comando.append("-n")

    try:
        r = subprocess.run(comando, capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            print("Error rpicam-still:", r.stderr or r.stdout)
            return None
        if os.path.isfile(ruta_salida):
            print("Imagen guardada:", ruta_salida)
            return ruta_salida
        return None
    except FileNotFoundError:
        print("Error: no se encontró 'rpicam-still'. Instala: sudo apt install -y rpicam-apps")
        return None
    except subprocess.TimeoutExpired:
        print("Error: tiempo de espera agotado.")
        return None


# ----- Ejemplo básico -----
if __name__ == "__main__":
    # 1) Captura simple: una foto con nombre automático (fecha/hora) en la misma carpeta
    ruta = capturar_imagen()
    if ruta:
        print("OK:", ruta)
    else:
        print("Fallo al capturar.")

    # 2) Captura guardando en un archivo concreto (descomenta para usar):
    # capturar_imagen(ruta_salida="mi_foto.jpg")
    # capturar_imagen(ruta_salida="/home/pi/fotos/salon.jpg", ancho=1280, alto=720)
