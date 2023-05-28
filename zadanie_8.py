# Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy
# liczbę punktów dla każdego studenta. Napisz program, który obliczy średnią liczbę punktów w grupie z
# wykorzystaniem pętli while

n = int(input("Podaj ilosc studentow "))
current_student = 1
sum_of_scores = 0

while True:
    score = int(input(f"Podaj ilosc punktów studenta numer {current_student} "))
    if (score <0  or score > 100):
        continue
    sum_of_scores += score
    current_student += 1
    if current_student > n:
        break

average = sum_of_scores / n
print(f"Srednia puntkow wynosi {average}.")
