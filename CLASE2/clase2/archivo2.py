import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        return

    window = glfw.create_window(500, 500, "Línea", None, None)
    glfw.make_context_current(window)
    mov_x = 0
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glLineWidth(10)  # Grosor de la línea
        glBegin(GL_LINES)
        glColor3f(0, 1, 0)  # Verde
        glVertex2f(mov_x, 0)
        glVertex2f(mov_x + 0.5, 0)
        
        glEnd()
        mov_x += 0.001
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

main()
