# Image Splitter for A4 Printing

rpg-image-splitter is a Python script that resizes and splits an image into multiple A4-sized sections for easy printing. Ideal for RPG battlemaps, it ensures the best possible fit while maintaining aspect ratio. Supports PNG and JPEG images and allows scaling to enhance detail.

## Features
✅ Automatically detects image orientation  
✅ Resizes image while preserving aspect ratio  
✅ Splits the image into multiple A4-sized sheets  
✅ Saves the output files in the same folder as the original image  
✅ Supports **PNG, JPG, and other common image formats**  

---

## Installation

This script requires Python and the **Pillow** library.

### Install Python (if not installed)
#### **Windows:**
1. Download and install Python from [python.org](https://www.python.org/downloads/)
2. Ensure Python and `pip` are added to the system PATH during installation.

#### **Linux/macOS:**
Most distributions come with Python pre-installed. If not, install it via:
```sh
sudo apt install python3  # Ubuntu/Debian
brew install python       # macOS
```

### Install Dependencies
Run the following command to install the required Python package:
```sh
pip install pillow
```

---

## Usage

### Basic Usage:
```sh
python split_image.py <image_path>
```
Example:
```sh
python split_image.py my_map.png
```
This will resize and split `my_map.png` into 4 A4-sized images.

### Enlarging the Image:
To **double** the image size before splitting (useful for better print quality):
```sh
python split_image.py my_map.png 2
```
To **triple** the size:
```sh
python split_image.py my_map.png 3
```

---

## Output Files
The script saves the split images in the **same folder as the original image**.  
For example, if your input file is:
```
/home/user/images/map.png
```
The output files will be:
```
/home/user/images/map_part_1.jpg
/home/user/images/map_part_2.jpg
/home/user/images/map_part_3.jpg
/home/user/images/map_part_4.jpg
```

---

## Troubleshooting

### Error: "cannot write mode RGBA as JPEG"
**Solution:** The input image has transparency. The script automatically converts it to RGB when saving as JPEG.

### Error: "ModuleNotFoundError: No module named 'PIL'"
**Solution:** Install Pillow using:
```sh
pip install pillow
```

---

## License

This project is licensed under the MIT License.  
Feel free to modify and distribute it as you wish. ⭐

---

## Contributing

If you have suggestions or improvements, feel free to fork the repository and submit a pull request! 🎉
