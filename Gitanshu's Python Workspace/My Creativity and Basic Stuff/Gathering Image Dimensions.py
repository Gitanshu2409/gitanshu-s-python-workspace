# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 13:24:11 2021

@author: Gitanshu
"""

# Gathering dimensions of an Image.
from PIL import Image
g = "C:/Users/Gitanshu/Downloads/sample.png"
a = Image.open(g)
y,z = a.size
print(y,z)