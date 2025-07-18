# 💻 Cómo usar este script en tu sistema operativo

## ✅ Linux (Debian, Ubuntu, Fedora, Arch, etc.)

No necesitas instalar nada adicional. Python ya viene preinstalado.

```bash
python3 renombrar.py
```

---

## 🪟 Windows

1. **Instalar Python** (si no lo tienes):

   * Ve a [https://www.python.org/downloads/](https://www.python.org/downloads/)
   * Descarga la última versión de Python 3.x para Windows.
   * Durante la instalación, asegúrate de marcar la casilla: **"Add Python to PATH"** antes de hacer clic en "Install Now".

2. **Verificar la instalación**:
   Abre la consola (puedes buscar “cmd” o “Windows PowerShell”) y escribe:

   ```bash
   python --version
   ```

   Si ves algo como `Python 3.x.x`, está todo listo.

3. **Ejecutar el script**:

   * Navega con la terminal hasta la carpeta donde están tus archivos y el script, por ejemplo:

     ```bash
     cd "C:\Users\TuUsuario\Imágenes\Libro"
     ```

   * Luego ejecuta:

     ```bash
     python renombrar.py
     ```

---

## 🍎 macOS

1. **Verificar si tienes Python 3**:
   Abre la Terminal (desde Launchpad o Spotlight) y escribe:

   ```bash
   python3 --version
   ```

   Si ya tienes una versión de Python 3, puedes ejecutar el script con:

   ```bash
   python3 renombrar.py
   ```

2. **Si no tienes Python 3 instalado**:

   * Instala [Homebrew](https://brew.sh/) si no lo tienes:

     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

   * Luego instala Python:

     ```bash
     brew install python
     ```

   * Y ejecuta el script con:

     ```bash
     python3 renombrar.py
     ```

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

