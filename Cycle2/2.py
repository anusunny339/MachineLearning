print('21mca006','Anu Sunny')

import numpy as np

arr=np.array([
    [1+4j,3+2j,4+2j],
    [1+2j,4+5j,9+1j]

])

print(arr)
print("\nnof row and columns =",arr.shape)
print("\ndimension of array=",arr.ndim)

newarr=arr.reshape(3,2)
print("\nreshaped array(3*2)\n",newarr)