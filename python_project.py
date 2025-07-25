"""1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]"""

lst = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l=[]
def flatten(lst):
    for i in lst:
        if isinstance(i, list):
            flatten(i)
        else:
            l.append(i)
    return l

print(flatten(lst))

"""2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]"""

lst2 = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(lst2):
    for i in lst2:
        i.reverse()
    lst2.reverse()
    return lst2
reverse(lst2)
print(lst2)

