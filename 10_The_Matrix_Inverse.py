##### 10 The Matrix Inverse #####
# 1) Create a 3D vector, create a diagonal matrix from that vector diagonal matrix
# 2) Compute the inverse of the matrix
# 3) Make any nonsquare matrix (any size) and try to compute it's inverse

import numpy as np

a = np.array([1,2,3])
b = np.diag(a)
binv = np.linalg.inv(b)
print (b)
print('')
print(binv)
print(binv@b)
#Was actually really cool

c = np.array([[5,4],[4,5],[9,3]])
cinv = np.linalg.inv(c)
