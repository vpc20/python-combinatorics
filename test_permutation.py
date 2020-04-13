from unittest import TestCase
from itertools import permutations
from Permutation import permutation_iter, permutation_recur


class TestPermutationWithLength(TestCase):
    def test_permutation_recur(self):
        slist = ['a', 'ab', 'abc', 'abcd', 'abcde',
                 'abcdef', 'abcdefg', 'abcdefgh']
        for s in slist:
            for r in range(1, len(s) + 1):
                print(s, r)
                self.assertEqual(list(permutations(s, r)), sorted(list(permutation_recur(s, r))))

    def test_permutation_iter(self):
        slist = ['a', 'ab', 'abc', 'abcd', 'abcde',
                 'abcdef', 'abcdefg', 'abcdefgh']
        for s in slist:
            for r in range(1, len(s) + 1):
                print(s, r)
                self.assertEqual(list(permutations(s, r)), sorted(list(permutation_iter(s, r))))
