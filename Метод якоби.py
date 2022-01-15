import numpy as np
import NORMA_matrix as NM  



eps=10**-3                     

X=np.array([[6.25,-1,0.5],
            [-1,5,2.12],
            [0.5,2.12,3.6]], dtype='float64' )


ans=np.array([[7.5,
               -8.68,
               -0.24]] , dtype='float64')


B=np.zeros([len(X),len(X)],dtype='float64')


for i in range(len(X)):
    for j in range(len(X)):
        if i != j:
            B[i,j]= -X[i,j] / X[i,i]    
        else:
            B[i,j]=0   

c = ans / X.diagonal()


eps1 = ( 1 - NM.Ainf(B) ) / ( NM.Ainf(B) * eps) 

x0=np.zeros([len(B)])


def Mult_matrix_vec(matrix_,vec_): 
    size_=len(matrix_)
    res_=np.zeros([size_],dtype='float64')
    
    for i in range (size_):
        for j in range(size_):
            res_[i] += vec_[i] * matrix_[j,i]  
    return res_



eps1 = ( 1 - NM.Ainf(B) ) / ( NM.Ainf(B) * eps) 
print("eps-  ",eps,"\n")
print("eps1-  ",eps1,"\n")

x0=np.zeros([len(B)],dtype='float64')
x1=np.zeros([len(B)],dtype='float64')


while True:
    x1 = Mult_matrix_vec( B , x0 ) + c
    res = x0 - x1
    temp_res_max =np.amax(res)
    
    if temp_res_max < eps:
        print(res)
        break
    else:












