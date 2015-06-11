#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import struct
from enum import Enum, unique

@unique
class BMP(Enum):
	SIGN = 0
	SIZE = 1
	WIDTH = 5
	HEIGHT = 6
	COLOR = 8

with open('struct.bmp', 'rb') as f:
	h = f.read(30)
sh = struct.unpack('<2sIIIIIIHH', h)
if sh[BMP.SIGN.value] == b'BM':
	print('is bmp')
	print('size: %s x %s' % (sh[BMP.WIDTH.value], sh[BMP.HEIGHT.value]))
	print('color sum: %d' % sh[BMP.COLOR.value])
else:
	print('not bmp')
