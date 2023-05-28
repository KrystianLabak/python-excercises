# Napisz skrypt działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć,
# dzielić oraz obliczać potęgę.
# Przykład: Jaką operację chcesz wykonać?
# 1) dodawanie
# 2) odejmowanie
# 3) mnożenie
# 4) dzielenie
# 5) potęgowanie
# Wpisz numer operacji: 2
# Podaj argument 1: 34
# Podaj argument 2: 5
# Wynik: 29
print("""Jaka operacje chcesz wykonac?
      1) Dodawanie
      2) Odejmowanie
      3) Mnozenie
      4) Dzielenie
      5) Potegowanie""")
x = int(input("Wybierz operacje "))
arg1 = int(input("Podaj argument 1 "))
arg2 = int(input("Podaj argument 2 "))

if x == 1:
    print("Wynik wynosi ", arg1 + arg2 )
elif x == 2:
    print("Wynik wynosi ", arg1 - arg2)
elif x == 3:
    print("Wynik wynosi ", arg1 * arg2)

elif x == 4:
    if arg2 == 0:
        print("Nie dzieli sie przez 0")
        exit()
    print("Wynik wynosi ", arg1 / arg2)

elif x == 5:
    print("Wynik wynosi ", arg1 ** arg2)
else:
    print("Niepoprawny numer operacji")


