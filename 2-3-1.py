#10進数を扱うdecimalモジュールで少数型のデータからDecimal型のデータを作る
from decimal import Decimal
print(Decimal.from_float(0.5))
print(Decimal.from_float(0.1))
print(Decimal.from_float(0.3))
