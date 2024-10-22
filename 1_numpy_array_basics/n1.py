# create array
import numpy as np
# 1D array
a=np.array([1,2,3,4])
print(a)
# print dimensions of array
print(a.ndim)


# 2D array
b=np.array([[1, 2, 3],[4, 5, 6]])
# print dimensions of array
print(b.ndim)

#3D array
c=np.array([
    [
        [1, 2, 3],[4, 5, 6]
    ],
    [
        [7, 8, 9],[10, 11, 12]
    ]
])
# print dimensions of array
print(c.ndim)


#order of matrix
print(a.shape)
print(b.shape)
print(c.shape)
