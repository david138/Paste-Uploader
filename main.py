from libraries.imgurpython.client import ImgurClient
from src.uploadPaste import *

from PIL import ImageGrab
import tkinter as tk
from src.auth import authenticate

FILENAME = 'Kitten.jpg'

def uploadPaste(client):

    # Here's the metadata for the upload. All of these are optional, including
    # this config dict itself.
    config = {
        'album': None,
        'name':  'Catastrophe!',
        'title': 'Catastrophe!',
        'description': 'Cute kitten being cute on'
    }

    print("Uploading image... ")
    image = client.upload_from_path(FILENAME, config=config, anon=False)
    print("Done")
    print()

    return image

if __name__ == "__main__":
    client = authenticate()
    screen = tk.Tk()
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()
    img = ImageGrab.grab((0, 0, screen_width, screen_height))
   # img.save(FILENAME)
    image = uploadPaste(client)

    print("Image was posted! Go check your images you sexy beast!")
    print("You can find it here: {0}".format(image['link']))