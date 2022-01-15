import numpy as np
import matplotlib.pyplot as plt

x=np.fromfile('x.txt',float,sep='\n')
y=np.fromfile('y.txt',float,sep='\n')

SIZE= len(x)

a=np.zeros(SIZE)

a[0]=y[0]
a[SIZE-1]=y[SIZE-1]

a=y
for i in range(1,SIZE - 1):
    a[i] = y[i] + (  (x[i]-x[i-1] )/(x[i+1]-x[i-1])  *  (y[i+1]-y[i-1] )   ) 


plt.plot(x, y, color='r',marker='o', label='y')
plt.plot(x, a, color='b', linewidth=2, label='y_inter')

plt.legend()
plt.grid()
plt.show()


