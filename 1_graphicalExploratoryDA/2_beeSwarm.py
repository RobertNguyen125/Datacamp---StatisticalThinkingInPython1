# hist problem: looks different if the bins are different
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# swing = pd.read_csv('/Users/apple/desktop/statisticsPython/dataset/2008_swing_states.csv')
# print(swing.head())
# df_swing = swing[['state', 'county', 'dem_share']]
# _ = sns.swarmplot(x='state', y='dem_share', data=swing)
# _ = plt.xlabel('state')
# _ = plt.ylabel('percent of vote for Obama')
#
# plt.show()

# --------------------------------------------------------------------------------
iris = pd.read_csv('/Users/apple/desktop/statisticsPython/dataset/iris.csv')
print(iris.head())
sns.set()
sns.swarmplot(x='species',y='petal length (cm)', data=iris)
plt.xlabel('Species')
plt.ylabel('Petal length (cm)')
plt.show()
