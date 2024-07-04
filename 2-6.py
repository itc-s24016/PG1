#formatを使用した文
a= "abc"
b= "xyz"
print("{}{}".format(a,b))

title= "name"
value= "Aimi Sunagawa"
print("Your {} is {}.".format(title,value))

age= "18"
print("Your age is {}.".format(age))

title= "IQ"
value= 100
print("{}={}".format(title,value))

#フォーマット済み文字列リテラル
a,b= "Hello", "World"
print(f"{a} {b}")

a,b= "Hello", "World"
print("{} {}".format(a,b))
