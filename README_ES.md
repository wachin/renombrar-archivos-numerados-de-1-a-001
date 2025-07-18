# renombrar-archivos-numerados-de-1-a-001

Este script en Python (`renombrar.py`) permite **renombrar archivos numerados secuencialmente** agregando ceros a la izquierda, para que se ordenen correctamente en sistemas que usan orden alfabético.

### 🧠 ¿Para qué sirve?

Cuando tienes archivos como:

```

libro 1.jpg
libro 2.jpg
...
libro 10.jpg
libro 100.jpg

```

El sistema los ordena así (alfabéticamente):

```

libro 1.jpg
libro 10.jpg
libro 100.jpg
libro 2.jpg
...

```

Esto puede causar problemas al unir imágenes en un PDF o al procesar archivos por lote. Este script los renombra así:

```

libro 001.jpg
libro 002.jpg
...
libro 100.jpg

````

Con esto, se mantienen en orden correcto tanto en la terminal como en programas que dependan del nombre del archivo.

---

### ⚙️ Cómo usarlo

1. Coloca el script `renombrar.py` dentro de la carpeta donde están tus imágenes (o archivos que quieres renombrar).
2. Asegúrate de tener Python 3 instalado.
3. Abre una terminal en esa carpeta y ejecuta:

```bash
python3 renombrar.py
````

El script buscará todos los archivos `.jpg` que tengan la palabra "libro" en el nombre, extraerá su número, y los renombrará en orden con ceros a la izquierda: `libro 001.jpg`, `libro 002.jpg`, etc.

---

### 📌 Requisitos

* Python 3.x
* Archivos en formato `.jpg` con un número en el nombre (como `libro 1.jpg`, `libro 23.jpg`, etc.)

---

### 🧩 Personalización

Si deseas adaptar el script a otros formatos de imagen (`.jpeg`, `.png`) o a nombres distintos de `libro`, puedes modificar esta línea:

```python
archivos = [f for f in os.listdir('.') if f.lower().endswith('.jpg') and 'libro' in f.lower()]
```

---

### 📄 Licencia

Este proyecto es de uso Software Libre. Puedes modificarlo, compartirlo y adaptarlo según tus necesidades.

