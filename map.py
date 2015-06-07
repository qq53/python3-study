#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def normalize(str):
	return str[:1].upper() + str[1:]

a = ['jack','rose']
lst = list(map(normalize,a))
print(lst)
