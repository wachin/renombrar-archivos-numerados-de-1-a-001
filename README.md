# rename-numbered-files-from-1-to-001

This Python script (`renombrar.py`) renames sequentially numbered files by **adding leading zeros** to ensure proper alphabetical order.

### 🧠 What is it for?

When you have files like:

```

libro 1.jpg
libro 2.jpg
...
libro 10.jpg
libro 100.jpg

```

Most systems sort them alphabetically like this:

```

libro 1.jpg
libro 10.jpg
libro 100.jpg
libro 2.jpg
...

```

This breaks the expected numerical order. The script renames them like:

```

libro 001.jpg
libro 002.jpg
...
libro 100.jpg

````

That way, the order is preserved in both terminals and any software that relies on filenames.

---

### ⚙️ How to use

1. Place the `renombrar.py` script in the folder containing your image files.
2. Make sure Python 3 is installed on your system.
3. Open a terminal in that folder and run:

```bash
python3 renombrar.py
````

The script looks for all `.jpg` files with the word "libro" in the filename, extracts their number, and renames them using three-digit formatting (e.g. `libro 001.jpg`, `libro 002.jpg`, etc.).

---

### 📌 Requirements

* Python 3.x
* `.jpg` image files with numbers in their names (e.g. `libro 1.jpg`, `libro 23.jpg`, etc.)

---

### 🧩 Customization

To use other image formats (like `.jpeg` or `.png`) or different filename prefixes, you can modify this line:

```python
archivos = [f for f in os.listdir('.') if f.lower().endswith('.jpg') and 'libro' in f.lower()]
```

---

### 📄 License

This project is Free Software to use. You can modify, share, and adapt it as needed.


