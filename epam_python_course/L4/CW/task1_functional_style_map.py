"""
У вас есть код в нефункциональном стиле. Перепишите его в функциональном стиле

names = ['Alexey', 'Ivan', 'Petr']

for i in range(len(names)):
    names[i] = hash(names[i])

print(names)

"""
names = ['Alexey', 'Ivan', 'Petr']

hash_names = []
for i in range(len(names)):
    hash_names.append(hash(names[i]))

print(hash_names)

assert hash_names == list(map(hash, names))
print(list(map(hash, names)))

assert hash_names == [hash(x) for x in names]
print([hash(x) for x in names])
