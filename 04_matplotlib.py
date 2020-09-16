##### 04 The Matplotlib Module #####
# Plot a Red X in a Matrix
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-9,10)
#y = np.arange(10,-9)

plt.plot([-9,10], [-9,10],'r', label = 'test line')
plt.plot([9,-10], [-9,10],'r', label = 'test line 2')
plt.legend()
plt.show()


