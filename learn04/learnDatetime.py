# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    utc=re.match(r'^UTC([+|-])([\d]{1,2})\:(\d{2})$',tz_str)
    hours=utc.groups()[0]+utc.groups()[1]
    date=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz_utc=timezone(timedelta(hours=int(hours)))
    date=date.replace(tzinfo=tz_utc)
    return date.timestamp()

if __name__ == '__main__':
    #learn_now()
    #to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1

    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433121030.0, t2

    print('Pass')