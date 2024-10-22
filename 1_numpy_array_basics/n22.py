# 2D , 4X5
import numpy as np
a=np.array([
    [1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]
])
print(a.shape)
# change to 5X4
b=a.reshape(5,4)
print(b.shape)
# change to 10X2
c=b.reshape(10,2)
print(c.shape)