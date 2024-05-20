import streamlit as st
import requests

def get_decals_count(user_id):
    url = f"https://www.roblox.com/Thumbs/Asset.ashx?width=110&height=110&assetId={user_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_urls = response.text.split(",")
            return len(image_urls)
        else:
            st.error("Failed to fetch user decals. Please check the user ID and try again.")
            return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

st.title("Roblox Decal Counter")
user_id = st.text_input("Enter Roblox UserID:")
if st.button("Count Decals"):
    if user_id.strip() == "":
        st.warning("Please enter a valid Roblox UserID.")
    else:
        decal_count = get_decals_count(user_id)
        if decal_count is not None:
            st.success(f"The user has {decal_count} decals.")
