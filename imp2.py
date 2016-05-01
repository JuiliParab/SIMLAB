
import pandas as pd
import numpy as np
location='D:\SEM6\SIMEXAM\ExamProblemData.csv'
df=pd.read_csv(location,"ExamProblemData")
Xdata=df['a']
x=np.array([Xdata])
print x
YData=df['b']
y=np.array([YData])
print y
