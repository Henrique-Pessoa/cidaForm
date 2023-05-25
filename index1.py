import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./dados_imposto_empresas.csv")

sns.countplot(data=data,x='Imposto')



plt.show()