from datetime import time, timedelta
h, m = map(int, input().split(' '))
# 1. datetime module.
t_before = time(hour=h, minute=m)
if t_before.minute < 45:
    hour = t_before.hour - 1 if t_before.hour > 0 else 23
    minute = t_before.minute + 15
    t_after = t_before.replace(hour, minute)
else:
    t_after = t_before.replace(minute=t_before.minute - 45)
print(t_after.hour, t_after.minute)


