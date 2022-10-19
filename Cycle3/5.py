import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array(['Walking','Cycling','Car','Bus','Train'])
ypoints=np.array([29,15,35,18,3])

plt.xlabel("Mode Of transport")
plt.ylabel("Frequency")
plt.title("Transport Data",loc='left')

plt.plot(xpoints,ypoints,linewidth=1,color='g')
plt.show()

