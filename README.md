### 💻 How to Use This Script on Your Operating System

#### ✅ Linux (Debian, Ubuntu, Fedora, Arch, etc.)

No additional installation is required. Python 3 is pre-installed on most distributions.

```bash
python3 renombrar.py
```

---

#### 🪟 Windows

1. **Install Python** (if not already installed):

   * Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
   * Download the latest version of Python 3.x for Windows.
   * During installation, make sure to check **"Add Python to PATH"** before clicking "Install Now".

2. **Verify the installation**:
   Open the Command Prompt (search for "cmd" or "PowerShell") and run:

   ```bash
   python --version
   ```

   If it shows something like `Python 3.x.x`, you're good to go.

3. **Run the script**:

   * Navigate to the folder containing your files and the script. For example:

     ```bash
     cd "C:\Users\YourUsername\Pictures\Libro"
     ```

   * Then run:

     ```bash
     python renombrar.py
     ```

---

#### 🍎 macOS

1. **Check if Python 3 is installed**:
   Open Terminal (via Spotlight or Launchpad) and run:

   ```bash
   python3 --version
   ```

   If it shows a Python 3 version, you can run the script with:

   ```bash
   python3 renombrar.py
   ```

2. **If Python 3 is not installed**:

   * Install [Homebrew](https://brew.sh/) if you don’t have it:

     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

   * Then install Python:

     ```bash
     brew install python
     ```

   * Finally, run the script:

     ```bash
     python3 renombrar.py
     ```

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


