def find(lista, liczba):
    lista2 = []
    index = 0
    for amount in lista:
        if liczba == amount:
            lista2.append(index)
        index+=1
    return lista2

L1 = find([3,2,5,-2,4,10], 2)
print(L1)
