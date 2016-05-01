from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import numpy as np

xdata=[1,2,3,4,5,6]
xdata=np.asarray(xdata)
ydata=[40,50,60,70,80,90]
ydata=np.asarray(ydata)

# print optimization.leastsq(func, x0, args=(xdata, ydata))

def func(xdata,a,b):
    f=a*xdata+b
    return f
x0=[5,20]
ans=leastsq(func, x0, args=(xdata, ydata))
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('Line')

plt.plot(xdata,yfit,color='g')

