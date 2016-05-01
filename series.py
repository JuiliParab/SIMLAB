# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:10:37 2016

@author: JUILI
"""

import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
k1=.1
k2=.06
def g(y, x):
    dcadt=-k1*y[0]
    dcbdt=k1*y[0]-k2*y[1]
    dccdt=k2*y[1]
    y[2]=1-y[0]-y[1]
    return dcadt,dcbdt,dccdt

# Initial conditions on y, y' at x=0
init = 1,0,0
# First integrate from 0 to 2
x = np.linspace(0,100,40)
sol=odeint(g, init, x)
# Then integrate from 0 to -2
plt.plot(x, sol[:,0], color='b')
plt.plot(x, sol[:,1], color='r')
plt.plot(x, sol[:,2], color='g')
plt.legend()

plt.show()
