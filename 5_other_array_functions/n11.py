import numpy as np
a=np.array([1,2,3,4,5,66,71,8,4,2,1,5,4,3])
# collect even numbers only
b=np.where(a%2==0)
c=a[b]
print(c)