#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def triangle():
	l1 = [1]
	i = 1
	while True:
		l2 = []
		for l in range(0,i-2):
			l2.append(l1[l] + l1[l+1])
		l2.insert(0,1);
		if i > 1:
			l2.append(1);
		yield l2
		l1 = l2
		i = i + 1

n = 0
for t in triangle():
	print(t)
	n = n + 1
	if n == 10:
		break
