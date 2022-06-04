# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Ways to open image in python.
from PIL import Image

def Method1():
    a = Image.open(r"C:/Users/Gitanshu/Downloads/sample.png")
    a.show()
    # Without Specifying the Path using another variable.
    
def Method2():
    b = "C:/Users/Gitanshu/Downloads/sample.png"
    c = Image.open(b)
    c.show()
    # Specifying the path of image using another variable.
    
Method1()
Method2()
#They both work the same XD.

    
