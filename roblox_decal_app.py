import streamlit as st
import requests
from PIL import Image
import io
import random

# Streamlit layout
st.title('Roblox Mass Uploader')

# User input for Roblox API key and userid
roblox_api_key = st.text_input('Enter your Roblox API key:')
userid = st.text_input('Enter your user id:')

# Image upload
uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg", "tga", "bmp"])

# Slider for noise generator
noise_level = st.slider("Noise Level", 0, 100, 1)

def apply_noise_effect(image_data, noise_level):
    data = image_data.getdata()
    modified_data = []
    for pixel in data:
        # Check if the pixel tuple has three values (R, G, B)
        if len(pixel) != 3:
            continue
        r, g, b = pixel
        if random.random() < noise_level / 100:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
        modified_data.append((r, g, b))
    image_data.putdata(modified_data)
    return image_data


# Function to upload image to Roblox
def upload_image_to_roblox(api_key, user_id, image):
    # Prepare data
    data = {
        'assetType': 'Decal',  # Default to Decal
        'displayName': 'Kegen Yassupload Sest!',
        'description': 'Check it out!',
        'creationContext': {
            'creator': {
                'userId': user_id
            }
        }
    }
    headers = {'x-api-key': api_key}

    # Convert image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # Prepare multipart form data
    files = {'fileContent': img_byte_arr}
    response = requests.post('https://apis.roblox.com/assets/v1/assets', headers=headers, data=data, files=files)
    
    return response

# Button to start uploading
if st.button('Start'):
    if roblox_api_key and userid and uploaded_file:
        # Load the image
        image = Image.open(uploaded_file)
        
        # Apply noise effect
        noisy_image = apply_noise_effect(image.copy(), noise_level)

        # Display original and noisy images
        st.image([image, noisy_image], caption=['Original Image', 'Noisy Image'], width=200)

        # Upload noisy image to Roblox
        response = upload_image_to_roblox(roblox_api_key, userid, noisy_image)
        
        # Display response
        st.write("Response from Roblox API:", response.text)
    else:
        st.error("Please fill in all the required fields.")
