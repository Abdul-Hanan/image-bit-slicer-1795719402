import cv2
import numpy as np
import os

def create_synthetic_grayscale_image(width, height):
    """
    Generates a synthetic grayscale image with a horizontal gradient from 0 to 255.
    """
    # Create a 1D array representing the gradient from 0 to 255
    # If width is 256, this will be [0, 1, ..., 255]
    gradient_row = np.linspace(0, 255, width, dtype=np.uint8)

    # Tile this row to create a 2D image of the specified height
    image = np.tile(gradient_row, (height, 1))
    return image

def extract_bit_planes(image):
    """
    Extracts the 8 bit planes from an 8-bit grayscale image.
    Each bit plane is returned as a binary image (0 or 255).
    """
    if image.dtype != np.uint8:
        raise ValueError("Input image must be of type np.uint8 for 8-bit plane extraction.")
    
    bit_planes = []
    for i in range(8):  # Iterate through 8 bits (0 to 7)
        # Extract the i-th bit from each pixel value
        # (image >> i) shifts bits to the right, bringing the i-th bit to the LSB position
        # & 1 isolates the LSB, resulting in 0 or 1 for each pixel
        bit_plane = (image >> i) & 1
        
        # Convert the 0/1 bit plane to a displayable binary image (0 or 255)
        # Multiplying by 255 makes the '1' bits visible as white.
        display_plane = (bit_plane * 255).astype(np.uint8)
        bit_planes.append((i, display_plane))
    return bit_planes

def main():
    project_name = "image-bit-slicer"
    output_dir = "output_bit_planes"
    
    print(f"[{project_name}] Starting project execution...")
    print(f"[{project_name}] Ensuring output directory '{output_dir}' exists...")
    os.makedirs(output_dir, exist_ok=True)

    # 1. Generate a synthetic grayscale image
    image_width = 256
    image_height = 256
    print(f"[{project_name}] Generating a {image_width}x{image_height} synthetic grayscale image...")
    original_grayscale_image = create_synthetic_grayscale_image(image_width, image_height)
    
    # Save the original image
    original_output_path = os.path.join(output_dir, "original_grayscale_image.png")
    cv2.imwrite(original_output_path, original_grayscale_image)
    print(f"[{project_name}] Original grayscale image saved to '{original_output_path}'")

    # 2. Extract bit planes
    print(f"[{project_name}] Extracting 8 bit planes from the image...")
    extracted_planes = extract_bit_planes(original_grayscale_image)

    # 3. Save each bit plane as a separate binary image
    for bit_index, plane_image in extracted_planes:
        plane_output_path = os.path.join(output_dir, f"bit_plane_{bit_index}.png")
        cv2.imwrite(plane_output_path, plane_image)
        print(f"[{project_name}] Bit plane {bit_index} saved to '{plane_output_path}'")
    
    print(f"[{project_name}] All bit planes successfully extracted and saved.")
    print(f"[{project_name}] Project finished. Check the '{output_dir}' directory for results.")

if __name__ == "__main__":
    main()