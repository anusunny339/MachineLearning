print('21MCA006','Anu Sunny')
import numpy as np
a = np.array([
              [1, 2,4],
              [3, 5,6],
              [7, 8, 9]
           ])
b = np.array([1, 2, 7])

x = np.linalg.solve(a, b)
print(" X=",x)

print(np.allclose(np.dot(a, x), b))