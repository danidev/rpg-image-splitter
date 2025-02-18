import os
import sys
from PIL import Image

# Constants for A4 size in pixels at 300 DPI
A4_WIDTH = 2480
A4_HEIGHT = 3508


def process_image(image_path, scale_factor=2):
    """
    Processes an image by resizing it to fit multiple A4 sheets while maintaining aspect ratio,
    then splits it into multiple parts for printing.

    Args:
        image_path (str): Path to the input image.
        scale_factor (int, optional): Determines how many A4 sheets the image should be spread across.
                                      Defaults to 2 (resulting in 2x2 = 4 sheets).
    """
    
    # Open the image
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Determine image orientation
    orientation = "landscape" if img_width > img_height else "portrait"
    print(f"The image is in {orientation} mode.")

    # Ensure the image fits into the scaled A4 grid while maintaining aspect ratio
    aspect_ratio = img_width / img_height
    scaled_width = A4_WIDTH * scale_factor
    scaled_height = A4_HEIGHT * scale_factor

    if aspect_ratio > (A4_WIDTH / A4_HEIGHT):
        # Scale based on width
        new_width = scaled_width
        new_height = int(new_width / aspect_ratio)
    else:
        # Scale based on height
        new_height = scaled_height
        new_width = int(new_height * aspect_ratio)

    # Resize the image
    img = img.resize((new_width, new_height), Image.LANCZOS)

    # Divide the image into equal parts
    cols = scale_factor
    rows = scale_factor
    part_width = new_width // cols
    part_height = new_height // rows

    # Get the original filename without extension
    base_name, _ = os.path.splitext(os.path.basename(image_path))

    # Determine the output folder (same as input image)
    output_folder = os.path.dirname(image_path)

    # Process each part
    for row in range(rows):
        for col in range(cols):
            left = col * part_width
            upper = row * part_height
            right = left + part_width
            lower = upper + part_height

            part = img.crop((left, upper, right, lower))

            # Ensure no alpha channel (convert RGBA to RGB if needed)
            if part.mode == "RGBA":
                part = part.convert("RGB")

            # Save the part in the same folder as the original image
            part_filename = os.path.join(output_folder, f"{base_name}_part_{row * cols + col + 1}.jpg")
            part.save(part_filename, format="JPEG")
            print(f"Saved: {part_filename}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_image.py <image_path> [scale_factor]")
        sys.exit(1)

    image_path = sys.argv[1]
    scale_factor = int(sys.argv[2]) if len(sys.argv) > 2 else 2  # Default to 2x2 grid

    try:
        process_image(image_path, scale_factor)
    except Exception as e:
        print(f"An error occurred: {e}")
