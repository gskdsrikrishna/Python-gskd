import requests
import json

def get_google_access_token(client_id, client_secret, authorization_code, redirect_uri):
    token_url = 'https://oauth2.googleapis.com/token'
    payload = {
        'code': authorization_code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    response = requests.post(token_url, data=payload)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        return None

def get_google_user_info(access_token):
    user_info_url = f'https://www.googleapis.com/oauth2/v1/userinfo?access_token={access_token}'
    response = requests.get(user_info_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def login_with_google(client_id, client_secret, redirect_uri):
    authorization_code = input("Enter the authorization code: ")
    access_token = get_google_access_token(client_id, client_secret, authorization_code, redirect_uri)
    if access_token:
        user_info = get_google_user_info(access_token)
        if user_info:
            # Extract relevant user information
            email = user_info['email']
            name = user_info['name']
            # Perform additional login logic or user registration

            print("Login successful!")
            print("Email:", email)
            print("Name:", name)
            return
    print("Google login failed.")

# Example usage
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'your_redirect_uri'

login_with_google(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
