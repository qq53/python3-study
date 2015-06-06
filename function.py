#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
	return (-b+math.sqrt(b**2-4*a*c))/2*a, (-b-math.sqrt(b**2-4*a*c))/2*a

print(quadratic(1,2,1))
