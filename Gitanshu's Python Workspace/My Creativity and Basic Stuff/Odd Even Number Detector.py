# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:24:14 2021

@author: Gitanshu Pal
"""

#Even and Odd number Detector.

a = int(input("Choose the number to determine whether it is even or odd : "))

if (a%2 == 0):
    print("The number is even.")
elif (a == 0):
    print("The number is Neutral (Neither even nor odd).")
else:
    print("The number is odd.")