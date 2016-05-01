import numpy as np
from scipy.optimize import leastsq
xdata=[1,2,3,4,5,6]
xdata=np.asarray(xdata)
ydata=[40,50,60,70,80,90]
ydata=np.asarray(ydata)

def fitfunc(p,xdata):
    f=p[0]*xdata+p[1]
    return f

def errfunc(p,xdata,ydata):
    e=fitfunc(p,xdata)-ydata
    return e
    
guess=np.array([10,10])
ans=leastsq(errfunc,guess,args=(xdata,ydata))[0]
print ans