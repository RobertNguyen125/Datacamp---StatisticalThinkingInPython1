import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('/Users/apple/desktop/statisticsPython/dataset/iris.csv')

print(iris.head())
sns.set()
sns.boxplot(x='variety', y='petal.length', data=iris)
plt.xlabel('Species')
plt.ylabel('Length')
plt.show()
