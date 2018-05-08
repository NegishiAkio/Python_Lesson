#listに変換
list_1 = "list1","list2","list3"

print(list(list_1))

#offsetでlist取り出し

print(list_1[1])

#タプル作成
taple = ("taple1","taple2","taple3")
print(taple)


#辞書作成

pythons = {"python1":"辞書","python2": "辞書","python3": "辞書"}
print(pythons)

#keyだけを出力
for key in pythons.keys():
    print(key)

#値だけを出力
for value in pythons.values():
    print(value)

#辞書のkeyと値を出力
for python in pythons.items():
    print(python)
#辞書を削除
pythons.clear()
print(pythons)

#内包表記
number_list = [i for i in range(1,6)]
naihouhyouki = number_list
print(naihouhyouki)
