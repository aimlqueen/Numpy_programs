import numpy as np
a=np.array([6,2,1,9,5,4,3])
print(a)
# print result like iterate through each element
for i in a:
    print(i)
print("------------------")
a = np.array([[11, 2, 3], [4, -5, 6], [71, 8, 9]])
for i in a:
    for j in i:
        print(j)
print("---------------")

a = np.array([[[11, 2, 3], [4, -5, 6], [71, 8, 9]]])
for i in a:
    for j in i:
        for k in j:
            print(k)