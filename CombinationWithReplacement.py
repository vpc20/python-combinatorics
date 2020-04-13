def combination_with_replacement(arr, r):
    if r == 1:
        for e in arr:
            yield (e,)
        return
    for i, e in enumerate(arr):
        for c in combination_with_replacement(arr[i:], r - 1):
            yield (e,) + c


# def combination_with_replacement(arr, r):
#     for i, e in enumerate(arr):
#         if r == 0:
#             return
#         if r == 1:
#             yield (e,)
#         for c in combination_with_replacement(arr[i:], r - 1):
#             yield (e,) + c


def combination_with_replacement_iter(arr, r):
    dp_arr = [[[()]] + [[] for _ in range(r)] for _ in range(len(arr) + 1)]
    # for e in dp_arr:
    #     print(e)
    for i in range(1, len(arr) + 1):
        for j in range(1, r + 1):
            if j <= i:
                for k in range(i):
                    for tup in dp_arr[i][j - 1]:
                        if not tup:
                            dp_arr[i][j].append((arr[k],))
                        elif (arr[k],) <= tup:
                            dp_arr[i][j].append((arr[k],) + tup)
    # print(dp_arr)
    # for e in dp_arr:
    #     print(e)
    return dp_arr[-1][-1]


# def combination_with_replacement_iter(arr, r):
#     dp_arr = [[[()]] + [[] for _ in range(r)] for _ in range(len(arr) + 1)]
#     # for e in dp_arr:
#     #     print(e)
#     for i in range(1, len(arr) + 1):
#         for j in range(1, r + 1):
#             if j <= i:
#                 for k in range(i):
#                     for l in range(k+x , len(dp_arr[i-1][j - 1])+1):
#                         if dp_arr[i][j - 1] == [()]:
#                             dp_arr[i][j].append((arr[k],))
#                         else:
#                             dp_arr[i][j].append((arr[k],) + dp_arr[i][j - 1][l])
#     # print(dp_arr)
#     # for e in dp_arr:
#     #     print(e)
#     return dp_arr[-1][-1]


if __name__ == '__main__':
    # for comb in combination_with_replacement('abcd', 2):
    #     print(''.join(comb))
    # for comb in combination_with_replacement('abc', 2):
    #     print(''.join(comb))
    for comb in combination_with_replacement('ab', 1):
        print(''.join(comb))
    # for comb in combination_with_replacement_iter('a', 1):
    #     print(''.join(comb))
