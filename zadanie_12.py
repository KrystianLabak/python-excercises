import random

list_1 = []
x = int(input("Enter len list"))
for i in range(x):
    list_1.append(random.randint(1,10))

print(list_1)

x = int(input("Enter len list"))

list_2 = []

for i in range(x):
    list_2.append(random.randint(5,15))

print(list_2)


y = int(input("Enter number: "))

if y in list_1:
    print("Number of fisrt list")
elif y in list_2:
    print("Number of second list")
else: print("Number not exist in both lists")

list_1_2 = list_1 + list_2
print(list_1_2)

list_1_2.sort()
print(list_1_2)