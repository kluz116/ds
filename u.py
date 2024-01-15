lista = [3,4,6,8,9,1,23,12,32,15,37,54,37]
listb = [100,102,105,37]
lista.append(30)
lista.insert(2,2)
lista.extend(listb)
lista.sort()
listc = lista.copy()
listc.pop(4)
listc.clear()
print(lista.count(37))
print(lista)
print(listc)