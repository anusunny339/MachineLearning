print('21MCA006','Anu Sunny')
import numpy as np
A = np.array([[1, 2], [3, 4], [5, 6]])
print(A)
# Singular-value decomposition
U, s, VT = np.linalg.svd(A)
# create m x n Sigma matrix
print("\nU:",U)
print("\ns:",s)
print("\nVT",VT)
Sigma = np.zeros((A.shape[0], A.shape[1]))
# populate Sigma with n x n diagonal matrix
Sigma[:A.shape[1], :A.shape[1]] = np.diag(s)
# reconstruct matrix
B = U.dot(Sigma.dot(VT))
print("\n",B)