import numpy as np
import matplotlib.pyplot as plt


x = [40,60,80,100,120,140,160]
y=[15.9,18.8,21.6,25.2,28.7,30.4,30.7]

arr = []
arr.append(x)
arr.append(y)

corr = np.corrcoef(arr)
print(corr)

plt.scatter(x,y)

plt.show()