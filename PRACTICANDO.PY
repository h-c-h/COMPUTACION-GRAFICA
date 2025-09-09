import pyautogui
import time

print("Mueve el mouse a la posición deseada. Presiona Ctrl+C para detener.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Coordenadas: X={x}, Y={y}", end="\r")  # imprime en la misma línea
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nPrograma terminado.")