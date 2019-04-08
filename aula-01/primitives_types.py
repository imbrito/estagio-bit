#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

class PrimitivesFunctionsSpec(unittest.TestCase):

    def test_primitives_types(self):
        self.assertEqual(bool, type(False))
        self.assertEqual(str, type('1'))
        self.assertEqual(int, type(1))
        self.assertEqual(float, type(1.0))
        self.assertEqual(dict, type({1:1}))
        self.assertEqual(tuple, type((1,)))
        self.assertEqual(list, type([1]))
        self.assertEqual(set, type({1}))

    def test_cast_primitives_types(self, x = '1'):
        self.assertEqual(x, '1')
        self.assertEqual(bool(x), True)
        self.assertEqual(int(x), 1)
        self.assertEqual(float(x), 1.0)
        self.assertEqual(dict([(x,x)]), {'1':'1'})
        self.assertEqual(tuple(x), ('1',))
        self.assertEqual(list(x), ['1'])
        self.assertEqual(set(x), {'1'})

    def test_boolean_cases(self):
        self.assertFalse(bool(0))
        self.assertTrue(bool(1))
        self.assertFalse(bool(''))
        self.assertTrue(bool('1'))
        self.assertFalse(bool([]))
        self.assertTrue(bool([1]))
        self.assertFalse(bool(()))
        self.assertTrue(bool((1,)))
        self.assertFalse(bool({}))
        self.assertTrue(bool({1:1}))
        self.assertTrue(bool({1}))

    def test_string_functions(self):

        self.assertTrue('1'.isnumeric())
        self.assertEqual(True ,'1'.isnumeric())
        self.assertFalse('a'.isnumeric())
        self.assertTrue('a'.isalpha())
        self.assertFalse('1'.isalpha())
        self.assertTrue('a1'.isalnum())
        self.assertFalse('a-1'.isalnum())
        self.assertTrue('100'.isdigit())
        self.assertFalse('0xF'.isdigit())
        self.assertFalse(' '.isdigit())
        self.assertTrue(' '.isspace())
        self.assertTrue('Python For Devs'.istitle())
        self.assertTrue('PYTHON FOR DEVS'.isupper())
        self.assertTrue('python for devs'.islower())
        self.assertEqual('PYTHON FOR DEVS', 'Python For Devs'.upper())
        self.assertEqual('python for devs', 'Python For Devs'.lower())
        self.assertEqual(['Python', 'For', 'Devs'], 'Python For Devs'.split(' '))
        self.assertEqual('Python For Devs', ' '.join(['Python', 'For', 'Devs']))
        self.assertEqual('Python for devs', 'python for devs'.capitalize())
        self.assertEqual('Python For Devs', 'python for devs'.title())
        self.assertEqual('pYTHON fOR dEVS', 'Python For Devs'.swapcase())
        self.assertEqual('Python-For-Devs', 'Python For Devs'.replace(' ','-'))
        self.assertEqual('Python For Devs', 'Python For {}'.format('Devs'))
        self.assertEqual('0001', '1'.zfill(4))
        self.assertTrue('Python for Devs'.startswith('Python'))
        self.assertTrue('Python for Devs'.endswith('Devs'))