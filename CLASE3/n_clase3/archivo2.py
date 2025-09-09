import keyboard
# autogui -> 


while True:
    # leer la tecla presionada
    event = keyboard.read_event()
    # si la tecla esta presionada (KEY_DOWN)
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Key {event.name} pressed")
        if event.name == 'esc':
            print("exit")
            break # salir del bucle -> bandera de salida