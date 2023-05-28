sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"
}

# for key in sample_dict:
#   print(f'{key:<10} = {sample_dict[key]:>10}')

# for k,v in sample_dict.items():
#  print(f'{k:<10} = {v:>10}')

  # L = ['age', 'name']
  # D = {}
  # for k in L:
  #     if k in sample_dict.keys():
  #         D[k] = sample_dict[k]
  #     print(D)
L=['age','name']
# D={}
# for k in L:
#  if k in sample_dict.keys():
#   D[k]=sample_dict[k]
D = {k: sample_dict[k] for k in L if k in sample_dict.keys()}
print(D)

if "jones" in sample_dict.values():
    print("Wartość Jones wystepuje")
else:
    print("Nie wystepuje")

