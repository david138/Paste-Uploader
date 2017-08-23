#!/usr/bin/env python3

from libraries.imgurpython.client import ImgurClient
import tempfile

def upload(snip):
    client = ImgurClient("2595bbb929fab88", "fb4fd695ff057b6aa95768c08a5f9f8545b5c711")
    snip_info = None

    print("Uploading...")
    tf_name = None
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tf:
        snip.save(tf, 'JPEG')
        tf_name = tf.name

        with open(tf_name, 'rb') as img_file:
            snip_info = client.upload(img_file, config=None, anon=False)

        print(format(snip_info['link']))
        return snip_info['link']