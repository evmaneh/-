import streamlit as st
import requests

# Function to fetch Roblox account inventory decals count
def get_decals_count(user_id, api_key):
    # Endpoint to get user inventory
    url = f"https://api.roblox.com/users/{user_id}/inventory"
    
    # Sending GET request with API key
    headers = {'Authorization': f'Bearer {api_key}'}
    
    try:
        response = requests.get(url, headers=headers)
        # Check if request was successful
        if response.status_code == 200:
            inventory = response.json()
            # Counting decals in inventory
            decal_count = sum(1 for item in inventory if item['assetType'] == 'Decal')
            return decal_count
        else:
            st.error(f"Failed to fetch decal count. Status Code: {response.status_code}")
            return None
    except requests.exceptions.ConnectionError as e:
        st.error("Connection error occurred. Please check your network connection and try again.")
        st.error(f"Error Details: {e}")
        return None

# Streamlit app UI
def main():
    st.title("Roblox Decal Inventory Counter")
    st.write("Enter your Roblox UserID and API key below:")
    
    # User input for UserID and API key
    user_id = st.text_input("Enter Roblox UserID:")
    api_key = st.text_input("Enter Roblox API Key:", type="password")
    
    # Check if user submitted input
    if st.button("Fetch Decals Count"):
        # Check if both UserID and API key are provided
        if user_id and api_key:
            st.write("Fetching decal count...")
            decal_count = get_decals_count(user_id, api_key)
            if decal_count is not None:
                st.write(f"Total Decals in Inventory: {decal_count}")
            else:
                st.write("Failed to fetch decal count. Please check the error messages above.")
        else:
            st.error("Please enter both UserID and API key.")

if __name__ == "__main__":
    main()
