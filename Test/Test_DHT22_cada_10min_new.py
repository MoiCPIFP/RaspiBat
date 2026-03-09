"""
Lee cada 10 minutos: humedad y temperatura (DHT22, adafruit_dht/board) y además
mantiene el PIR (MotionSensor de gpiozero) activo todo el tiempo.

- Cada 10 minutos se registra: fecha/hora, temperatura, humedad y último estado conocido del PIR.
- Cada vez que el PIR detecta movimiento o deja de detectar, se registra un evento independiente.

DHT22: VCC 3.3V, DATA → GPIO, GND.
PIR:   VCC 3.3V/5V, OUT → GPIO, GND.
"""
import time
from datetime import datetime

from gpiozero import MotionSensor
import adafruit_dht
import board

# Pines GPIO (BCM). DHT22 y PIR en pines distintos.
PIN_DHT22 = 4
PIN_PIR = 18
INTERVALO_MINUTOS = 10
INTERVALO_SEGUNDOS = INTERVALO_MINUTOS * 60
LOG_FILE = "dht22_log.txt"

# Mapeo BCM -> board para DHT22
PIN_TO_BOARD = {
    4: board.D4,
    17: board.D17,
    27: board.D27,
    22: board.D22,
    5: board.D5,
    6: board.D6,
    13: board.D13,
    19: board.D19,
    26: board.D26,
}
BOARD_PIN = PIN_TO_BOARD.get(PIN_DHT22, board.D4)


def escribir_log(texto: str) -> None:
    print(texto)
    if not LOG_FILE:
        return
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(texto + "\n")
    except OSError as e:
        print("  (No se pudo escribir en log:", e, ")")


def main():
    dht = adafruit_dht.DHT22(BOARD_PIN)
    pir = MotionSensor(PIN_PIR)

    # Estado compartido del PIR
    pir_estado = {"texto": "Sin movimiento"}

    def on_motion():
        pir_estado["texto"] = "Movimiento"
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        escribir_log(f"{ahora} | EVENTO PIR: Movimiento detectado")

    def on_no_motion():
        pir_estado["texto"] = "Sin movimiento"
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        escribir_log(f"{ahora} | EVENTO PIR: Vuelve a estar tranquilo")

    pir.when_motion = on_motion
    pir.when_no_motion = on_no_motion

    escribir_log(
        f"DHT22 GPIO {PIN_DHT22} | PIR (MotionSensor) GPIO {PIN_PIR}. "
        f"Leyendo DHT22 cada {INTERVALO_MINUTOS} min. (Ctrl+C para salir)\n"
    )

    try:
        while True:
            ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Lectura DHT22
            temp_str = "—"
            hum_str = "—"
            try:
                temperatura = dht.temperature
                humedad = dht.humidity
                if temperatura is not None and humedad is not None:
                    temp_str = f"{temperatura:.1f} °C"
                    hum_str = f"{humedad:.1f} %"
            except RuntimeError:
                # Errores típicos del DHT (checksum, timeout)
                pass

            linea = (
                f"{ahora} | Temp: {temp_str} | Humedad: {hum_str} | "
                f"PIR (último estado): {pir_estado['texto']}"
            )
            escribir_log(linea)

            time.sleep(INTERVALO_SEGUNDOS)
    except KeyboardInterrupt:
        print("\nPrograma terminado.")
    finally:
        try:
            dht.exit()
        except Exception:
            pass
        pir.close()


if __name__ == "__main__":
    main()

