import streamlit as st
from PIL import Image
import numpy as np


def color_to_alpha(image, target_color, tolerance):
    """
    Convert pixels with colors similar to the target color to alpha channel in the image.

    Parameters:
    image (PIL.Image): The input image.
    target_color (tuple): The RGB color to convert to alpha.
    tolerance (int): The allowed difference in RGB values for a pixel to be considered similar.

    Returns:
    PIL.Image: The resulting image with the specified colors converted to alpha.
    """
    img = image.convert("RGBA")
    data = np.array(img)
    red, green, blue, alpha = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    
    # Calculate the difference between each pixel's RGB values and the target color
    difference = np.sqrt((red - target_color[0])**2 + (green - target_color[1])**2 + (blue - target_color[2])**2)
    
    # Create a mask for pixels within the tolerance range of the target color
    mask = difference <= tolerance
    
    # Set alpha channel to 0 for pixels within the tolerance range
    alpha[mask] = 0
    
    # Update the image with the modified alpha channel
    img_with_alpha = Image.fromarray(np.dstack((red, green, blue, alpha)))
    
    return img_with_alpha


def main():
    st.title("Color to Alpha Effect")

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)

        # Get the color to convert to alpha
        color_str = st.text_input("Enter the color to convert to alpha (e.g., '255,255,255' for white):")
        color = tuple(map(int, color_str.split(','))) if color_str else None

        # Get the tolerance value
        tolerance = st.slider("Tolerance", 0, 100, 20)

        if color:
            st.write("Converting similar colors to alpha...")
            alpha_image = color_to_alpha(image, color, tolerance)
            st.image(alpha_image, caption="Image with Color Converted to Alpha", use_column_width=True)
        else:
            st.warning("Please enter a valid color.")

if __name__ == "__main__":
    main()
