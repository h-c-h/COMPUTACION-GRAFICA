# pip install PyOpenGL glfw

import glfw
from OpenGL.GL import *
import math


def main():
    # Inicializar GLFW
    if not glfw.init():
        return

    # Crear ventana
    window = glfw.create_window(900, 900, "Dibujar un círculo con OpenGL", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # Bucle principal
    while not glfw.window_should_close(window):
        # Fondo azul oscuro
        glClearColor(0.1, 0.1, 0.2, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujar un círculo en el centro
        glColor3f(1, 0.5, 0)  # naranja
        glBegin(GL_TRIANGLE_FAN)
        centrox = 0.3
        centroy = 0.3
        glVertex2f(centrox, centroy)
        #glVertex2f(0.3, 0.3)  # centro del círculo

        num_segments = 100   # más segmentos = círculo más suave
        radius = 0.3  # radio del círculo
        

        for i in range(num_segments + 1):
            angle = 2 * math.pi * i / num_segments
            x = centrox + radius * math.cos(angle)
            y = centroy + radius * math.sin(angle)
            glVertex2f(x, y)

        glEnd()
        
        # Intercambiar buffers y procesar eventos 
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
