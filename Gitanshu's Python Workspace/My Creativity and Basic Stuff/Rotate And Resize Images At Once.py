# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 13:35:25 2021

@author: Gitanshu
"""
# Trying to open an image while resizing it and rotating it at the same time.

from PIL import Image

g = "C:/Users/Gitanshu/Downloads/sample.png"
a = Image.open(g)

b = (200,200)
c = 45

d = a.resize(b)
e = d.rotate(c)

e.show()
# This one took time TwT
