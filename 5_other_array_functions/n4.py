# arg sort
import numpy as np
a=np.array([11,21,3,14,5,6,7,8,9])
print(a) #[11 21  3 14  5  6  7  8  9]
b=np.sort(a)
print(b) #[ 3  5  6  7  8  9 11 14 21]
c=np.argsort(a)
print(c) #[2 4 5 6 7 8 0 3 1]

