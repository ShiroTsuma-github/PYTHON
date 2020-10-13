from itertools import product, permutations

letters = ('A','B')
#print(list(product(letters, range(2))))
print(list(permutations(letters)))
print(list(product(letters, range(2))))