# pip install PyOpenGL glfw

import glfw
from OpenGL.GL import *

# --- NUEVO: Variables para la posición del cuadrado ---
# Posición inicial en el centro (0.0, 0.0)
square_x = 0.0
square_y = 0.0
move_speed = 0.1 # Velocidad a la que se moverá el cuadrado

# --- NUEVO: Función de callback para el teclado ---
# Esta función se ejecutará cada vez que se presione, suelte o repita una tecla.
def key_callback(window, key, scancode, action, mods):
    global square_x, square_y # Usamos 'global' para modificar las variables de fuera de la función

    # Solo nos interesa si la tecla está presionada (PRESS) o se mantiene presionada (REPEAT)
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            square_y += move_speed  # Mover hacia arriba
        elif key == glfw.KEY_DOWN:
            square_y -= move_speed  # Mover hacia abajo
        elif key == glfw.KEY_LEFT:
            square_x -= move_speed  # Mover hacia la izquierda
        elif key == glfw.KEY_RIGHT:
            square_x += move_speed  # Mover hacia la derecha

def main():
    # Inicializar GLFW
    if not glfw.init():
        return

    # Crear ventana
    window = glfw.create_window(800, 600, "Cuadrado que se mueve con el teclado", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # --- NUEVO: Registrar nuestra función de callback ---
    glfw.set_key_callback(window, key_callback)

    # Bucle principal
    while not glfw.window_should_close(window):
        # Color de fondo
        glClearColor(0.2, 0.3, 0.4, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # --- NUEVO: Aplicar la transformación de traslación ---
        glPushMatrix() # Guarda la matriz de transformación actual
        glTranslatef(square_x, square_y, 0.0) # Mueve el origen según nuestra posición

        # Dibujar un cuadrado (usando GL_QUADS)
        # Ahora lo dibujamos siempre alrededor del origen (0,0)
        # porque la traslación ya se encargó de moverlo a su sitio.
        glBegin(GL_QUADS)
        glColor3f(1, 0, 0)   # rojo
        glVertex2f(-0.5, -0.5)  # abajo izquierda
        glColor3f(0, 1, 0)   # verde
        glVertex2f(0.5, -0.5)   # abajo derecha
        glColor3f(0, 0, 1)   # azul
        glVertex2f(0.5, 0.5)    # arriba derecha
        glColor3f(1, 1, 0)   # amarillo
        glVertex2f(-0.5, 0.5)   # arriba izquierda
        glEnd()

        glPopMatrix() # Restaura la matriz de transformación original

        # Intercambiar buffers y eventos
        glfw.swap_buffers(window)
        glfw.poll_events() # Esencial para que se procesen los eventos como el teclado

    glfw.terminate()

if __name__ == "__main__":
    main()