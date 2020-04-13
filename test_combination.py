from itertools import combinations
from unittest import TestCase

from Combination import combination, combination_iter


class TestCombination(TestCase):
    def test_combination(self):
        slist = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']
        for s in slist:
            for r in range(1, len(s) + 1):
                print(s, r)
                self.assertEqual(list(comb for comb in combinations(s, r)),
                                 sorted(list(comb for comb in combination(s, r))))

    def test_combination_iter(self):
        slist = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']
        for s in slist:
            for r in range(1, len(s) + 1):
                print(s, r)
                self.assertEqual(list(comb for comb in combinations(s, r)),
                                 sorted(list(comb for comb in combination_iter(s, r))))
