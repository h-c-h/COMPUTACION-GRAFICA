# pip install PyOpenGL glfw mouse

import glfw
import mouse
from OpenGL.GL import *

state = {
    "cx": 0.0,
    "cy": 0.0,
    "size": 0.2  # tamaño del cuadrado
}

def window_to_ndc(window, x, y):
    """Convierte coords de pantalla (px) a NDC (-1..1)."""
    w, h = glfw.get_window_size(window)
    if w == 0 or h == 0:
        return 0.0, 0.0
    nx = (x / w) * 2.0 - 1.0
    ny = 1.0 - (y / h) * 2.0
    return nx, ny

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Cuadrado con mouse lib", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.swap_interval(1)

    w, h = glfw.get_framebuffer_size(window)
    glViewport(0, 0, w, h)

    # Obtener posición inicial del mouse
    mx, my = mouse.get_position()
    nx, ny = window_to_ndc(window, mx % w, my % h)
    state["cx"], state["cy"] = nx, ny

    while not glfw.window_should_close(window):
        # Leer posición del mouse (global en pantalla)
        mx, my = mouse.get_position()
        # Lo reducimos al tamaño de la ventana
        mx_local = mx % w
        my_local = my % h
        state["cx"], state["cy"] = window_to_ndc(window, mx_local, my_local)

        # Limpiar fondo
        glClearColor(0.1, 0.1, 0.15, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujar cuadrado
        cx, cy, s = state["cx"], state["cy"], state["size"]
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.3, 0.2)  # rojo/naranja
        glVertex2f(cx - s/2, cy - s/2)
        glVertex2f(cx + s/2, cy - s/2)
        glVertex2f(cx + s/2, cy + s/2)
        glVertex2f(cx - s/2, cy + s/2)
        glEnd()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
