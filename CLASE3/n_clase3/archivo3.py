import keyboard
import time
from OpenGL.GL import *
import glfw

# posicion del centro
pos_x = -0.5
pos_y = 0.5
# velocidad del cuadrado
# aceleracion 
dx = 0.01
dy = 0.01
# ->
def draw_square(x, y):
    glBegin(GL_QUADS)
    # r g b
    glColor3f(0.2, 0.7, 0.7)
    # coordenadas de los vertices
    glVertex2f(-0.1+pos_x, -0.1+pos_y)
    glVertex2f( 0.1+pos_x, -0.1+pos_y)
    glVertex2f( 0.1+pos_x,  0.1+pos_y)
    glVertex2f(-0.1+pos_x,  0.1+pos_y)
    glEnd()

def check_keys():
    global pos_x, pos_y, dx, dy
    if keyboard.is_pressed('up'):
        pos_y += dy
    if keyboard.is_pressed('down'):
        pos_y -= dy
    if keyboard.is_pressed('left'):
        pos_x -= dx
    if keyboard.is_pressed('right'):
        pos_x += dx

    time.sleep(0.01)

def main():
    global pos_x, pos_y, dx, dy
    if not glfw.init():
        return
    
    window = glfw.create_window(800, 800, "Move the Square with Arrow Keys", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        check_keys()
        draw_square(pos_x, pos_y)
        time.sleep(0.01)

        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()

if __name__ == "__main__":
    main()