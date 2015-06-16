#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image
import requests

#depend on tesseract-ocr

header = {'Cookie': 'saeut=218.108.135.246.1416190347811282; PHPSESSID=5f3d9f5685452d1474f59371067e36af'}

def vcode():
	pic_url = 'http://1.hacklist.sinaapp.com/vcode7_f7947d56f22133dbc85dda4f28530268/vcode.php'
	r = requests.get(pic_url, headers=header, timeout=10)
	with open('vcode.png', 'wb') as pic:
		pic.write(r.content)
	text = pytesseract.image_to_string(Image.open('vcode.png'))
	text = text.replace(' ', '')
	if text != '':
		return text
	else:
		return vcode()

print(vcode())
