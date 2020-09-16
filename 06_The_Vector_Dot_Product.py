##### 06 The vector dot product #####
# 1) come up with 3 2D vectors, make sure they are orthogonal but niether orthogonal
#to the third

# 2) plot all three vectors -- make sure the axis are square and equal

import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([1,2])
v2 = np.array([2,-1])
v3 = np.array([5,5])


q = np.dot(v1,v2)
y = np.dot(v1,v3)
z = np.dot(v2,v3)
print(q)
print(y)
print(z)

plt.plot(v1, 'g', label = 'v1')
plt.plot(v2, 'r', label = 'v2')
plt.plot(v3, 'b', label = 'v3')
plt.legend()
plt.show()
