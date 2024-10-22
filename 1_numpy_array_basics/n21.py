# 2D 3X4
import  numpy as np
a=np.array([[1,2,3,4],[2,3,4,5],[5,6,78,5]])
print(a.ndim)# 2
print(a.shape)#(3,4)
print("="*30)
# reshape(): to change order of matrix
# change to 4X3
b=a.reshape([4,3])
print(b)
print(b.ndim)# 2
print(b.shape)#(43)
# change to 3X3
c=a.reshape([6,2])
print(c)