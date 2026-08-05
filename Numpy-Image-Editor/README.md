# Numpy Image Editor
A command-line image editing tool built with **NumPy** and **Pillow (PIL)**.
Load an image, apply a series of transformations through an interactive menu, and save the result — all powered by direct NumPy array manipulation.

## Features
| # | Feature | Description |
|---|---------|-------------|
| 1 | Show Image Info | Displays dimensions, size, height, width, channels, and data type |
| 2 | Convert to Grayscale | Converts RGB to grayscale using weighted luminosity (`0.299R + 0.587G + 0.114B`) |
| 3 | Increase Brightness | Adds a user-defined value to every pixel, clamped to 0–255 |
| 4 | Decrease Brightness | Subtracts a user-defined value from every pixel, clamped to 0–255 |
| 5 | Flip Horizontally | Mirrors the image left-to-right |
| 6 | Flip Vertically | Mirrors the image top-to-bottom |
| 7 | Crop Image | Extracts a rectangular region defined by the user |
| 8 | Negative Image | Inverts all colors (`255 - pixel`) |
| 9 | Rotate Image | Rotates 90°, 180°, or 270° |
| 10 | Black & White Image | Converts to grayscale, then applies a threshold for pure black/white |
| 11 | Resize Image | Changes image dimensions using PIL's resize |
| 12 | Blur Image | Applies Gaussian blur with adjustable intensity |
| 13 | Save Image | Saves the current state to `.jpg` or `.png` |
| 14 | Exit | Prompts to save (if not already saved) and shows an edit summary |

## Requirements
```
numpy
Pillow
```

Install with:
```bash
pip install numpy pillow
```

## Usage
```bash
python new_project.py
```
You'll be prompted for an image path, then presented with a menu.
Each operation updates the image in place and displays the result immediately.
Choose **14** to exit — you'll be asked whether you've saved your changes.

## Project Structure
The project is built as a single class, `ImageEditor`, which:
- Stores the current image as a NumPy array in `self.img_array`
- Exposes one method per menu operation
- Methods that can fail (e.g. `crop`, `rotate`, `resize_image`) return `True`/`False` so the menu only calls `display_image()` on success
- `run()` contains the main menu loop
