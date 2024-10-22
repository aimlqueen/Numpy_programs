import numpy as np
a=np.array([1,2,3,4,5,6,71,8,4,2,1,5,4,3])
b=a>8
print(b)
print("-------------")
# Using boolean indexing to get elements greater than 8
result = a[a > 8]
print(result)
print("-----------")
c=a[b]
print(c)

