# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 19:23:28 2021

@author: Tim
"""
import unittest

import classify_triangle

class TestTriangle(unittest.TestCase):
    
    def test_triangle_equilateral(self):
    
        self.assertEqual(classify_triangle.classify_triangle(1,1,1), "triangle is equilateral")
        self.assertEqual(classify_triangle.classify_triangle(4,4,4), "triangle is equilateral")
        
    
    def test_triangle_isosceles(self):
    
        self.assertEqual(classify_triangle.classify_triangle(4,4,5), "triangle is isosceles")
        self.assertEqual(classify_triangle.classify_triangle(7,7,4), "triangle is isosceles")
        self.assertEqual(classify_triangle.classify_triangle(8,12,8), "triangle is isosceles")
    
    
    def test_triangle_scalene(self):
    
        self.assertEqual(classify_triangle.classify_triangle(3,4,5), "triangle is scalene")
        self.assertEqual(classify_triangle.classify_triangle(10,4,7), "triangle is scalene") 
    
    
    def test_triangle_right(self):
        
        self.assertEqual(classify_triangle.classify_right_triangle(3,4,5), "triangle is also a right triangle")
        self.assertEqual(classify_triangle.classify_right_triangle(3,4,6), "triangle is not a right triangle")

    def test_triangle_error(self):
        
        self.assertEqual(classify_triangle.classify_triangle(0,0,0), "not a triangle")
        self.assertEqual(classify_triangle.classify_triangle(-1,-1,-1), "not a triangle")
        self.assertEqual(classify_triangle.classify_triangle(0,8,9), "not a triangle")
        self.assertEqual(classify_triangle.classify_triangle(3,0,7), "not a triangle")
        self.assertEqual(classify_triangle.classify_triangle(6,5,0), "not a triangle")
        self.assertEqual(classify_triangle.classify_triangle(-2,4,5), "not a triangle")
        self.assertEqual(classify_triangle.classify_triangle(3,-3,5), "not a triangle")
        self.assertEqual(classify_triangle.classify_triangle(3,4,-7), "not a triangle")
        self.assertEqual(classify_triangle.classify_triangle(-1,0,-1), "not a triangle")


if __name__ == '__main__':
    unittest.main()
    
  
    