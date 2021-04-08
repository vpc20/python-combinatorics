from itertools import product


# def cartesian_product(arr, r):
#     for i, e in enumerate(arr):
#         if r == 0:
#             return
#         if r == 1:
#             yield (e,)
#         for p in cartesian_product(arr, r - 1):
#             yield (e,) + p


# def cartesian_product(arr, r):
#     if r == 1:
#         for e in arr:
#             yield (e,)
#         return
#     for i, e in enumerate(arr):
#         for p in cartesian_product(arr, r - 1):
#             yield (e,) + p


def cartesian_product(arr, r):
    if r == 0:
        yield tuple()
        return
    for i, e in enumerate(arr):
        for p in cartesian_product(arr, r - 1):
            yield (e,) + p


def cartesian_product_iter(arr, r):
    dp_arr = [[[()]] + [[] for _ in range(r)] for _ in range(len(arr) + 1)]
    # for e in dp_arr:
    #     print(e)
    for i in range(1, len(arr) + 1):
        for j in range(1, r + 1):
            if j <= i:
                for k in range(i):
                    for tup in dp_arr[i][j - 1]:
                        # if not tup:
                        #     dp_arr[i][j].append((arr[k],))
                        # else:
                        #     dp_arr[i][j].append((arr[k],) + tup)
                        dp_arr[i][j].append((arr[k],) + tup)
    # print(dp_arr)
    # for e in dp_arr:
    #     print(e)
    return dp_arr[-1][-1]


if __name__ == '__main__':
    print(list([''.join(comb) for comb in cartesian_product('abcd', 1)]))
    print(list([''.join(comb) for comb in cartesian_product('abcd', 2)]))
    print(list([''.join(comb) for comb in cartesian_product('abcd', 3)]))
    print(list([''.join(comb) for comb in cartesian_product('abcd', 4)]))
    print(list([''.join(comb) for comb in cartesian_product_iter('abcd', 2)]))
    # print([comb for comb in cartesian_product('abcd', 2)])
