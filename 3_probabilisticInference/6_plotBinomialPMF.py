import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n_defaults = np.random.binomial(100,0.05,size=10000)

bins = np.arange(min(n_defaults), max(n_defaults)+1.5)-0.5
plt.hist(n_defaults, normed=True, bins=bins)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
