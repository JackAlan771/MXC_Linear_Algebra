##### 05 Vectors and Scalar multiplication #####
# Create two vectors
# plot each vector
# plot v1+v2, v1-v2, (v1*4 + v2/2)

import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([1,2,3,4,5])
v2 = np.array([4,6,9,12,13])

plt.plot(v1, 'r', label = 'v1')
plt.plot(v2, 'g', label = 'v2')
plt.plot(v1+v2, label = 'v1+v2')
plt.plot(v1*4 + v2/2, 'o', label = 'v1*4 + v2/2')
plt.legend()
plt.show()
