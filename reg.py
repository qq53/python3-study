#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

c = ''
while True: 
	c = input()
	exit() if c == 'q' else True
	g = re.match(r'([\w\.]+)@\w+\.\w{2,3}', c)
	if g != None:
		print('name: ' + g.groups()[0])
