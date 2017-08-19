#!/usr/bin/env python3

from PIL import ImageGrab
from libraries.imgurpython.client import ImgurClient

import tkinter as tk
import tempfile

FILENAME = "temp.jpg"

def upload_to_imgur(client, img):

	print("Uploading image... ")
	image = client.upload_from_path(img, config=None, anon=False)
	print("Done")
	print()

	return image

def upload():
	client = ImgurClient("2595bbb929fab88", "fb4fd695ff057b6aa95768c08a5f9f8545b5c711")
	screen = tk.Tk()
	screen_width = screen.winfo_screenwidth()
	screen_height = screen.winfo_screenheight()
	img = ImageGrab.grab((0, 0, screen_width, screen_height))

	tf = tempfile.NamedTemporaryFile(mode='w', delete=False)
	tf_name = tf.name
	img.save(tf, 'JPEG')

	image = upload_to_imgur(client, tf_name)

	print("Image was posted! Go check your images you sexy beast!")
	print("You can find it here: {0}".format(image['link']))