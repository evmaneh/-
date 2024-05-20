import streamlit as st
from PIL import Image


def color_to_alpha(image, color):
    """
    Convert a specific color to alpha channel in the image.

    Parameters:
    image (PIL.Image): The input image.
    color (tuple): The RGB color to convert to alpha.

    Returns:
    PIL.Image: The resulting image with the specified color converted to alpha.
    """
    img = image.convert("RGBA")
    data = img.getdata()
    new_data = []
    for item in data:
        # Change all pixels that match the specified color to transparent
        if item[:3] == color:
            new_data.append((item[0], item[1], item[2], 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
    return img


def main():
    st.title("Color to Alpha Effect")

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)

        # Get the color to convert to alpha
        color_str = st.text_input("Enter the color to convert to alpha (e.g., '255,255,255' for white):")
        color = tuple(map(int, color_str.split(','))) if color_str else None

        if color:
            st.write("Converting specified color to alpha...")
            alpha_image = color_to_alpha(image, color)
            st.image(alpha_image, caption="Image with Color Converted to Alpha", use_column_width=True)
        else:
            st.warning("Please enter a valid color.")

if __name__ == "__main__":
    main()
