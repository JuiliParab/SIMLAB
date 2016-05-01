import csv
import numpy as np
i=0
a=[]
b=[]
f=open("ExamProblemData.csv")
csv_f=csv.reader(f)
for  row  in csv_f:
    a.append(row[2])
    b.append(row[3])
print a
print b
a=np.asarray(a)
b=np.asarray(b)
c=int(np.transpose(a))+int(np.transpose(b))
print c
       