# sort
import numpy as np
a=np.array([11,2,3,4,5,6,7,8,9])
b=np.sort(a)
print(b)#[ 2  3  4  5  6  7  8  9 11]
c = np.sort(a)[::-1] #reverse , :: means full data
print(c)

n=np.array([[11,2,13],[41,15,6],[17,81,9]])
m=np.sort(n) #m=np.sort(n,axis=1)
print(m)
# [[ 2 11 13]
#  [ 6 15 41]
#  [ 9 17 81]]

o=np.sort(n,axis=0)
print(o)
# [[11  2  6]
#  [17 15  9]
#  [41 81 13]]