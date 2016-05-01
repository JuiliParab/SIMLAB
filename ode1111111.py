import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
b=c=1
def g(y,x,b,c):
    y0=y[0]
    y1=y[1]
    y2=(6*x-8)*y0/(3*x-1)*b+(3*x+2)*y1*c/(3*x-1)
    return [y1,y2]
x=np.linspace(-2,2,100)
init=[2,3]
sol=odeint(g,init,x,args=(b,c))
#print sol
plt.plot(x,sol[:,0])
plt.show()

