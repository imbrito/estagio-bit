#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from math import pi, factorial
from functools import reduce
from functional_programming import combinatorial_analysis

radius = lambda x: x / (2 * pi)
triangle_area = lambda x, y: (x * y) / 2
rectangle_area = lambda x, y: x * y
square_area = lambda x: x ** 2
impar = lambda x: x % 2
par = lambda x: not x % 2

class FunctionalProgrammingSpec(TestCase):
   
    def test_it_lambda(self):
        self.assertEqual(1, (lambda x: x ** 2)(1))
        self.assertEqual(9, (lambda x: x ** 2)(3))
        self.assertEqual(2.39, round(radius(15), 2))
        self.assertEqual(3, triangle_area(2,3))
        self.assertEqual(6, rectangle_area(2,3))
        self.assertEqual(4, square_area(2))
    
    def test_it_filter(self):
        self.assertEqual([1,3,5,7,9], list(filter(impar, range(10))))
        self.assertEqual([0,2,4,6,8], list(filter(par, range(10))))
    
    def test_it_map(self):
        self.assertEqual([9,8,7,6,5], list(map(abs, [-9,-8,-7,-6,-5])))
        self.assertEqual(['0','1','2','3','4'], list(map(str, range(5))))
        self.assertEqual([1,4,9,16,25,36,49], list(map(square_area, range(1,8))))
        self.assertEqual([1, 1, 2, 6, 24, 120, 720], list(map(factorial, range(7))))

    def test_it_reduce(self):
        self.assertEqual(sum(range(10)), reduce(lambda x,y: x + y, range(10)))
        self.assertEqual(factorial(6), reduce(lambda x,y: x * y, range(1,7), 1))

    def test_it_map_reduce_fake(self):
        words = {"map": [1,1,1], "reduce":[1,1,1,1,1,1]}
        reduce_by_key = lambda x: (x, reduce(lambda x, y: x + y, words[x]))
        self.assertEqual([('map',3),('reduce',6)], sorted(list(map(reduce_by_key, words.keys()))))
    
    def test_it_zip(self):
        self.assertEqual([(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)], list(zip([0,2,4,6,8],[1,3,5,7,9])))
        self.assertEqual([('l','o'),('v','e')], list(zip(list('lv'),list('oe'))))

    def test_it_list_comprehension(self):
        self.assertEqual(list(filter(par, range(10))), [x for x in range(10) if not x % 2])
        self.assertEqual(list(filter(impar, range(10))), [x for x in range(10) if x % 2])
        self.assertEqual(list(map(square_area, range(1,8))), [pow(x,2) for x in range(1,8)])
        self.assertEqual(list('bit'), [x for x in 'bit'])
    
    def test_it_dict_comprehension(self):
        self.assertEqual({'A':0,'B':1,'C':2,'D':3}, dict([(chr(65+x), x) for x in range(4)]))
        self.assertEqual({0:1,1:1,2:2,3:6,4:24,5:120,6:720}, {x : factorial(x) for x in range(7)})

    def test_it_combinatorial_analysis(self):
        self.assertEqual([102,120,201,210], combinatorial_analysis(120))
        self.assertEqual([102,120,201,210], combinatorial_analysis(102))
        self.assertEqual([102,120,201,210], combinatorial_analysis(201))
        self.assertEqual([102,120,201,210], combinatorial_analysis(210))
        self.assertEqual([112,121,211], combinatorial_analysis(211))
        self.assertEqual([112,121,211], combinatorial_analysis(121))
        self.assertEqual([112,121,211], combinatorial_analysis(112))