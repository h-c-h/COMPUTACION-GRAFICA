import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        return

    window = glfw.create_window(500, 500, "Triángulo", None, None)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_TRIANGLES)
        #         R  G   B
        glColor3f(0, 1, 1)   # Azul
        glVertex2f(-0.5, -0.5)
        glVertex2f(0.5, -0.5)
        glVertex2f(0.0, 0.5)
        glEnd()
        
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

main()
