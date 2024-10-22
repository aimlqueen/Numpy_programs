import numpy as np
a=np.array([[1,2,3,44],[11,4,5,6],[72,2,8,9],[11,13,22,33]])
print(a)
# [[ 1  2  3 44]
#  [11  4  5  6]
#  [72  2  8  9]
#  [11 13 22 33]]
print("-------------------")
# slicing in 2D matrix 4X4
# [row,columns]
print(a[:2,:3]) #row : 0,1  col : 0,1,2
# [[ 1  2  3 ]
#  [11  4  5 ]
print("-------------------------")
print(a[1:2,1:3]) #row : 1,2 col :1,2
#  [4  5  ]
print(a[1:4:2,1:]) # row : 1,2,3 col : 1 , step row : 1,2,3
#  [ 4  5  6]
#  [13 22 33]]
print("-------------")
print(a[2::2,1::2]) #[[2 9]]
print("-------------")
# zeroth column of data
print(a[:,0])
print(a[:,:1])
# zeroth row of data
print(a[0, :])
















