#!/usr/bin/env python3
import PIL
from PIL import Image
import os
import sys

path = os.path.expanduser('~') + '/images/'
new_path = '/opt/icons/'

for image in os.listdir(path):
  if '.' not in image[0]:
    im = Image.open(path +image)
    im.rotate(270).resize((128,128)).convert('RGB').save(new_path + image.split('.')[0],'jpeg')
    im.close()

