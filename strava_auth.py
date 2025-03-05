from stravalib import Client
from dotenv import dotenv_values
import webbrowser


def get_code():
    secrets = dotenv_values(".env")

    client = Client()
    url = client.authorization_url(
        client_id= secrets["CLIENT_ID"],
        redirect_uri="http://127.0.0.1:5000/authorization",
        scope = 'activity:read_all',
        approval_prompt = 'auto'
    )

    #webbrowser.open(url) # Authorize the application in web browser

    webbrowser.open_new_tab(url)

def get_token(your_code):
    secrets = dotenv_values(".env")
    client = Client()
    
    token_response = client.exchange_code_for_token(
        client_id=secrets["CLIENT_ID"], client_secret=secrets['CLIENT_SECRET'], code=your_code
    )

    # The token response above contains both an access_token and a refresh token.
    access_token = token_response["access_token"]
    refresh_token = token_response["refresh_token"]  # You'll need this in 6 hours
    print(token_response)
    return token_response

get_code()
