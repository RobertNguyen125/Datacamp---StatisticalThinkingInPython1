# ECDF: empirical cumulative distribution function
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

swing = pd.read_csv('/Users/apple/desktop/statisticsPython/dataset/2008_swing_states.csv', index_col='state')
print(swing.head())

x= np.sort(swing['dem_share']) # NOTE: x-axis is sorted data
# y-axis: evenly spaced data points with max of 1
# y = np.arange(1, len(x)+1)/len(x)
# print(len(x))
# plt.plot(x,y,marker='.', linestyle='none')
# plt.xlabel('% vote for Obama')
# plt.ylabel('ECDF')
# plt.margins(0.02) # keep data off plot edges
# plt.show()


# -------------------------------------------------------------------------
# plotting ECDF with iris dataset
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

def ecdf(data):
    n = len(data)
    x = np.sort(data)
    y = np.arange(1,1+n)/n
    return x,y

x_vers, y_vers = ecdf(versicolor_petal_length)
plt.plot(x_vers, y_vers, marker='.', linestyle='none')
plt.xlabel('length')
plt.ylabel('ECDF')

plt.show()
