# Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała

litera = input("Podaj litere ")
if len(litera) > 1:
    print("Wprowadzono wiecej niz jedna litere")
    exit()

if len(litera) == 0:
    print("Nie wprowadzono liter")
    exit()

if 'a' <= litera <= 'z':
    print("Mała")
elif 'A' <= litera <= 'Z':
    print("Duża")
else:
    print("nie jest litera")