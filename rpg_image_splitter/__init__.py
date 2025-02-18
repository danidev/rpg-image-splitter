"""
rpg-image-splitter: A utility for splitting and resizing images for RPG battlemaps.

This package provides functionality to:
- Resize images to fit multiple A4 sheets while maintaining aspect ratio.
- Split images into multiple parts for easy printing.
- Handle different image formats (PNG, JPEG).
"""

from .splitter import process_image

__version__ = "1.0.0"
__all__ = ["process_image"]
