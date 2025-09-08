# pip install PyOpenGL glfw

import glfw
from OpenGL.GL import *

def main():
    # Inicializar GLFW
    if not glfw.init():
        return

    # Crear ventana
    window = glfw.create_window(600, 600, "Dibujar un cuadrado con OpenGL", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # Bucle principal
    while not glfw.window_should_close(window):
        # Color de fondo
        glClearColor(0.2, 0.3, 0.4, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujar un cuadrado (usando GL_QUADS)
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

        # Intercambiar buffers y eventos
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
