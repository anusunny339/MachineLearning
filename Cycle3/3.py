import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array(['Jan','feb','Mar','Apr','May','jun','jul','Aug','Sep','Oct','Nov','Dec'])
ypoints=np.array([173,153,195,147,120,144,148,109,174,130,172,131])
plt.scatter(xpoints,ypoints,color='hotpink')

ypoints=np.array([189,189,105,112,173,109,151,197,174,145,177,161])
plt.scatter(xpoints,ypoints,color='yellow')

ypoints=np.array([185,185,126,134,196,153,112,133,200,145,167,110])
plt.scatter(xpoints,ypoints,color='blue')


plt.show()