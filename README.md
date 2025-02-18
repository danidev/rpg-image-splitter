# RPG Image Splitter

**RPG Image Splitter** is a Python script that resizes and splits an image into multiple A4-sized sections for easy printing.
It's ideal for RPG battlemaps, ensuring the best possible fit while maintaining the original aspect ratio.

## Features
✔️ Supports **PNG** and **JPEG** images
✔️ **Maintains aspect ratio** while resizing
✔️ **Splits images** across multiple A4 sheets (default: 2x2 grid)
✔️ Saves output images in the **same folder** as the original file
✔️ Automatically **detects orientation** (landscape/portrait)

## Installation

### 1. Install Python
Ensure you have Python **3.8+** installed.
[Download Python](https://www.python.org/downloads/) if needed.

### 2. Install Dependencies
Use `pip` to install the required library:

```sh
pip install pillow
```

### Usage

#### Option 1: Running as a script
If you're using `splitter.py` as a standalone script, run:

```sh
python splitter.py "<image_path>" [scale_factor]
```

**Example:**
```sh
python splitter.py "battlemap.jpg" 2
```
This will resize `battlemap.png` to fit **4 A4 sheets (2x2 grid)** and save the parts as:

```
battlemap_part_1.jpg
battlemap_part_2.jpg
battlemap_part_3.jpg
battlemap_part_4.jpg
```

#### Option 2: Running as a package
If you're running the script from the installed package, use:

```sh
python -m rpg_image_splitter.splitter "<image_path>" [scale_factor]
```

**Example:**
```sh
python -m rpg_image_splitter.splitter "battlemap.png" 2
```

If you want **even larger prints**, increase `scale_factor` (e.g., `3` for 3x3 = 9 A4 sheets).

## License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

## Future Enhancements (TODO)
🔹 Add GUI support (Tkinter/PyQt)
🔹 Improve error handling & logging
🔹 Support more image formats

## Contributing
Pull requests are welcome! Feel free to open an issue or suggest features.

🚀 Happy printing & enjoy your RPG battlemaps!