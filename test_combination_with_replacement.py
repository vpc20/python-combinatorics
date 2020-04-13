from unittest import TestCase
from itertools import combinations_with_replacement

from CombinationWithReplacement import combination_with_replacement, combination_with_replacement_iter


class TestCombinationWithReplacement(TestCase):
    def test_combination_with_replacement(self):
        slist = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']
        for s in slist:
            for r in range(1, len(s) + 1):
                print(s, r)
                self.assertEqual(list(comb for comb in combinations_with_replacement(s, r)),
                                 list(comb for comb in combination_with_replacement(s, r)))

    def test_combination_with_replacement_iter(self):
        slist = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']
        for s in slist:
            for r in range(1, len(s) + 1):
                print(s, r)
                self.assertEqual(list(comb for comb in combinations_with_replacement(s, r)),
                                 list(comb for comb in combination_with_replacement_iter(s, r)))
