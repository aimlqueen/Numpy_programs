
import numpy as np
a=np.array([[11,2,3],[4,-5,6],[71,8,9]])
b=np.max(a)
print(b)
c=np.min(a)
print(c)
# row wise max in 2D
b=np.max(a,axis=1)
print(b)
# col wise max in 2D
b=np.max(a,axis=0)
print(b)

print("-------------")
# Finding the index of the minimum value in the entire array
argmin_index = np.argmin(a)
print("Index of min value:", argmin_index)

# Finding the index of the maximum value in the entire array
argmax_index = np.argmax(a)
print("Index of max value:", argmax_index)

# Finding the index of the maximum value in each row
argmax_row_indices = np.argmax(a, axis=1)
print("Row-wise indices of max values:", argmax_row_indices)

# Finding the index of the maximum value in each column
argmax_col_indices = np.argmax(a, axis=0)
print("Column-wise indices of max values:", argmax_col_indices)