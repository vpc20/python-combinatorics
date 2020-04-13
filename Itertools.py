from itertools import permutations, combinations, combinations_with_replacement, product

print(list([''.join(comb) for comb in permutations('abc', 2)]))
print(list([''.join(comb) for comb in combinations('abc', 2)]))
print(list([''.join(comb) for comb in combinations_with_replacement('abc', 2)]))
print(list([''.join(prod) for prod in product('abc', repeat=2)]))
