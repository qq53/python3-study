#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import struct

with open('struct.bmp', 'rb') as f:
	h = f.read(30)
sh = struct.unpack('<ccIIIIIIHH', h)
if h[:2] == 'BM':
	print('yes')
