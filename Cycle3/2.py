import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array(['Mon','Tues','wed','Thurs','Fri'])
ypoints=np.array([300,450,150,400,650])


plt.subplot(1,2,1)
plt.grid(color = 'blue', linestyle = 'dotted')
plt.title("Sales Data1",loc='right')
plt.plot(xpoints,ypoints,linestyle='dotted',color='c',marker='h',mfc='m',mec='k')


ypoints=np.array([400,500,350,300,500])


plt.subplot(1,2,2)
plt.title("Sales Data2",loc='center')
plt.plot(xpoints,ypoints,linestyle='dashed',color='y',marker='d',mfc='g',mec='r')

plt.grid(color = 'blue', linestyle = 'dotted')
plt.show()