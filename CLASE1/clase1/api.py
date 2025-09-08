import requests


# URL para una imagen de 400x300 píxeles
url = "https://picsum.photos/400/300"

print(f"Solicitando imagen desde: {url}")

try:
    # allow_redirects=True es el comportamiento por defecto, pero lo ponemos para ser explícitos
    response = requests.get(url, timeout=10, allow_redirects=True)

    # 1. Verificar si la petición fue exitosa (código 200-299)
    response.raise_for_status()  # Esto lanzará un error si el código no es 2xx

    # 2. Imprimir la URL final después de la redirección
    print(f"Redirigido a la URL final: {response.url}")

    # 3. (Opcional pero recomendado) Verificar que lo que descargamos es una imagen
    content_type = response.headers.get('content-type')
    if 'image' not in content_type:
        print(f"Error: El contenido no es una imagen, es de tipo '{content_type}'")
    else:
        # 4. Guardar como archivo local
        with open("imagen_random.jpg", "wb") as f:
            f.write(response.content)
        print("¡Éxito! Imagen descargada como imagen_random.jpg")

except requests.exceptions.RequestException as e:
    # Captura cualquier error relacionado con la librería requests (DNS, timeout, conexión, etc.)
    print(f"Error al realizar la petición: {e}")