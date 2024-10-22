import numpy as np

a=np.array([1,2,3,4,5,6,7,8,9])
print(a)
# sum of array
b=np.sum(a)
print(b)

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# sum of array
b=np.sum(a)
print(b)
# we can pass axis in this
# in 2D there will be 2Axis, (row,col)
# axis=0
# axis=1
c=np.sum(a,axis=0)
print(c)
c=np.sum(a,axis=1)
print(c)

