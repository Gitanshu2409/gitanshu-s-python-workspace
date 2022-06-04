# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:53:52 2021

@author: Gitanshu
"""
# Using direct path will be better, but Okay!!

from PIL import Image

g = "C:/Users/Gitanshu/Downloads/sample.png"
a = Image.open(g)
imgsize = 200,200
b = a.resize(imgsize)
b.show()

# Finally figured it out.