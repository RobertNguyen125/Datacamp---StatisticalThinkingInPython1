import matplotlib.pyplot as plt
import numpy as np

# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
samples_std1 = np.random.normal(20,1,size=100000)
samples_std3 = np.random.normal(20,3,size=100000)
samples_std10 = np.random.normal(20,10,size=100000)

# plot histogram for each of the sample
plt.hist(samples_std1, bins=100,density=True, histtype='step')
plt.hist(samples_std3, bins=100,density=True, histtype='step')
plt.hist(samples_std10, bins=100,density=True, histtype='step')
plt.legend(('std=1','std=3','std=10'))
plt.ylim(-0.01,0.42)
plt.show()