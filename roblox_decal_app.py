import streamlit as st
import requests

def fetch_inventory(user_id):
    # Make a request to Roblox API to get the user's inventory
    url = f"https://inventory.roblox.com/v2/users/{user_id}/inventory"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error(f"Failed to fetch inventory. Error code: {response.status_code}")

def count_decals(inventory):
    # Count how many decals are in the inventory
    decal_count = 0
    for item in inventory["data"]:
        if item["assetType"]["name"] == "Decal":
            decal_count += 1
    return decal_count

def main():
    st.title("Roblox Decal Counter")

    user_id = st.text_input("Enter your Roblox UserID:")
    if st.button("Count Decals"):
        if user_id:
            inventory = fetch_inventory(user_id)
            if inventory:
                decal_count = count_decals(inventory)
                st.success(f"Number of decals in inventory: {decal_count}")
        else:
            st.warning("Please enter a valid Roblox UserID.")

if __name__ == "__main__":
    main()
