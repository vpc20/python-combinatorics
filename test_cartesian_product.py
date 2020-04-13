from itertools import product
from unittest import TestCase

from CartesianProduct import cartesian_product, cartesian_product_iter


class TestCartesianProduct(TestCase):
    def test_cartesian_product(self):
        slist = ['a', 'ab', 'abc', 'abcd', 'abcde',
                 'abcdef', 'abcdefg']
        for s in slist:
            for r in range(1, len(s) + 1):
                print(s, r)
                self.assertEqual(list(product(s, repeat=r)), list(cartesian_product(s, r)))

    def test_cartesian_product_iter(self):
        slist = ['a', 'ab', 'abc', 'abcd', 'abcde',
                 'abcdef', 'abcdefg']
        for s in slist:
            for r in range(1, len(s) + 1):
                print(s, r)
                self.assertEqual(list(product(s, repeat=r)), list(cartesian_product_iter(s, r)))
