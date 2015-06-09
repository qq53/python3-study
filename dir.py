#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

argv = sys.argv
if len(argv) < 2:
	print('need a param')
	exit()
dir = argv[1]
if os.path.isdir(dir) == False:
	print('param not a dir')
	exit()
for x in os.listdir(dir):
	print(x)
