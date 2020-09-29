'''
Author : F323RED
Date : 2020/9/29
Version : 0.1.0
Describe : Python homework-002
'''

import pylab as lab
import math

def F(x) :      # Define function F()
    return (math.cos(x) ** 2) / (max(1.0, 2 * x - 1) ** 0.5)

#---------------------
# Begining of program

a = 10 * math.pi
b = 0                           # X c [0, 10 * PI]
n = 1000                        # Number of points

listX = lab.linspace(a, b, n)
listY1 = [F(i) for i in listX ]

# Some fancy stuff
lab.title("f(x) = cos(x)^2 / max(1, 2x+1)^0.5")
lab.xlabel("X axis")
lab.ylabel("Y axis")
lab.grid()

lab.plot(listX, listY1)         # Draw graph of F(x)

lab.show()                      # Show graph
