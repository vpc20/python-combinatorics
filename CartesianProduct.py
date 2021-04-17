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
    for e in arr:
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


def cartesian_product2(arrs):
    if not arrs:
        yield tuple()
        return

    for e in arrs[0]:
        for p in cartesian_product2(arrs[1:]):
            yield (e,) + p


# def cartesian_product2x(arrs):
#     result = [()]
#     for arr in arrs:
#         n = len(result)
#         for e in result.copy():
#             for item in arr:
#                 result.append(e + (item,))
#         result = result[n:]  # remove all previous values
#     return result

# iterative, dp solution
def cartesian_product2_iter(arrs):
    prev = [()]
    result = []
    for arr in arrs:
        result.clear()
        for e in prev:
            for item in arr:
                result.append(e + (item,))
        prev = result.copy()
    return result


if __name__ == '__main__':
    print([''.join(prod) for prod in cartesian_product('abcd', 1)])
    print([''.join(prod) for prod in cartesian_product('abcd', 2)])
    print([''.join(prod) for prod in cartesian_product('abcd', 3)])
    print([''.join(prod) for prod in cartesian_product('abcd', 4)])
    print([''.join(prod) for prod in cartesian_product_iter('abcd', 2)])
    # print([prod for prod in cartesian_product('abcd', 2)])
    # print([''.join(prod) for prod in cartesian_product2(['abc', 'def'])])
    # print([''.join(prod) for prod in cartesian_product2([[]])])
    # print([''.join(prod) for prod in cartesian_product2([[], []])])
    # print([''.join(prod) for prod in cartesian_product2([[], [], []])])
    # print([''.join(prod) for prod in cartesian_product2([[], [5], []])])
    # print([''.join(prod) for prod in cartesian_product2x(['abc', 'def'])])
    print(cartesian_product2_iter([[1, 2, 3], [4, 5, 6]]))
    print(cartesian_product2_iter(['abc', 'def']))
    print(cartesian_product2_iter([[1, 2], [3, 4], [5, 6]]))
