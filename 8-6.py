#現在の年月日
from datetime import date
day_now = date.today()
print(day_now)

#適当な年月日と今日の差分
xday = date(2005, 7, 9)
td = day_now - xday
print(td)


