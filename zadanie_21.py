def potega(lista1, lista2):
    lista3 = []
    if len(lista1) != len(lista2):
        print("Różna długość list")
        return lista3
    for i in range(len(lista1)):
        lista3.append(lista1[i]**lista2[i])
    return lista3

lista1 = [2,3,1,5,8]
lista2 = [2,2,0,1]

print(potega(lista1,lista2))
