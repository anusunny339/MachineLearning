import numpy as np
m1=np.array([
    [1,2],
    [3,4]
])

m2=np.array([
    [5,6],
    [7,8]
])

print("addition",np.add(m1,m2))

print("sub",np.subtract(m1,m2))

print("mul",np.matmul(m1,m2))
ele=np.multiply(m1,m2)

print("div",np.divide(m1,m2))