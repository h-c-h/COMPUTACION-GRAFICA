import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def main():
    if not glfw.init():
        return

    window = glfw.create_window(600, 600, "Cubo 3D con OpenGL", None, None)
    glfw.make_context_current(window)

    glEnable(GL_DEPTH_TEST)  # Para ver correctamente en 3D

    angle = 0

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Configuración de la proyección
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, 1, 0.1, 10)

        # Cámara
        gluLookAt(1.5, 1.5, 3,   # posición de la cámara
                  0, 0, 0,       # a dónde mira
                  0, 1, 0)       # vector "arriba"

        # Modelo
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Rotación para que se vea mejor
        glRotatef(angle, 1, 1, 1)

        # Dibujar un cubo (6 caras)
        glBegin(GL_QUADS)

        # Cara frontal (Z+)
        glColor3f(1, 1, 0)  
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)

        # Cara trasera (Z-)
        glColor3f(1, 0, 0)  
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f(-0.5,  0.5, -0.5)

        # Cara izquierda (X-)
        glColor3f(0, 1, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5, -0.5)

        # Cara derecha (X+)
        glColor3f(0, 0, 1)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, -0.5,  0.5)
        glVertex3f(0.5,  0.5,  0.5)
        glVertex3f(0.5,  0.5, -0.5)

        # Cara superior (Y+)
        glColor3f(0, 1, 1)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f( 0.5, 0.5, -0.5)
        glVertex3f( 0.5, 0.5,  0.5)
        glVertex3f(-0.5, 0.5,  0.5)

        # Cara inferior (Y-)
        glColor3f(1, 0, 1)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f(-0.5, -0.5,  0.5)

        glEnd()

        glfw.swap_buffers(window)
        glfw.poll_events()

        # Animación
        angle += 1

    glfw.terminate()

main()
