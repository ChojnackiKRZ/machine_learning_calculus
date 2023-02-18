# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:53:40 2023

@author: krzys
"""

#lesson 1.Calculate and plot derivative

import sympy as sym
import numpy as np
import matplotlib.pyplot as plt


function = 'x**3 - 2*x**2 + 1'

def funcx(x, function):
    return eval(function)

def der_funcx(x, function):
    return eval(str(sym.diff(str(function))))

# compute f(x) for x=--2 to x=3
x = np.linspace(-2,3,500)
y = funcx(x, function = function)
# Plot f(x) on left half of the figure
fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(121)
ax.plot(x, y)
ax.set_title("y=f(x**3 - 2*x**2 + 1)")

ax = fig.add_subplot(122)
y1 = der_funcx(x = x, function = function)
ax.plot(x, y1, c="r", alpha=0.5, label="rate")
ax.set_title("derivative") 

plt.show()
