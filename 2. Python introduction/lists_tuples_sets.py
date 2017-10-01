################3
# lists
lista = [88, 99, 77, 66]
print(sum(lista) / len(lista))
# add items
lista.append(88)
print(lista[1])
lista[1] = 11
print(lista[1])

#################
# tuples
# imutable
tuple1 = (88, 99, 77, 66)
# create a new tuple
# !!!! la virgula
print(tuple1)
tuple1 = tuple1 + (100,)
print(tuple1)


####################
# sets
# unique & unordered
set1 = { 88, 99, 77, 66}
set1.add(34)
print(set1)
setOne = {1, 2, 3, 4, 5}
setTwo = {4, 5, 6, 7}
print(setOne.intersection(setTwo)) # produces a new set
print(setOne.union(setTwo)) 
print(setOne.difference(setTwo))