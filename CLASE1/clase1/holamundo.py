import glfw
import OpenGL.GL as gl
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

class HolaMundoOpenGL:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.window = None
        self.texture = None
        self.shader_program = None
        
    def init_glfw(self):
        """Inicializa GLFW"""
        if not glfw.init():
            raise Exception("No se pudo inicializar GLFW")
            
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        
        self.window = glfw.create_window(self.width, self.height, "Hola Mundo - OpenGL", None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("No se pudo crear la ventana GLFW")
            
        glfw.make_context_current(self.window)
        
    def create_shaders(self):
        """Crea los shaders para renderizar texto"""
        vertex_shader_source = """
        #version 330 core
        layout (location = 0) in vec2 position;
        layout (location = 1) in vec2 texCoord;
        
        out vec2 TexCoord;
        
        void main()
        {
            gl_Position = vec4(position, 0.0, 1.0);
            TexCoord = texCoord;
        }
        """
        
        fragment_shader_source = """
        #version 330 core
        out vec4 FragColor;
        
        in vec2 TexCoord;
        
        uniform sampler2D textTexture;
        uniform vec3 textColor;
        
        void main()
        {
            vec4 sampled = vec4(1.0, 1.0, 1.0, texture(textTexture, TexCoord).r);
            FragColor = vec4(textColor, 1.0) * sampled;
        }
        """
        
        # Compilar vertex shader
        vertex_shader = gl.glCreateShader(gl.GL_VERTEX_SHADER)
        gl.glShaderSource(vertex_shader, vertex_shader_source)
        gl.glCompileShader(vertex_shader)
        
        # Verificar compilación del vertex shader
        if not gl.glGetShaderiv(vertex_shader, gl.GL_COMPILE_STATUS):
            error = gl.glGetShaderInfoLog(vertex_shader)
            raise Exception(f"Error compilando vertex shader: {error}")
            
        # Compilar fragment shader
        fragment_shader = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
        gl.glShaderSource(fragment_shader, fragment_shader_source)
        gl.glCompileShader(fragment_shader)
        
        # Verificar compilación del fragment shader
        if not gl.glGetShaderiv(fragment_shader, gl.GL_COMPILE_STATUS):
            error = gl.glGetShaderInfoLog(fragment_shader)
            raise Exception(f"Error compilando fragment shader: {error}")
            
        # Crear programa de shaders
        self.shader_program = gl.glCreateProgram()
        gl.glAttachShader(self.shader_program, vertex_shader)
        gl.glAttachShader(self.shader_program, fragment_shader)
        gl.glLinkProgram(self.shader_program)
        
        # Verificar enlace del programa
        if not gl.glGetProgramiv(self.shader_program, gl.GL_LINK_STATUS):
            error = gl.glGetProgramInfoLog(self.shader_program)
            raise Exception(f"Error enlazando programa de shaders: {error}")
            
        # Limpiar shaders
        gl.glDeleteShader(vertex_shader)
        gl.glDeleteShader(fragment_shader)
        
    def create_text_texture(self, text="¡Hola Mundo!", font_size=48):
        """Crea una textura con el texto renderizado"""
        # Crear imagen con texto
        img = Image.new('RGBA', (512, 128), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        try:
            # Intentar usar una fuente del sistema
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            try:
                # Fallback a otra fuente común
                font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", font_size)
            except:
                # Usar fuente por defecto
                font = ImageFont.load_default()
        
        # Obtener dimensiones del texto
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Centrar el texto
        x = (512 - text_width) // 2
        y = (128 - text_height) // 2
        
        # Dibujar texto en blanco
        draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
        
        # Convertir a array de numpy
        img_data = np.array(img)
        
        # Crear textura OpenGL
        self.texture = gl.glGenTextures(1)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture)
        
        # Configurar parámetros de textura
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
        
        # Subir datos de la imagen
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, 512, 128, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, img_data)
        
    def setup_geometry(self):
        """Configura la geometría para renderizar el texto"""
        # Coordenadas del quad (posición y coordenadas de textura)
        vertices = np.array([
            # posición        # coordenadas de textura
            -0.5,  0.2,       0.0, 1.0,  # esquina superior izquierda
             0.5,  0.2,       1.0, 1.0,  # esquina superior derecha
             0.5, -0.2,       1.0, 0.0,  # esquina inferior derecha
            -0.5, -0.2,       0.0, 0.0   # esquina inferior izquierda
        ], dtype=np.float32)
        
        # Índices para dibujar el quad
        indices = np.array([
            0, 1, 2,  # primer triángulo
            2, 3, 0   # segundo triángulo
        ], dtype=np.uint32)
        
        # Crear VAO y VBO
        self.vao = gl.glGenVertexArrays(1)
        self.vbo = gl.glGenBuffers(1)
        self.ebo = gl.glGenBuffers(1)
        
        gl.glBindVertexArray(self.vao)
        
        # Configurar VBO
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, gl.GL_STATIC_DRAW)
        
        # Configurar EBO
        gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, gl.GL_STATIC_DRAW)
        
        # Configurar atributos de vértices
        # Posición
        gl.glVertexAttribPointer(0, 2, gl.GL_FLOAT, gl.GL_FALSE, 4 * 4, None)
        gl.glEnableVertexAttribArray(0)
        
        # Coordenadas de textura
        gl.glVertexAttribPointer(1, 2, gl.GL_FLOAT, gl.GL_FALSE, 4 * 4, ctypes.c_void_p(2 * 4))
        gl.glEnableVertexAttribArray(1)
        
    def render(self):
        """Renderiza el texto"""
        # Limpiar pantalla con color de fondo
        gl.glClearColor(0.1, 0.1, 0.3, 1.0)  # Azul oscuro
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        
        # Usar programa de shaders
        gl.glUseProgram(self.shader_program)
        
        # Activar textura
        gl.glActiveTexture(gl.GL_TEXTURE0)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture)
        gl.glUniform1i(gl.glGetUniformLocation(self.shader_program, "textTexture"), 0)
        
        # Establecer color del texto
        text_color = np.array([1.0, 1.0, 0.0], dtype=np.float32)  # Amarillo
        gl.glUniform3fv(gl.glGetUniformLocation(self.shader_program, "textColor"), 1, text_color)
        
        # Habilitar blending para transparencia
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        
        # Dibujar
        gl.glBindVertexArray(self.vao)
        gl.glDrawElements(gl.GL_TRIANGLES, 6, gl.GL_UNSIGNED_INT, None)
        
        # Intercambiar buffers
        glfw.swap_buffers(self.window)
        
    def run(self):
        """Ejecuta el programa principal"""
        try:
            self.init_glfw()
            self.create_shaders()
            self.create_text_texture("¡Hola Mundo con OpenGL!")
            self.setup_geometry()
            
            print("¡Hola Mundo con OpenGL iniciado!")
            print("Presiona ESC para salir")
            
            # Bucle principal
            while not glfw.window_should_close(self.window):
                glfw.poll_events()
                
                # Salir con ESC
                if glfw.get_key(self.window, glfw.KEY_ESCAPE) == glfw.PRESS:
                    glfw.set_window_should_close(self.window, True)
                
                self.render()
                
        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Limpieza
            if hasattr(self, 'vao'):
                gl.glDeleteVertexArrays(1, [self.vao])
            if hasattr(self, 'vbo'):
                gl.glDeleteBuffers(1, [self.vbo])
            if hasattr(self, 'ebo'):
                gl.glDeleteBuffers(1, [self.ebo])
            if self.texture:
                gl.glDeleteTextures([self.texture])
            if self.shader_program:
                gl.glDeleteProgram(self.shader_program)
            
            glfw.terminate()

if __name__ == "__main__":
    import ctypes
    app = HolaMundoOpenGL()
    app.run()

