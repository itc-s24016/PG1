import collections

#普通に書いた
data = "すもももももももものうち"
count_dic = {}
for v in data:
    if v in count_dic:
        count_dic[v] += 1
    else:
        count_dic[v] = 1
print(count_dic)

#collectionsモジュール入り(defaultdict())
count_dic = collections.defaultdict(int)
for v in data:
    count_dic[v] += 1
print(count_dic)


#リスト型にしてみた
count_dic = collections.defaultdict(list)
for v in data:
    count_dic[v].append(v)
print(count_dic)


#defaultdict()よりも短縮できるCounter()
counter = collections.Counter(data)
print(counter)


#要素の数を出力する
print(counter["す"])
print(counter["ぽ"])

#namedtapleを使用してタプルの各要素に名前をつけてみる
CharCount = collections.namedtuple("CharCount", ["char", "count"])
mo = CharCount("も", 8)
print(mo)





count = collections.Counter(data)
res_dict = collections.defaultdict(list)
for ch, cnt in count.items():
    res_dict[cnt].append(ch)
print(res_dict[1])

'''より短くしたもの
import collections
data = "すもももももももものうち"
count = collentions.Counter(data)
[v[0] for v in count.items() if v[1] == 1]
'''

