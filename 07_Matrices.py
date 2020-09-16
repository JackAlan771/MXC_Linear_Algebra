##### 07 Matrices #####
# 1) Create 3 matrices: 2x2, 2x2, 3x2
# 2) Compute Scalar-matrix multiplication (scalar being a single number)
# 3) Add all pairs of matrices

import numpy as np

m1 = np.array([[1,2],[1,2]])
m2 = np.array([[4,5],[9,9]])
m3 = np.array([[1,7],[1,7],[1,7]])
blnk = np.array([[0,0]])
m11 = np.concatenate((m1,blnk), axis = 0)
m21 = np.concatenate((m2,blnk), axis = 0)

# Scalar matrix multiplication
print(m1*2)
print(m2*2)
print(m3*3)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#Add all pairs of matrices


print(m11+m3)
print(m21+m3)
print(m1+m2)

#Owned it. All you have to do is add another line of the matrix. But it adds the matrix and
#returns an incorrect set of numbers... What's going on?




