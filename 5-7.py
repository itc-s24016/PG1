prefecture_of_japan = {1:"Hokkaido", 2:"Aomori", 3:"Iwate"}

print(prefecture_of_japan[1])#キーが１の要素

print(prefecture_of_japan.get(0))#キーが０の要素
print(prefecture_of_japan.get(1))#キーが１の要素
print(prefecture_of_japan.get(0, "Not Found"))#キーの値が存在しなかったときの文章を変更

prefecture_of_japan[4] = "Miyagi"#キーが４で要素が"Miyagi"を追加
print(prefecture_of_japan)

print(1 in prefecture_of_japan)#キーが１の要素はprefecture_of_japanにあるか

del prefecture_of_japan[4]#キーが４の要素を消す
print(prefecture_of_japan)

print(prefecture_of_japan.pop(3))#キーが３の要素を取り出す
print(prefecture_of_japan)

for i in prefecture_of_japan.keys():#キーのみ表示
    print(i)
    
for i in prefecture_of_japan.values():#バリューのみ表示
    print(i)

for i in prefecture_of_japan.items():#キー&バリューを表示
    print(i)

