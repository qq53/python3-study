#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('struct.bmp')
# # 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# # 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# # 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.bmp', 'bmp')