from itertools import product
from random import randrange
from unittest import TestCase

from CartesianProduct import cartesian_product, cartesian_product_iter, cartesian_product2
from RandomData import random_int_array


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

    def test_cartesian_product2(self):
        for _ in range(1000):
            arrs = [random_int_array(5, 100) for _ in range(randrange(2, 6))]
            print(arrs)
            # print(list(product(*arrs)))
            # print(list(cartesian_product2(arrs)))
            self.assertEqual(list(product(*arrs)), list(cartesian_product2(arrs)))
