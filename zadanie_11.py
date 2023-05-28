import random

zestaw_1 = []

generowane_liczby = int(input("Podaj liczbe "))

for y in range(generowane_liczby):
    x = random.randint(1, 10)
    zestaw_1.append(x)
print(zestaw_1)

generowane_liczby_2 = int(input("Podaj liczbe 2 "))
zestaw_2 = [random.randint(5, 15) for y in range(generowane_liczby_2)]
print(zestaw_2)

