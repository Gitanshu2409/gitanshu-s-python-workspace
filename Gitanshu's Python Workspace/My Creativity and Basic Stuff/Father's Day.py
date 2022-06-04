# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 09:47:31 2021

@author: Gitanshu
"""

import sys
import time
from PIL import Image

a = Image.open(r"D:/Gitanshu_Data/Nothing/p1.png")
b = Image.open(r"D:/Gitanshu_Data/Nothing/p2.png")
c = Image.open(r"D:/Gitanshu_Data/Nothing/p3.png")
d = Image.open(r"D:/Gitanshu_Data/Nothing/p4.png")
e = Image.open(r"D:/Gitanshu_Data/Nothing/p5.png")

print("...")
time.sleep(3)
print("..")
time.sleep(2)
print(".")

time.sleep(2)
a.show()
time.sleep(5)
b.show()
time.sleep(3)
c.show()
time.sleep(4)
d.show()
time.sleep(3)
e.show()
time.sleep(5)
sys.exit()
