# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 15:37:57 2021

@author: Gitanshu
"""
# Pre-registered User Acess Info
# User1 - User = Gitanshu, Pass = Gitanshu2409
# User2 - User = TestUser, Pass = 123abc
# This Code is Very Confusing (Took 3 Days after dealing with BUGS !1!!)

import sys
import time

RegdUserlist = ["Gitanshu","TestUser"]
RegdPasslist = ["Gitanshu2409", "123abc"]

# Variable A is for conformation statement.
A = input("Are you sure to continue ahead [Y/N] : ")

# Code for A

def Problem():
    print("Can't validate your input, please try again later")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    sys.exit()
    
def codecomplete():
    print("Access Granted")
    time.sleep(1)
    print("Welcome "+e)
    time.sleep(1)
    print("I hope you enjoyed the code.")
    time.sleep(1)
    print(".")
    print('This one took a long time')

if (A == "Y"):
    print(".")
    time.sleep(1)
    print("This code might have some problems, If you notice any, plese contact me :)")
    time.sleep(1)
    print("Make your selection before you continue ahead...")
    time.sleep(2)
    print("Type 'Login' to login into your account or Type 'Register' to make a new account...")
    time.sleep(1)
    print("...")
    
b = input("Make your choice now : ")
    
if (A == "N"):
    print("Code Exiting")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    sys.exit()
    
    
# Code for B
# c will be New Username and d will be New Password 
# e will be Reged User and f will be Reged Password
if (b == "Register"):
    print("Thanks for choosing your selection, You may continue ahead.")
    print("...")
    time.sleep(1)
    c = input("New Username : ")
    print("...")
    time.sleep(1)
    d = input("New Password : ")
    print("...")
    time.sleep(1)
    print("Thanks for you input, Please wait for a while before you continue ahead.")
    time.sleep(1)
    print("...")
    print("Veryfying....")
    time.sleep(3)
    print("Verified :)")
    time.sleep(1)
    print("Please wait for a while, You will be prompted for login.")
    print("...")
    time.sleep(1)
    
e = input("Registered Username : ")
print("...")
    
if (b == "Login"):
    print("Thanks for choosing your selection, You may continue ahead.")
    print("...")
    time.sleep(1)

e = input("Registered Username : ")
print("...")
time.sleep(1)

if (e == RegdUserlist or c):
    print("Please enter your pasword now")
   
f = input("Registered Password : ")
time.sleep(1)
print("...")
    
if (f == RegdPasslist or d):
    print("........................................................")
    time.sleep(2)
    print("The Final Code Begins .........")
    time.sleep(2)
    codecomplete()
    
if (b != "Register" or "Login"):
    Problem()

if (e != RegdUserlist or c):
    Problem()

if (f != RegdPasslist or d):
    Problem()
    