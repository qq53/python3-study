#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import re
from urllib import request
import html

with request.urlopen(r'https://www.python.org/events/python-events') as f:
	if f.status == 200:
		data = f.read().decode('utf8')
		data = html.unescape(data)
		recent = re.findall(r'(<ul class="list-recent-events menu">.+?</ul>)',data,re.S)
		time = re.findall(r'<time.*?>(.+?)</time>',recent[0],re.S)
		time = list(map(lambda x:re.findall(r'(.+?) ?<',x)[0],time))
		event = re.findall(r'<h3 class="event-title">(.+?)</h3>',recent[0],re.S)
		event = list(map(lambda x:re.findall(r'<a.+?>(.+)</a>',x)[0],event))
		place = re.findall(r'<span class="event-location">(.+?)</span>',recent[0],re.S)
		print('---Python Events Calendar [Upcoming Events]---\n')
		for i in range(0,len(time)):
			print('Date: ' + time[i])
			print('Event: ' + event[i])
			print('Location: ' + place[i] + '\n')
