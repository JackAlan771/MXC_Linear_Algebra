##### 08 Transposint Vectors and Matrices #####
# 1) what happens when we transpose twice, M, M.T, M.TT
# 2) confirm transpose operation works on non-square matrices
import numpy as np

M = np.random.randn(3,3)
print(M)
print('#######')
print(M.T)
print('#######')
N = M.T
print(N)
print('#######')
print(N.T)
#Anser is that if you transpose twice, it just goes back to it's original state.

print('')
a = np.round(10*np.random.randn(15,4))
print(a)
print('')
print(a.T)
#The answer is yes, it does. The transpose operation still works on non-square matrices.
