import numpy as np


x = [6,8,6,10,8,15,12,14,12,16]
y = [8,8,12,12,16,16,20,20,24,24]

arr = []

arr.append(x)
arr.append(y)
corr = np.corrcoef(arr)
print(corr)
