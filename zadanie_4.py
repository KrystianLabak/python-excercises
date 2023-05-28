# Napisz skrypt, który pobierze od użytkownika dwie liczby całkowite. Następnie zaczynając od
# mniejszej liczby, wypisze kolejne liczby aż do osiągnięcia wartości drugiej (większej) liczby.
# Np. Wejście: 10, 5
# Wyjście: 5, 6, 7, 8, 9, 10

a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))

if b < a:
    a,b = b,a

while b>=a:
    print(a,end=' ')
    a = a + 1
