import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        return

    window = glfw.create_window(500, 500, "Punto", None, None)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(10)  # Tamaño del punto
        glBegin(GL_POINTS)
        #         R  G  B
        glColor3f(1, 0, 0)  # Rojo
        glVertex2f(0.0, 0.0)  # Centro

        #glColor3f(0, 1, 0)  # Verde
        glVertex2f(1, 0.0)  # Centro

        glVertex2f(0.3, 0.0)  # Centro
        glEnd()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

main()

