# plot histogram of irish dataset
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

iris = pd.read_csv('/Users/apple/desktop/statisticsPython/dataset/iris.csv')
print(iris.head())

versicolor_petal_length = [4.7, 4.5, 4.9, 4. , 4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4. ,
       4.7, 3.6, 4.4, 4.5, 4.1, 4.5, 3.9, 4.8, 4. , 4.9, 4.7, 4.3, 4.4,
       4.8, 5. , 4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5, 4.7, 4.4, 4.1,
       4. , 4.4, 4.6, 4. , 3.3, 4.2, 4.2, 4.2, 4.3, 3. , 4.1]
versicolor_petal_length = np.array(versicolor_petal_length)
# set the style of graph
sns.set()
# Adjusting No of bins: the rule is the square root of No of samples
# compute datapoint:
n_data =len(versicolor_petal_length)
# compute No of bins:
n_bins = np.sqrt(n_data)
n_bins =int(n_bins)
plt.hist(versicolor_petal_length,bins=n_bins)
plt.xlabel('petal length (cm)')
plt.ylabel('count')
plt.show()
