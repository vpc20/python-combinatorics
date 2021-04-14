from itertools import permutations, combinations, combinations_with_replacement, product

print([''.join(perm) for perm in permutations('abc', 2)])
print([''.join(comb) for comb in combinations('abc', 2)])
print([''.join(comb) for comb in combinations_with_replacement('abc', 2)])
print([''.join(prod) for prod in product('abc', repeat=2)])

print(tuple(''.join(perm) for perm in permutations('abc', 2)))
print(tuple(''.join(comb) for comb in combinations('abc', 2)))
print(tuple(''.join(comb) for comb in combinations_with_replacement('abc', 2)))
print(tuple(''.join(prod) for prod in product('abc', repeat=2)))

print(tuple(''.join(prod) for prod in product('abc', 'def')))
print(tuple(''.join(prod) for prod in product(*['abc', 'def'])))

# removing duplicate results if there are duplicate characters
pset = set()
for perm in permutations('aabc', 2):
    if perm not in pset:
        print(perm)
    pset.add(perm)
