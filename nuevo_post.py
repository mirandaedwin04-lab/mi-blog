import os
import datetime
from unicodedata import normalize

def limpiar_texto(texto):
    # Convierte "Hola Mundo" en "hola-mundo" para el nombre del archivo
    texto = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    return texto.lower().replace(" ", "-")

def crear_post():
    # 1. Pedir datos al usuario
    print("🤖 GENERADOR DE POSTS AUTOMÁTICO 🤖")
    titulo = input(">> Título del artículo: ")
    categoria = input(">> Categoría (Enter para 'Blog'): ") or "Blog"
    tags = input(">> Etiquetas (separadas por coma): ")

    # 2. Calcular fecha y nombre de archivo
    ahora = datetime.datetime.now()
    fecha_formato = ahora.strftime("%Y-%m-%d %H:%M")
    slug = limpiar_texto(titulo)
    nombre_archivo = f"content/{slug}.md"

    # 3. Crear el contenido del archivo (Plantilla)
    contenido = f"""Title: {titulo}
Date: {fecha_formato}
Category: {categoria}
Tags: {tags}
Slug: {slug}
Author: Edwin Miranda
Status: published

Escribe aquí tu contenido...
"""

    # 4. Guardar el archivo
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(contenido)

    print(f"\n✅ ¡Listo! Archivo creado en: {nombre_archivo}")
    print("---------------------------------------------")

if __name__ == "__main__":
    crear_post()