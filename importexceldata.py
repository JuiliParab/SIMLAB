
import pandas as pd
import numpy as np
location='D:\SEM6\SIMEXAM\imp.xlsx'
df=pd.read_excel(location,0)
Xdata=df['X']
x=np.array([Xdata])
print x
YData=df['Y']
y=np.array([YData])
print y
y=np.multiply(y,2)
print y
