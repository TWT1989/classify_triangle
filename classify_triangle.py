# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 17:50:07 2021

@author: Tim
"""

a = int(input('Enter a positive integer greater than 0 for side a: '))
b = int(input('Enter a positive integer greater than 0 for side b: '))
c = int(input('Enter a positive integer greater than 0 for side c: '))


def classify_triangle(a, b, c):
     
    
    if a <= 0 or b <= 0 or c <= 0:
        return "not a triangle"

    else:
        if a == b == c:
            return "triangle is equilateral"
        
        elif a == b or b == c or a == c:
            return "triangle is isosceles" 
    
        else: 
            return "triangle is scalene"

       
print(classify_triangle(a, b, c))



def classify_right_triangle(a, b, c):

    if a ** 2 + b ** 2 == c ** 2:
        return "triangle is also a right triangle"
    else:
        return "triangle is not a right triangle"

print(classify_right_triangle(a, b, c))


