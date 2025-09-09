import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    if not glfw.init():
        return

    window = glfw.create_window(500, 500, "Cámara en Perspectiva", None, None)
    glfw.make_context_current(window)

    glEnable(GL_DEPTH_TEST)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # angulo, aspecto, cerca, lejos
        # aspecto = alto/ancho
        #gluPerspective(60, 1, 0.1, 10)  # Ángulo de cámara
        gluPerspective(60, 1, 0.1, 10)  # Ángulo de cámara
        gluLookAt(1, 1, 5,    # posicion de la camara
                  0, 0, 0,   # a dónde mira
                  0, 0, 1)  # Cámara virtual
        # posicion de la camara (0,0,0) mirando al origen (0,0,0) con el eje Y hacia arriba (0,1,0)
        #gluLookAt(1, 1, 0.4, 0, 0, 0, 0, 1, 0)  # Cámara virtual
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glBegin(GL_QUADS)
        glColor3f(1, 1, 0)  # Amarillo
        glVertex3f(-0.5, -0.5, 0)
        glVertex3f( 0.5, -0.5, 0)
        glVertex3f( 0.5,  0.5, 0)
        glVertex3f(-0.5,  0.5, 0)
        glEnd()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

main()
