import numpy as np


def matrix_inf(a_):
    A_inf = np.zeros ( len(a_) ,dtype = np.float64 )
    a_ = np.abs(a_)
    for i in range(len(a_)):
        A_inf[i] = np.sum(a_[i,:])     
    return np.amax(A_inf) 

#Вставляем вместо X циферки
X=np.array([[X,X,X],[-X,X],[X,X,X]], dtype = np.float64 )
ans=np.array([[X,X,X]] , dtype = np.float64)

B=np.zeros([len(X),len(X)],dtype = np.float64)
c = ans / X.diagonal()

for i in range(len(X)):
    for j in range(len(X)):
        if i != j:
            B[i,j]= -X[i,j] / X[i,i]    
        else:
            B[i,j]=0  

eps=10**-3  
eps1 = ( 1 - matrix_inf(B) ) / ( matrix_inf(B) ) * eps
omega=1.12 

x0=np.zeros(len(B), dtype = np.float64)
x1=np.zeros(len(B), dtype = np.float64)
xs=np.zeros(len(B))
k=1


if matrix_inf(B)<1:
    while True:        
        
        for i in range(len(B)):
            for j in range(len(B)):
                if i!=j:
                    if i<j :
                        x1[i] += B[i,j] *x0[j]   
                    else:
                        x1[i] += B[i,j] *x1[j]
            x1[i]+=c[0,i]
        
        for i in range(len(x1)):
            x1[i] = omega * x1[i] +(1 - omega) * x0[i]
        
        
        xs=np.append(xs,x1,axis=0)        
        res  = max( abs( x1 - x0 ) ) 
        if max( abs( x1 - x0 ) ) < eps1:
            print("Итераций: ",k)
            print(x0)
            break
        else:
            k += 1
            x0 = x1
            x1=np.zeros(len(B), dtype = np.float64)
            
            if k>100:
                print("Вертай в зад")
                break

        
        
      