import os
from dotenv import load_dotenv

load_dotenv()

API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")
API_KEY_TWITTER = os.getenv("API_KEY_TWITTER")
API_KEY_NEWSAPI = os.getenv("API_KEY_NEWSAPI")
RABBITMQ_URL = os.getenv("RABBITMQ_URL")

required_keys = [API_KEY_OPENAI, API_KEY_TWITTER, API_KEY_NEWSAPI, RABBITMQ_URL]

if not all(required_keys):
    raise ValueError("One or more required environment variables are missing.")
