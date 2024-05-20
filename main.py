import streamlit as st
import requests
from bs4 import BeautifulSoup

def check_approved_decals(user_id):
    url = f"https://www.roblox.com/users/{user_id}/inventory#!/decals"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    decals = soup.find_all('div', class_='item-card')
    approved_decals = []

    for decal in decals:
        button = decal.find('button', class_='btn-primary')
        if button and button.find('img'):
            approved_decals.append(decal.find('a')['href'])

    return approved_decals

def main():
    st.title("Roblox Approved Decal Checker")
    user_id = st.text_input("Enter your Roblox User ID:")
    if st.button("Check Approved Decals"):
        if user_id:
            try:
                approved_decals = check_approved_decals(user_id)
                if approved_decals:
                    st.success("Approved Decals Found!")
                    for decal in approved_decals:
                        st.write(decal)
                else:
                    st.warning("No approved decals found.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a valid User ID.")

if __name__ == "__main__":
    main()
