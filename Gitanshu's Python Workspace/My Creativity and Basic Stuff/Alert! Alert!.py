# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 20:24:04 2021

@author: Kartik
"""
#Alert! Alert! Alert!

#Variables for LoopingGitansh

z = 1

import time

def Alert():
   while(z != 2):
       time.sleep(1)
       print("Alert!")

def FinalFunc():
    time.sleep(1)
    print("Welcome Sir :)")
    Space()
    time.sleep(1)
    print("Your Access Information is listed Below ----")
    Space()
    time.sleep(1)
    print("Username : "+a)
    print("Password : "+b)

def Space():
    time.sleep(1)
    print(".")

print("Before you Continue Ahead")
Space()
Space()
print("You Can Only Enter Your Acess Information Once.")
Space()
Space()
print("Proceed With Caution!")
Space()
Space()

a = input("Enter Username : ")

if (a == ("Gitanshu")):
    b = input("Enter Password : ")

if (a != ("Gitanshu")):
    Alert()

if (b != ("Gitanshu2409")):
    Alert()

if (b == ("Gitanshu2409")):
    FinalFunc()
