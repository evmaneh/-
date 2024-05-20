import streamlit as st
import numpy as np
import cv2

def color_to_alpha(img, color):
    """
    Converts a specific color to alpha (transparent) in an image.
    
    Args:
    - img (numpy.ndarray): Input image.
    - color (tuple): RGB color tuple to be converted to alpha.
    
    Returns:
    - numpy.ndarray: Image with the specified color converted to alpha.
    """
    alpha = np.ones((img.shape[0], img.shape[1]), dtype=np.float32)
    mask = np.all(img == color, axis=-1)
    alpha[mask] = 0
    return alpha

def main():
    st.title("Color to Alpha Effect")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        original_image = cv2.imdecode(file_bytes, 1)

        st.subheader("Original Image")
        st.image(original_image, channels="BGR")

        color_picker = st.color_picker("Select the color to make transparent", "#ffffff")
        color = tuple(int(color_picker[i:i+2], 16) for i in (1, 3, 5))

        alpha_image = color_to_alpha(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB), color)

        st.subheader("Alpha Image")
        st.image(alpha_image, channels="RGBA")

if __name__ == "__main__":
    main()
