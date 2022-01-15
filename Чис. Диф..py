import numpy as np
import matplotlib.pyplot as plt

def f_(x_):
    return np.round((3*np.sin(2*x_**2 * np.exp(x_))),6)

def f1_(x_,h_):
    return np.round(((f_(x_ + h_)- f_(x_ - h_) )/( 2*h )),6  )

def f2_(x_,h_):
    return np.round(( (f_(x+h) - 2 * f_(x) + f_(x-h)) / (h**2) ),6)

x_start=0
x_end=20

h=0.5
count_val = 20/h

x=np.arange(x_start, x_end+h, h)
y=f_(x)

y1 = f1_(x,h)
y2 = f2_(x,h)

mea_er1 = f_(x)-y1

plt.grid()
plt.plot(x, y, label='y=f(x)')
plt.plot(x, y1, label="y=f'(x)")
plt.plot(x, y2, label="y=f''(x)")
plt.legend()

