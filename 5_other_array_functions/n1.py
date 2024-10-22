# round,floor,ceil
# 4X4 matrix with all elements are floating point num
import numpy as np
arr = np.array([[1.1, 2.5, 3.7],[4.3, 5.9, 6.1],[7.8, 8.3, 9.9]])
# Rounding
rounded = np.round(arr)
print("Rounded:\n", rounded)

# Floor
floored = np.floor(arr)
print("Floored:\n", floored)

# Ceiling
ceiled = np.ceil(arr)
print("Ceiled:\n", ceiled)