# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 20:07:54 2021

@author: Gitanshu
"""

# Trying to understand Lambda
# a,b,c,d are variables but are defined while printing the solution.

g = lambda a, b, c, d : a + b - c *d
print(g(9, 6, 8, 4))

# Got it !!
# Assigns values while performing any operation with the listed Variable in lambda in same respective order.