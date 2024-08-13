#今日の年月日日時分秒ミリ秒まで取得&各属性を表示
from datetime import datetime
now = datetime.today()
print(now)#今日の年月日時分秒マイクロ秒
print(now.year)#年
print(now.month)#月
print(now.day)#日
print(now.hour)#時
print(now.minute)#分
print(now.second)#秒
print(now.microsecond)#マイクロ秒

#架空の時刻を生成
Happy_New_Year = datetime(2025, 1, 1, 0, 0, 0, 0)
print(Happy_New_Year)

#特定の時刻データを指定したフォーマットに変換
dt = datetime.strptime("13/08/2024 15:11", "%d/%m/%Y %H:%M")
print(dt)
