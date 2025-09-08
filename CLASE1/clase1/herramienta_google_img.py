from pygoogle_image import image as pi


search_queries = [
    "chatgpt",
    "chatgpt 4",
    "chatgpt 4.5",
    "chatgpt 4.5 ollama"
]

# Límite de imágenes a descargar por cada término de búsqueda
image_limit = 2

# --- Bucle de Descarga ---
for query in search_queries:
    print(f"Buscando y descargando imágenes para: '{query}'")
    try:
        pi.download(keywords=query, limit=image_limit, output_dir="images")
    except Exception as e:
        print(f"Ocurrió un error con la búsqueda '{query}': {e}")

print("\n¡Descarga completada!")
print("Revisa las carpetas creadas en el mismo directorio que este script.")


