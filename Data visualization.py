import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/home/keldendraduldorji/Desktop/K.csv', engine='python')
#df = pd.DataFrame(d, columns=['Name', 'Age', 'Program'])
sns.pointplot(x='Name',y='EnrolNo', data=df)
plt.show()