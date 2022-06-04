# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 13:24:11 2021

@author: Gitanshu
"""

# Rotating The Image
from PIL import Image
g = "C:/Users/Gitanshu/Downloads/sample.png"
a = Image.open(g)
c = 45
b = a.rotate(c)
b.show()

# Speedrunning the basics.