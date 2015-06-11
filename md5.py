#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import hashlib

db = {}

def get_md5(s):
	md5 = hashlib.md5()
	s = s + 'the-Salt'
	md5.update(s.encode('utf-8'))
	return md5.hexdigest()

def register(username, password):
	db[username] = get_md5(password + username)

def login(username, password):
	pwd = get_md5(password + username)
	if db[username] == pwd:
		print('Login OK')
	else:
		print('Auth Fail')

register('admin', '123456')
login('admin', '12345611')
