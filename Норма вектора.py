import numpy as np

print("введите порядок нормы")
p=int(input())
size=4                         

a=np.zeros([size])
res=0

print("введите эл-ты")
for i in range(size):
    a[i]=input()


def Vec(a_,p_):
    a_=np.power(a_, p_)
    res=np.sum(a_)
    res=np.power(res, 1/p_)
    
    print(res)
    return res
    
Vec(a,p)