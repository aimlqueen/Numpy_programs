import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
# slicing
print(a) #[ 1  2  3  4  5  6  7  8  9 10]
print(a[2]) #3
print(a[2:5])#[3 4 5]
print(a[3:])#[ 4  5  6  7  8  9 10]
print(a[:5])#[1 2 3 4 5]
print(a[:])#[ 1  2  3  4  5  6  7  8  9 10]
print(a[3:10:2])#[ 4  6  8 10]