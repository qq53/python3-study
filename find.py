#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import os, re, sys

srh = sys.argv[1] if len(sys.argv)>1 else ''
dirlist = ['.']
i = 0
while i < len(dirlist):
	tmp = dirlist[i]
	_filelist = [x for x in os.listdir(tmp)]
	_dirlist = map(lambda x: os.path.join(tmp,x), _filelist)
	_dirlist = list(filter(lambda x: os.path.isdir(x), _dirlist))
	dirlist = dirlist + _dirlist
	i = i + 1

for x in dirlist:
	filelist = os.listdir(x)
	filelist = map(lambda y: os.path.join(x,y), filelist)
	filelist = list(filter(lambda x:re.match(r'.*'+srh+'.*',x), filelist))
	for x in filelist:
		print(x)
