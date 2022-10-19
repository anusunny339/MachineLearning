print('21MCA006','Anu Sunny')
import numpy as np


A=np.matrix([[0,2,4],
             [-2,0,3],
             [-4,-3,0]])
print(A)
B=A.transpose()
if A.all() == B.all():
    print("matrix is symmetric ")
else:
    print("not  symmetric")

if np.allclose(-A,B)==True :
    print("matrix is skew symmetric")
else:
    print("not skew symmetric")