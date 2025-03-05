from stravalib import Client
from dotenv import dotenv_values
import webbrowser
from strava_auth import get_token

your_code_here = '324a685ea22ff187fb677f44a5353bf354a266af' #your code

get_token(your_code_here)