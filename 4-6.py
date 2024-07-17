#１~１０の数字だけのリストを文字列のリストに変換
i_num_list = range(1,11)
s_num_list = list(map(lambda i: "No." + str(i), i_num_list))
print("文字列リスト:", s_num_list)

#数値を文字に変換して装飾
for s in map(lambda i: "No." + str(i), range(1,11)):
    print(s, end=" ")

#filter関数使用　偶数のみ取得
for e in filter(lambda i: i % 2 == 0, range(1,11)):
    print(e, end=" ")
