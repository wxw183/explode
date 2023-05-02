infile=open("data.csv",'r')
import csv
table=[]
for row in csv.reader(infile):
    table.append(row)
infile.close()

import numpy as np
sample=1000
start=0
end=10000000-sample
span=end-start
t=np.zeros(span)
ch1=np.zeros(span)


for r in range(start,end+sample):
    for c in range(2):
        table[r][c]=float(table[r][c])

for r in range(start,end):
    t[r-start]=table[r][0]*1000.0
    p=0.0
    for m in range(sample):
        p+=table[r+m][1]
    p/=sample
    p/=0.1539
    ch1[r-start]=p
import matplotlib as mpl
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(40,10))
ax=fig.add_axes((0.1,0.1,0.8,0.8),facecolor="#e1e1e1")
ax.plot(t,ch1,linewidth=1);
ax.set_xlim(-10,90)
ax.set_xlabel('t/ms')
ax.set_ylabel('p/MPa')
#fig.savefig('tmp2.png',dpi=500)#滤波前
fig.savefig('origin.png',dpi=500)
