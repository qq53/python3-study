#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def move(n, a, b, c):
	if n == 1:
		print('%s --> %s' % (a,c))
	else:
		move(n-1, a, c, b)
		move(1, a, b, c)
		move(n-1, b, a, c)

print('input n:')
n = 0
while int(n) <= 0:
	n = input()

move(int(n),'A','B','C')
