import random
punkty = []
y = 0
for i in range(15):
    punkty.append(round(random.uniform(0, 50), 2))

print(punkty)

print(f"Wartosc maksymalna wynosi: {max(punkty)}")
print(f"Wartosc minimalna wynosi: {min(punkty)}")

liczba = float(input("Podaj liczbe: "))
if y in punkty:
    print(punkty.index(liczba))
else:
    print("Brak wartosci.")
