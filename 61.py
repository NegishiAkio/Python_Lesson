import this
print(61)

#--------------様々な関数------------------
alphabet = "abcdefghijklmnopqrstuvwxyz"
#文字数を返す
len2 = len(alphabet)
print(len2)
#print(len(alphabet))
#戦闘だけ大文字にする
print(alphabet.capitalize())
#すべての文字列を大文字にする
print(alphabet.upper())
#リストの削除
list_one =["akio","TK"]
print(list_one[1])
#print(list_one.remove("akio"))

#tple_one = ("chees","kore","oo")

#----------タプル-----------
marx_tple = ("akio","miyuki","kayo")
a,b,c = marx_tple
print(a)
#---------------------------

accusatuon = {"room":"bassroom","weapon":"leadpipe","person":"Mustard"}
accusatuon2 = ["1T2","1T3","1T4",]

#----------値の取り出し-----------
for card3 in accusatuon.values():
    print(card3)
#---------keyの取り出し----------
for card in accusatuon.keys():
    print(card)
#---------リストの取り出し--------
for card2 in accusatuon2:
    print(card2)
#--------keyと値の両方を取り出す---
for item in accusatuon.items():
    print(item)
#--------条件比較----------
python_lesson = True
if python_lesson:
    print("ok")
else:
    print("no")
#--------------------------

#---------forでの値の取り出し---------

hairetu ={"phone":"5s","tablet":"pad"}

for hairetu2 in hairetu.items():
    print(hairetu2)

for k in range(0,3):
    print(k)

#-------内包表記---------
number_list = [number for number in range(1,6)]
print(number_list)
number_month = []
for number in range(1,6):
    number_month.append(number)

cheeses = ["WW"]
for cheese in cheeses:
    print(cheese)
    break
else:
    print("this is not")

def akio(a,b):
    return a + b

d = akio(12,18)
print(d)

years_list = ["1980","1981","1982","1983","1984","1985"]

print(years_list[2])
print(years_list[5])

things = ["mozzarella","cinderella","salmonella"]

class Myclass():
    def calc(self,x,y):
        self.z = x * y

        def main():
            my = Myclass()

            my.calc(11,20)

            print(my.z)

if __name__ == "__main__":
            main()
