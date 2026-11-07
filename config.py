import os

MAX_IMAGE_SIZE = 5  # Max image size in MB
PORT = int(os.environ.get("PORT", 8000))  # Heroku/Docker set PORT; defaults to 8000
