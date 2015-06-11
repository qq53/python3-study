#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from functools import reduce

def prod(L):
	def add(x, y):
		return x + y
	return reduce(add, L)

print(prod(range(1,10)))
