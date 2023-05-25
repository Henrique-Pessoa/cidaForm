import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./aa.csv")
plt.scatter(data["Temperatura"],data["Produtividade"])
arr = []

arr.append(data["Temperatura"])
arr.append(data["Produtividade"])

print(np.corrcoef(arr))

plt.show()

