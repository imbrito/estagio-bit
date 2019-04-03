#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

class BuiltInFunctionsSpec(unittest.TestCase):

    def test_it_instance_of(self):
        self.assertTrue(isinstance(None, type(None)))
        self.assertTrue(isinstance(False, bool))
        self.assertTrue(isinstance('1',str))
        self.assertTrue(isinstance(1,int))
        self.assertTrue(isinstance(1.0,float))
        self.assertTrue(isinstance({1:1},dict))
        self.assertTrue(isinstance((1,),tuple))
        self.assertTrue(isinstance([1],list))
        self.assertTrue(isinstance({1},set))

    def test_it_generator_range(self):
        self.assertEqual([0,1,2,3,4], list(range(5)))

    def test_it_max_value(self):
        self.assertEqual(9, max(range(10)))
        self.assertEqual(4, max([0,1,2,3,4]))

    def test_it_min_value(self):
        self.assertEqual(0, min(range(10)))
        self.assertEqual(5, min([5,6,7,8,9]))

    def test_it_sum_values(self):
        self.assertEqual(45, sum(range(10)))

    def test_it_quantity_elements(self):
        self.assertEqual(5, len(range(5)))
        self.assertEqual(5, len([0,1,2,3,4]))
        self.assertEqual(5, len('learn'))
        self.assertEqual(5, len(('a','e','i','o','u')))

    def test_it_included(self):
        self.assertFalse(5 in [0,1,2,3,4])
        self.assertTrue(2 in [0,1,2,3,4])
        self.assertFalse('a' in 'python')
        self.assertTrue('e' in ('a','e','i','o','u'))

    def test_it_boolean_operations(self):
        self.assertTrue(1 and 1)
        self.assertFalse(1 and 0)
        self.assertTrue(1 or 0)
        self.assertFalse(0 or 0)
        self.assertTrue(not 0)
        self.assertFalse(not 1)

    def test_it_comparations(self):
        self.assertTrue(1 == 1)
        self.assertFalse(1 != 1)
        self.assertTrue(1 >= 1)
        self.assertFalse(0 >= 1)
        self.assertTrue(0 <= 1)
        self.assertFalse(1 <= 0)
        self.assertTrue(0 < 1)
        self.assertFalse(1 < 0)
        self.assertTrue(0 > -1)
        self.assertFalse(0 < -1)
        self.assertTrue(1 is 1)
        self.assertFalse(0 is not 0)

    def test_it_numeric_operations(self):
        self.assertTrue(1 / 1)
        self.assertFalse(0 / 1)
        self.assertTrue(3 % 2)
        self.assertFalse(2 % 2)
        self.assertTrue(1 * 1)
        self.assertFalse(0 * 1)
        self.assertTrue(0 + 1)
        self.assertFalse(1 - 1)
        self.assertTrue(abs(-1))
        self.assertFalse(abs(0))
        self.assertEqual(pow(2, 2), 2 ** 2)