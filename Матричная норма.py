import numpy as np

a=np.array([[0.1,-0.4,0],
            [0.2,0,-0.3],
            [0,0.1,0.3]],dtype=float)

size=len(a)


def A1(a_):
    A1=np.zeros([size],dtype=float)
    a_=np.abs(a_)
    for i in range(size):
        A1[i]= np.sum(a_[:,i])
        
    print("A1 = ",np.amax(A1))
    return A1


def A2(a_):
    size_=len(a_)
    
    A_inf=np.zeros([size_],dtype=float)
    a_=np.abs(a_)
    
    for i in range(size_):
        A_inf[i]=np.sum(a_[i,:])
     
    print("A2 = ",np.amax(A_inf))
    return np.amax(A_inf)


A1(a)
A2(a)
