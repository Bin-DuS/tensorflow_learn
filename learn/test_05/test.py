import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,2*np.pi,50)
y = np.sin(x)
#plt.plot(x,y)
#plt.plot(x,y*2)
plt.plot(x,y,'y*-')
plt.plot(x,y*2,'m--')
#plt.plot(x,x*x)
plt.show()
