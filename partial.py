#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

int3 = functools.partial(int, base=3)

print(int3('12'))
