import os
import re

archivos = [f for f in os.listdir('.') if f.lower().endswith('.jpg') and 'libro' in f.lower()]

# Extraer número del nombre de archivo, por ejemplo "libro 9.jpg" → 9
def extraer_numero(nombre):
    match = re.search(r'(\d+)', nombre)
    return int(match.group(1)) if match else 0

# Ordenar los archivos según su número
archivos.sort(key=extraer_numero)

# Renombrar con ceros a la izquierda
for i, nombre in enumerate(archivos, start=1):
    nuevo_nombre = f"libro {i:03}.jpg"
    os.rename(nombre, nuevo_nombre)
    print(f'Renombrado: {nombre} → {nuevo_nombre}')
