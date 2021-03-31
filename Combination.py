# for strings only
# def combination(s, r):
#     for i in range(len(s)):
#         if r == 1:
#             yield s[i]
#         for c in combination(s[i + 1:], r - 1):
#             yield s[i] + c


# for arrays and strings, output is tuple
# def combination(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield (arr[i],)
#         for c in combination(arr[i + 1:], r - 1):
#             yield (arr[i],) + c


# def combination(arr, r):
#     if r == 1:
#         for e in arr:
#             yield (e,)
#         return
#     for i in range(len(arr) - 1):
#         for c in combination(arr[i + 1:], r - 1):
#             yield (arr[i],) + c


def combination(arr, r):
    if r == 0:
        yield tuple()
        return
    for i in range(len(arr)):
        for c in combination(arr[i + 1:], r - 1):
            yield tuple(arr[i]) + c


# use backtracking method
# def combination(arr, r, comb=[]):
#     if r == 0:
#         yield tuple(comb[:])
#     else:
#         for i in range(len(arr)):
#             comb.append(arr[i])
#             yield from combination(arr[i + 1:], r - 1, comb)
#             comb.pop()

# use backtracking method, return list instead of generator
# def combination(arr, k):
#     def combine(arr, k, comb):
#         if k == 0:
#             result.append(comb[:])
#         else:
#             for i in range(len(arr)):
#                 comb.append(arr[i])
#                 combine(arr[i + 1:], k - 1, comb)
#                 comb.pop()
#
#     result = []
#     combine(arr, k, [])
#     return result


# def combination(arr, r):
#     if r == 0:
#         return [()]
#     if not arr or r > len(arr):
#         return []
#     if r <= len(arr):
#         new_comb = [tup1 + (arr[-1],) for tup1 in combination(arr[:-1], r - 1)]
#         return combination(arr[:-1], r) + new_comb


# def combination(arr, r):
#     for i, e in enumerate(arr):
#         if r == 1:
#             yield (e,)
#         for c in combination(arr[i + 1:], r - 1):
#             yield (e,) + c


# def combination(s, r):
#     dp_arr = [[['']] + [[] for _ in range(r)] for _ in range(len(s) + 1)]
#     # for e in dp_arr:
#     #     print(e)
#
#     for i in range(1, len(s) + 1):
#         for j in range(1, r + 1):
#             if j <= i:
#                 new_comb = [s1 + s[i - 1] for s1 in dp_arr[i - 1][j - 1]]
#                 dp_arr[i][j] = dp_arr[i - 1][j] + new_comb
#     # for e in dp_arr:
#     #     print(e)
#     return dp_arr[-1][-1]

# for arrays and strings, output is tuple, dynamic
def combination_iter(arr, r):
    dp_arr = [[[()]] + [[] for _ in range(r)] for _ in range(len(arr) + 1)]
    for e in dp_arr:
        print(e)
    for i in range(1, len(arr) + 1):
        for j in range(1, r + 1):
            if j <= i:
                new_comb = [tup1 + (arr[i - 1],) for tup1 in dp_arr[i - 1][j - 1]]
                dp_arr[i][j] = dp_arr[i - 1][j] + new_comb
    # for e in dp_arr:
    #     print(e)
    # print(dp_arr)
    return dp_arr[-1][-1]


# def combination(alist, n):
#     # print(alist)
#     if len(alist) <= n:
#         yield alist
#         # alist = []
#     else:
#         if alist:
#             head = alist[0]
#             tail = alist[1:]
#             for c in combination(tail, n - 1):
#                 yield [head] + c
#             for c in combination(tail, n):
#                 yield c

if __name__ == '__main__':
    # arr = [0, 1, 2, 3, 4, 5]
    # for comb in combination(arr, 3):
    #     print(comb)
    # pass

    # for comb in combination('abc', 2):
    #     print(comb)
    # for comb in combination('abcde', 3):
    #     print(comb)

    # for comb in combination('abcd', 2):
    #     print(comb)
    #       0               1                           2                                          3
    #    ┌──────┬──────────────────────┬──────────────────────────────────────┬──────────────────────────────────────┐
    # '' │ [''] │                   [] │                                   [] │                                   [] │
    #    ├──────┼──────────────────────┼──────────────────────────────────────┼──────────────────────────────────────┤
    # a  │ [''] │                ['a'] │                                   [] │                                   [] │
    #    ├──────┼──────────────────────┼──────────────────────────────────────┼──────────────────────────────────────┤
    # b  │ [''] │           ['a', 'b'] │                               ['ab'] │                                   [] │
    #    ├──────┼──────────────────────┼──────────────────────────────────────┼──────────────────────────────────────┤
    # c  │ [''] │      ['a', 'b', 'c'] │                   ['ab', 'ac', 'bc'] │                              ['abc'] │
    #    ├──────┼──────────────────────┼──────────────────────────────────────┼──────────────────────────────────────┤
    # d  │ [''] │ ['a', 'b', 'c', 'd'] │ ['ab', 'ac', 'bc', 'ad', 'bd', 'cd'] │         ['abc', 'abd', 'acd', 'bcd'] │
    #    └──────┴──────────────────────┴──────────────────────────────────────┴──────────────────────────────────────┘

    # for comb in combination('abcd', 2):
    #     print(''.join(comb))
    for comb in combination('abcd', 2):
        print(''.join(comb))
    for comb in combination_iter('abcd', 2):
        print(''.join(comb))
    # for comb in combination_iter('abcd', 3):
    #     print(''.join(comb))
    # for comb in combination([1, 2, 3], 2):
    #     print(comb)
    for comb in combination('a', 1):
        print(''.join(comb))
