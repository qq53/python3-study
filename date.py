#!/usr/bin/env python3.4.4
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta, timezone

def to_timestamp(dt_str, tz_str):
	dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
	n = int(re.match(r'^UTC([+-]\d+):00$',tz_str).group(1))
	tz_utc = timezone(timedelta(hours=n))
	dt = dt.replace(tzinfo=tz_utc)
	ts = dt.timestamp()
	return ts

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-9:00')
assert t2 == 1433121030.0, t2
