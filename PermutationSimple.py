import unittest
from random import randrange, choice
from string import ascii_lowercase
from itertools import permutations, combinations


# def permutation(s, p=''):
#     if len(s) == 0:
#         yield p
#     else:
#         for i in range(len(s)):
#             yield from permutation(s[:i] + s[i + 1:], p + s[i])


# def permutation(head, tail=''):
#     if len(head) == 0:
#         print tail
#     else:
#         for i in range(len(head)):
#             permutation(head[0:i] + head[i + 1:], tail + head[i])

# def permutation(s):
#     if len(s) <= 1:
#         yield s
#     else:
#         for i in range(len(s)):
#             for p in permutation(s[:i] + s[i + 1:]):
#                 yield s[i] + p


def permutation(arr):
    if len(arr) <= 1:
        yield tuple(arr)
    else:
        for i in range(len(arr)):
            for p in permutation(arr[:i] + arr[i + 1:]):
                yield tuple([arr[i]]) + p


# def permutation(s):
#     if len(s) <= 1:
#         yield s
#     else:
#         for perm in permutation(s[1:]):
#             for i in range(len(s)):
#                 yield (perm[:i] + s[0] + perm[i:])  # nb elements[0:1] works in both string and list contexts


# def permutation(a, k=0):
#     if k == len(a):
#         print a
#     else:
#         for i in xrange(k, len(a)):
#             a[k], a[i] = a[i], a[k]
#             permutation(a, k + 1)
#             a[k], a[i] = a[i], a[k]

# def permutation(s, chridx=0):
#     output = ''
#     if chridx == len(s):
#         return ''
#     else:
#         for i in range(len(s)):
#             output += s[:i] + s[chridx] + s[i + 1:]
#             permutation(s, chridx + 1)
#     return output

# def permutation(s):
#     if len(s) < 2:
#         yield s
#     else:
#         for i in range(len(s)):
#             for p in permutation(s[:i] + s[i + 1:]):
#                 yield s[i] + p

# permutation using rotation - version 1
# def permutation(suff, pref=''):
#     if len(suff) == 1:
#         yield pref + suff
#     for i in range(len(suff)):
#         rotated_suff = suff[i:] + suff[:i]  # rotate suffix left
#         yield from permutation(rotated_suff[1:], pref + rotated_suff[0])

# permutation using rotation - version 2
# def permutation(s):
#     def _permutation(pref, suff):
#
#         if len(suff) == 1:
#             yield pref + suff
#         for i in range(len(suff)):
#             rotated_suff = suff[i:] + suff[:i]  # rotate left
#             yield from _permutation(pref + rotated_suff[0], rotated_suff[1:])
#
#     yield from _permutation('', s)


# def swap_char(s, i, j):
#     return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:] if i != j else s
#
# def _permutation(pref, suff):
#     if len(suff) == 1:
#         yield pref + suff
#     for i in range(len(suff)):
#         swapped_suff = swap_char(suff, 0, i)
#         yield from _permutation(pref + swapped_suff[0], swapped_suff[1:])

# def permutation(arr):
#     if len(arr) == 1:
#         yield arr
#     for i in range(len(arr)):
#         for p in permutation(arr[:i] + arr[i + 1:]):
#             yield [arr[i]] + p
#
#
# for p1 in permutation([1, 2, 3]):
#     print(p1)

# def permutation(arr):
#     yield from _permutation([], arr)
#
#
# def _permutation(initial, tail):
#     if len(tail) == 1:
#         yield initial + tail
#     for i in range(len(tail)):
#         rotated_tail = tail[i:] + tail[:i]  # rotate left
#         yield from _permutation(initial + [rotated_tail[0]], rotated_tail[1:])
#
#
# for p in permutation([1, 2, 3]):
#     print(p)


# def permutation(arr, r):
#     yield from _permutation([], arr, r)
#
#
# def _permutation(initial, tail, r):
#     if r == 0:
#         yield initial  # + tail
#     for i in range(len(tail)):
#         rotated_tail = tail[i:] + tail[:i]  # rotate array left
#         yield from _permutation(initial + [rotated_tail[0]], rotated_tail[1:], r - 1)


# def random_string(maxlen):
#     return ''.join([choice(ascii_lowercase) for _ in range(randrange(1, maxlen + 1))])
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, True)
#
#         for _ in range(1000):
#             s = random_string(6)
#
#             p1 = [perms for perms in permutation(s)]
#             p1.sort()
#             print(p1)
#
#             p2 = [''.join(p) for p in permutations(s)]
#             p2.sort()
#             print(p2)
#
#             self.assertEqual(p1, p2)
#
#
# if __name__ == '__main__':
#     unittest.main()

# for e in permutation('abc'):
#     print(e)

for e in permutation('ab'):
    print(e)

# for e in permutation([1, 2, 3]):
#     print(e)

# from itertools import combinations, permutations, product
#
# for e in permutations('abc'):
#     print ''.join(e)

# for e in insert_all_positions('abc'):
#     print e

# print rotate_string('a', 0)
