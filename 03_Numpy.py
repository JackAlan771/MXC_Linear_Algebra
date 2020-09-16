#Assignment
# 1) create list of 15 numbers from 4 to 100
# 2) round those numbers to the nearest integer, and store in another vairble
# 3) print out #2
# 4) print out the sqrt of each number in the list

import numpy as np

list = np.linspace(4,100,15)
roundedlist = np.round(list)
print(roundedlist)
print(np.sqrt(list))

