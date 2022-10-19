import numpy as np
mat=np.random.randint(7,size=(3,3))
print('matrix :\n',mat)
print('inverse of matrix :\n',np.linalg.inv(mat))
print('rank of matrix:\n',np.linalg.matrix_rank(mat))
print('determinat:\n',np.linalg.det(mat))
print('transform to 1D array:\n',mat.flatten(order='c'))

v,vr=np.linalg.eig(mat)
print('eigen values of the matrix:\n',v)
print('eigen vectors of matrix:\n',vr)
