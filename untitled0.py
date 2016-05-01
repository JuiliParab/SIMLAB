from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
xdata=[1,2,3,4,5,6]
xdata=np.asarray(xdata)
ydata=[40,50,60,70,80,90]
ydata=np.asarray(ydata)
def parabola(xdata,m,c):
    f=xdata*m+c
    return f
a=curve_fit(parabola,xdata,ydata)
print a[0]
m=a[0][0]
c=a[0][1]
print m,c
plt.plot(xdata,ydata,'ro')
yfit=parabola(xdata,m,c)
#for i in range(6):
    #yfit=xdata[i]*m+c
print yfit
plt.plot(xdata,yfit,color='g')