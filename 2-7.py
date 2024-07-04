my_list=[2,4,8,16]
print(my_list + [3,6,9,12])
print(my_list)

#（）内の要素をリストの末尾に追加
my_list.append(3)
my_list.append(6)
my_list.append(9)
print(my_list)

my_list.extend([12,15])#リストを連結
print(my_list)

my_list.sort()#リストをソート
print(my_list)

my_list.sort(reverse= True)#リストをソート＋降順
print(my_list)

my_list.reverse()#リストを降順へ
print(my_list)

new_list= sorted(my_list)#sortedでソート済みの新しいリストを作る
print(new_list)
