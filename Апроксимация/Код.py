import numpy as np
import matplotlib.pyplot as plt

x=np.fromfile('x.txt',float,sep='\n')
y=np.fromfile('y.txt',float,sep='\n')

size_x=len(x) 
sum_y=sum(y)

s1 = np.sum(x)
s2 = np.sum( x**2 )
s3 = np.sum( y*x )  

x_0= ( ( sum_y * s2 - s1 * s3) / ( size_x * s2 - s1**2 ))
x_1=(( size_x * s3 - s1 * sum_y) / ( size_x * s2 - s1**2 ))
y_2= ( x*x_1+ x_0 )


plt.plot(x, y, color='r', marker='o', label='y')
plt.plot(x, y_2, color='b', linewidth=2, label='apr')
plt.legend()
plt.show()









