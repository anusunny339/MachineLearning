print('21MCA006','Anu Sunny')
import numpy as np

mat=np.array([
    [2,4],
    [5,6]
])
print('matrix :\n',mat)
print('cube using multiply:\n',np.multiply(mat,np.multiply(mat,mat)))
print('cube using power:\n',np.power(mat,3))
print('cube using **:\n',mat**3)
print('cube using *:\n',mat*mat*mat)
print('identity matrix of given matrix:\n',np.identity(2,dtype=int))
print('element of the matrix to different powers:\n',np.power(mat,[[1,1],[2,2]]))

y=np.array([
    [5,6],
    [9,0]
])

print('X^2 +2Y\n',(mat**2)+(2*y))