#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

def by_name(t):
	return t[1]

L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

print(sorted(L, key=by_name))
