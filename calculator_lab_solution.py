# -*- coding: utf-8 -*-
"""calculator-lab-solution.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K_zfmwym8Y62fd-IHKJ2lg-M5ZTrXw84
"""

def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def mulitply(a,b):
  return a*b

def divide(x, y):
    if(y == 0):
      return "Invalid value for denominator, cant't divide by 0!"
    else:
      return x/y

def square(x):
    return x**2

def power(x, y):
    return x**y

def sqrt(x):
    return x**0.5