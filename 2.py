import numpy as np

m1=np.random.randint(10,size=(3,3))
print("inv",np.linalg.inv(m1))
print("rank",np.linalg.matrix_rank(m1))
print("det",np.linalg.det(m1))

print("eig",np.linalg.eig(m1))

print("identity",np.identity(3,dtype=int))

print("power",np.power(m1,[[1,2,1],[1,1,1],[1,1,1]]))

