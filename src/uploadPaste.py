#!/usr/bin/env python3

from PIL import ImageGrab
import tkinter as tk
from libraries import imgurpython

from datetime import datetime

def uploadPaste(client, img):

	print("Uploading image... ")
	image = client.upload(img, config=None, anon=False)
	print("Done")
	print()

	return image

if __name__ == "__main__":
	client = ImgurClient("2595bbb929fab88", "fb4fd695ff057b6aa95768c08a5f9f8545b5c711")
	screen = tk.Tk()
	screen_width = screen.winfo_screenwidth()
	screen_height = screen.winfo_screenheight()
	img = ImageGrab.grab((0, 0, screen_width, screen_height))
	image = uploadPaste(client, img)

	print("Image was posted! Go check your images you sexy beast!")
	print("You can find it here: {0}".format(image['link']))