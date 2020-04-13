from itertools import permutations


# for strings only
# def permutation(s, r):
#     for i in range(len(s)):
#         if r == 1:
#             yield s[i]
#         for p in permutation(s[:i] + s[i + 1:], r - 1):
#             yield s[i] + p


# for arrays and strings, output is tuple, recursive
# def permutation_recur(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield (arr[i],)
#         for p in permutation_recur(arr[:i] + arr[i + 1:], r - 1):
#             yield (arr[i],) + p


# for arrays and strings, output is tuple, recursive
# def permutation_recur(arr, r):
#     for i, e in enumerate(arr):
#         if r == 1:
#             yield (e,)
#         for p in permutation_recur(arr[:i] + arr[i + 1:], r - 1):
#             yield (e,) + p


def permutation_recur(arr, r):
    if r == 1:
        for e in arr:
            yield e,  # yield a tuple
        return
    for i, e in enumerate(arr):
        for p in permutation_recur(arr[:i] + arr[i + 1:], r - 1):
            yield (e,) + p


def permutation_backtrack(arr, r, perm=[]):
    if len(perm) == r:
        yield perm

    for e in arr:
        if e not in perm:
            perm.append(e)
            yield from permutation_backtrack(arr, r, perm)
            perm.pop()


# for strings only
# def permutation(s, r):
#     dp_arr = [[['']] + [[] for _ in range(r)] for _ in range(len(s) + 1)]
#     # for e in arr:
#     #     print(e)
#
#     for i in range(1, len(s) + 1):
#         for j in range(1, r + 1):
#             if j <= i:
#                 # new_comb = [s1 + s[i - 1] for s1 in dp_arr[i - 1][j - 1]]
#                 new_perm = []
#                 for s1 in dp_arr[i - 1][j - 1]:
#                     for k in range(len(s1), -1, -1):
#                         new_perm.append(s1[:k] + s[i - 1] + s1[k:]) # insert char in all positions
#                 dp_arr[i][j] = dp_arr[i - 1][j] + new_perm
#     for e in dp_arr:
#         print(e)
#     return dp_arr[-1][-1]


# for arrays and strings, output is tuple, iterative, dynamic
def permutation_iter(arr, r):
    dp_arr = [[[()]] + [[] for _ in range(r)] for _ in range(len(arr) + 1)]
    # for e in arr:
    #     print(e)

    for i in range(1, len(arr) + 1):
        for j in range(1, r + 1):
            if j <= i:
                new_perm = []
                for tup1 in dp_arr[i - 1][j - 1]:
                    for k in range(len(tup1), -1, -1):
                        new_perm.append(tup1[:k] + tuple([arr[i - 1]]) + tup1[k:])  # insert char in all positions
                dp_arr[i][j] = dp_arr[i - 1][j] + new_perm
    # for e in dp_arr:
    #     print(e)
    # print(dp_arr)
    return dp_arr[-1][-1]


if __name__ == '__main__':
    # print([e for e in permutations('abc', 3)])
    # print([e for e in permutation_recur('abc', 3)])
    # print([''.join(e) for e in permutation_recur('abc', 2)])
    print([''.join(e) for e in permutation_recur('abc', 2)])
