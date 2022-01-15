import numpy as np



def Vvod_Matrix():
    print("Enter the number of unknown elements")
    ss=int(input())
    matrix_=np.empty((ss,ss+1))
    
    for i in range(ss):
        print("line-"+str(i))
        for j in range(ss+1):
            matrix_[i,j]=float(input())
    
    return(matrix_)


def Alfs_and_Matr():
    matrix_=Vvod_Matrix()
    print("Current matrix is: \n",matrix_,'\n'*2)
    xs_max=len(matrix_)
    
    for i in range(xs_max):
        al=matrix_[i+1:,i]/matrix_[i,i]
        matrix_[i+1:] +=-np.full_like(matrix_[i+1:,:],matrix_[i])*(al[:,np.newaxis])
    print("matrix after changes: \n",matrix_,'\n'*2)
    return matrix_
         

a=np.array([[1,-1,2,-1],
           [3,2,1,2],
           [2,2,1,3]], dtype=float)

b=np.array([[1,2,3,-2,1],
            [2,-1,-2,-3,2],
            [3,2,-1,2,-5],
            [2,-3,2,1,11]],dtype=float)


def Res():
    matrix_=Alfs_and_Matr()
    answ=np.empty(len(matrix_),dtype="float64")
    for i in range(len(matrix_)-1,-1,-1):
        answ[i]=matrix_[i][len(matrix_)]/matrix_[i,i]
        for j in range(i,-1,-1):
            if matrix_[j-1][i]!=0:
                matrix_[j-1][-1]-=matrix_[j-1][i]*answ[i]
                matrix_[j-1][i]=0
    print("answers is:",answ)
    
Res()    
