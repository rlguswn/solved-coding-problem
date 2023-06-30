import sys
import datetime

x, y = map(int, sys.stdin.readline().split())
d = datetime.date(2007, x, y)
w = d.weekday()
week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
print(week[w])