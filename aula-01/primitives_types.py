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
        '''
        Crie um caso de teste para cada um dos métodos abaixo. 

        String Methods:
            isnumeric
            isalpha
            isalnum
            isdigit
            isspace
            istitle
            isupper
            islower
            upper
            lower
            split
            join
            capitalize
            swapcase
            title
            replace
            format
            zfill
            startswith
            endswith

        Para informações sobre o funcionamento de cada um visite o link: 
        https://docs.python.org/3.7/library/stdtypes.html#string-methods
        '''