# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 12:22:18 2021

@author: Gitanshu
"""

# Learning __init__() function in classes.

class ProgrammingLangs:
    def __init__(self,name,year):
        self.name = name
        self.year = year
        
a1 = ProgrammingLangs("Python", 1991)
a2 = ProgrammingLangs("Java", 1995)

print(a1.name)
print(a1.year)
print(".")
print(a2.name)
print(a2.year)

#Got it