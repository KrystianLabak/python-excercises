def sum_of_values(dict1):
    suma=0
    x = dict1.values()
    for v in x:
        suma+=v
    return suma

wynik = sum_of_values({'data1':10, 'data2':-4, 'data3':2})
print(wynik)
