import numpy as np
m1=np.array(
    [
        [1,2,3,4],
        [4,5,6,7],
        [1,2,3,4],
        [1,5,6,7]
    ]
)

print("first row ex",m1[1:4])
print("ex last col",m1[:,0:3])
print("\n",m1[1:3,0:3])