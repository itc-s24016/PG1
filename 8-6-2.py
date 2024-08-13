#1日時間を進める
import datetime
t_delta = datetime.timedelta(days = 1)
dt = datetime.datetime.strptime("13/08/24", "%d/%m/%y")
print(dt + t_delta)

