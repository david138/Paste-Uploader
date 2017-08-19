#!/usr/bin/env python3

from PIL import ImageGrab
from libraries.imgurpython.client import ImgurClient

import tkinter as tk
import tempfile

FILENAME = "temp.jpg"

def upload_to_imgur(client, img):

	print("Uploading image... ")
	image = client.upload(open(img, 'rb'), config=None, anon=False)
	print("Done")
	print()

	return image

def upload():
	client = ImgurClient("2595bbb929fab88", "fb4fd695ff057b6aa95768c08a5f9f8545b5c711")
	screen = tk.Tk()
	screen_width = screen.winfo_screenwidth()
	screen_height = screen.winfo_screenheight()
	img = ImageGrab.grab((0, 0, screen_width, screen_height))

	with tempfile.NamedTemporaryFile(mode='w', delete=False) as tf:
		img.save(tf, 'JPEG')
		tf.close()
		image = upload_to_imgur(client, tf.name)

		print("Image was posted! Go check your images you sexy beast!")
		print("You can find it here: {0}".format(image['link']))