# Librerias a emplear
import time
import board
import adafruit_dht

# Datos en GPIO14
datos = adafruit_dht.DHT22(board.D14)

# Bucle de recogida de datos
while True:
    # Comprobar que los datos son correctos
    try:
        temp = datos.temperature      # °C
        hum = datos.humidity          # %

        if temp is not None and hum is not None:
            print(f"Temp: {temp:.1f} °C  Humedad: {hum:.1f} %")
        # Si no ha tomado algun dato, no mostrarlo
        else:
            print("Lectura no válida")

    # Si el calculo de comprobación de datos sale mal
    except RuntimeError as e:
        print("Error de lectura:", e)

    time.sleep(2)   # mínimo 2 s según el datasheet