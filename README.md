# image-bit-slicer

Generates and slices a grayscale image into its 8 binary bit planes.

This project creates a synthetic grayscale image, then decomposes it into its individual 8 bit planes. Each bit plane is saved as a separate binary image, visualizing how different bit depths contribute to the overall pixel intensity.

## How it works

1.  A `256x256` grayscale image with a horizontal gradient (pixel values from 0 to 255) is synthetically generated.
2.  The script then extracts each of the 8 bit planes (from the least significant bit, bit 0, to the most significant bit, bit 7).
3.  Each extracted bit plane is converted into a binary image (0 for pixels where the bit is unset, 255 for pixels where the bit is set).
4.  All generated images (the original grayscale image and its 8 bit planes) are saved as PNG files in an `output_bit_planes` directory.

## Requirements

You need `opencv-python` and `numpy` installed.

```bash
pip install -r requirements.txt
```

## How to Run

Navigate to the project directory and execute the main script:

```bash
python main.py
```

## Output

After running, an `output_bit_planes` directory will be created in the same location as `main.py`. This directory will contain:

*   `original_grayscale_image.png`: The synthetic grayscale gradient image.
*   `bit_plane_0.png`: The image representing the least significant bit.
*   `bit_plane_1.png`: ...and so on...
*   `bit_plane_7.png`: The image representing the most significant bit.