import matplotlib.pyplot as plt
import numpy as np

plt.xlabel("Year")
plt.ylabel("Value")
plt.title("Value Depreciation",loc='left')


xpoints=np.array([2001,2002,2003,2004,2005,2006,2007])
ypoints=np.array([24000,22500,19700,17500,14500,10000,5800])

plt.plot(xpoints, ypoints, linestyle='dashed',color='r' ,marker='*',mfc='g',ms=20)
plt.show()
