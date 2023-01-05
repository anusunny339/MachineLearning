import numpy as np

A=np.array([
    [1,2,3],
    [3,1,5],
    [1,5,6]
])

B=np.array([
    [1,3,8],
    [2,1,1],
    [1,5,7]
])

#c=np.random.randint(9,size=(3,3))


print("matrix A:\n",A)
print("\nmatrix B:\n",B)

trans_a=np.transpose(A)
trans_b=np.transpose(B)

#print(2*trans_b)

res1=np.matmul(A,trans_a)
res2=np.matmul(2*B,trans_b)

print("\nAAT - 2BBT = \n",np.subtract(res1,res2))