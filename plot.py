infile=open("data.csv",'r')
import csv
table=[]
for row in csv.reader(infile):
    table.append(row)
infile.close()

import numpy as np
start=1390000
end=1410000
span=end-start
t=np.zeros(span)
ch1=np.zeros(span)
sample=1000
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
ax.plot(t,ch1,linewidth=1,linestyle=':');
ax.set_xlim(3.9,4.1)
ax.set_xlabel('t/ms')
ax.set_ylabel('p/MPa')
#fig.savefig('tmp2.png',dpi=500)#滤波前
fig.savefig('tmp5.png',dpi=500)

for r in range(start,end):
    if pmax<ch1[r]:
        pmax=ch1[r]
        tmax=t[r]
for r in range(start,end-1):
    if ch1[r]>=pmax/2.718281828 and ch1[r]<=pmax/2.718281828:
        tdown=t[r]-tmax
outfile=open('out.dat','w')
outfile.write('pmax=%g\n' % pmax)
outfile.write('tmax=%g\n' % tmax)
outfile.write('tdown=%g' % tdown)

