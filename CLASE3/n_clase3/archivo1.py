import keyboard
import time

w=0 # bandera de salida -> break
while w==0:
    
    if keyboard.is_pressed('up'):
        print("up")
    if keyboard.is_pressed('down'):
        print("down")
    if keyboard.is_pressed('left'):
        print("left")
    if keyboard.is_pressed('right'):
        print("right")
    if keyboard.is_pressed('q'):
        w=1
        print("exit")

    # pequeña pausa 
    time.sleep(0.08)