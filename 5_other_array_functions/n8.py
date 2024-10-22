import numpy as np
a=np.array([1,2,3,4,5,6,7,8,4,2,1,5,4,3])
# task: element is present or not
# Ans : we can use where() for that
x=np.where(a==4) #4 present in array or not
print(x) #return all index where 4 is present
y=np.where(a>2)
print(y)