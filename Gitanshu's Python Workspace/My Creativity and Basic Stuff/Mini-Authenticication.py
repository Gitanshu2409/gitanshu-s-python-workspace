# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:02:48 2021

@author: Gitanshu Pal
"""
import sys
import time
def TestFunc123():
    time.sleep(1)
    print("Access Granted, Welcome "+a)
    time.sleep(1)
    print("Hope You Enjoyed!")
    time.sleep(1)
    print("Program Ends :D")
    
a = input("Enter Your Username to Continue Ahead:")

if (a!=("Gitanshu")):
    time.sleep(1)
    print("Wrong Username!")
    time.sleep(2)
    print("Access Denied.")
    sys.exit()
    
if (a==("Gitanshu")):
    time.sleep(1)
    print("One More Step Before You Continue")
    time.sleep(1)
    
b = input("Go Ahead And Enter The Correct Password:")
    
if (b!=("Gitanshu2409")):
    time.sleep(1)
    print("Wrong Password!")
    time.sleep(2)
    print("Access Denied.")
    sys.exit()
     
if (b==("Gitanshu2409")):
    time.sleep(2)
    TestFunc123()
        
    
   
    