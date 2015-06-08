#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*arg, **kw):
			print('begin call')
			res = func(*arg, **kw)
			print('end call')
		return wrapper
	if isinstance(text, str):
		print(text)
		return decorator
	else:
		return decorator(text)

@log('execute')
def f():
	pass

f()
