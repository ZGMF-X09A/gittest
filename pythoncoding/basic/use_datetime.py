import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    m = re.match(r'^UTC([+-]\d{1,2}):00$', tz_str)
    tz0 = int(m.group(1))
    tz = timezone(timedelta(hours=tz0))
    utc_dt = cday.replace(tzinfo = tz)
    return utc_dt.timestamp()
    
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')