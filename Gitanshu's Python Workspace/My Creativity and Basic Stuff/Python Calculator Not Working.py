# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
import sys

def addition(x,y):
    return(x+y)

def subtraction(x,y):
    return(x-y)

def multiplication(x,y):
    return(x*y)

def division(x,y):
    return(x/y)
    
   
x = int(input("Choose Number 1 : "))
y = int(input("Choose Number 2 : "))
time.sleep(2)
print("Choose an operation to Confirm ---")
time.sleep(1)
print("1 = Addition [Number 1 + Number2]")
print("2 = Subtraction [Number 1 - Number2]")
print("3 = Multiplication [Number1 * Number2]")
print("4 = Division [Number1/Number2]")
print("5 = Exit")
a = input("Enter [1/2/3/4] : ")

if a == 1:
    addition(x,y)

if a == 2:
    subtraction(x,y)

if a == 3:
    multiplication(x,y)
    
if a == 4:
    division(x,y)
    
if a == 5:
    sys.exit()

