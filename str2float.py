#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from functools import reduce

def str2float(str):
	def mul(x, y):
		return x * 10 + y
	def ch2int(c):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[c]
	for k,v in enumerate(str):
		if v == '.':
			break;
	return reduce(mul, map(ch2int, str[:k])) +\
			reduce(mul, map(ch2int, str[k+1:])) / pow(10,len(str[k+1:]))

print(str2float('123.456'))
