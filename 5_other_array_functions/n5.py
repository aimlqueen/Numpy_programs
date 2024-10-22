# arg sort in 2d
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.argsort(a,axis=1)#b=np.argsort(a)
print(b)
# [[0 1 2]
#  [0 1 2]
#  [0 1 2]]
c=np.argsort(a,axis=0)
print(c)
#
# [[0 0 0]
#  [1 1 1]
#  [2 2 2]]