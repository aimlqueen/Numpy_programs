# dot product
import numpy as np
# 1D matrix
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
c=np.dot(a,b)
print(c)
# Alternatively, you can use the @ operator for dot product
c_alt = a @ b

# 1 6
# 2 7
# 3 8
# 4 9
# 5 10

# 1×6+2×7+3×8+4×9+5×10
# =6+14+24+36+50
# =130

