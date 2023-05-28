values = [10, 20, 33]
keys = ["Ten", "Twenty", "Thirty"]
D = {}
#print(list(zip(keys, values)))
#D=dict(zip(keys, values))
for i in range(len(values)):
    D[keys[i]] = values[i]

print(D)
A = dict(Thirty = 30, Forthy = 40, Fifthy = 50)
print(A)

#D.update(A)
D3 = D.copy()
D3.update(A)

print(D3)

