# Zmodyfikuj program z zad. 1 tak, aby przechodząc po kolejnych liczbach przedziału, wypisywać
# tylko liczby parzyste, a nieparzyste – pomijać. Użyj instrukcji continue.

a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))

if b < a:
    a,b = b,a

while a <= b:
    if a%2 == 1:
        a = a + 1
        continue

    print(a,end=' ')
    a = a + 1
