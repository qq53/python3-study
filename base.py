#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(str):
	str = str + bytes('=' * (len(str)%4),encoding='utf8')
	return base64.b64decode(str)

assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
