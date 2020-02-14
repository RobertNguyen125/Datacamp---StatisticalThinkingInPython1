import numpy as np
import matplotlib.pyplot as plt
#
# Probability Mass Function: the set of probabilities of discreet outcome
# Rolling dice: the outcome is discreet because only certain value can be attained
# each result have the same/uniform probability (1/6). PMF the discreet uniform PMF

# No of r of successes in n Bernoulli trials with probability p of successes, is Binomially distributed
# the No r of heads in 4 coin flips with probability 0.5 of heads, is binomially distributed

print(np.random.binomial(4, 0.5))
print(np.random.binomial(4,0.5,size=10))

np.random.seed(42)
n_defaults = np.random.binomial(100,0.05,size=10000)
print(type(n_defaults))

def ecdf(data):
    n = len(data)
    x = np.sort(data)
    y = np.arange(1,1+n)/n
    return x,y
x,y = ecdf(n_defaults)
plt.plot(x,y, marker='.', linestyle='none')
plt.xlabel('No of defaults out of 100 loans')
plt.ylabel('CDF')
plt.show()
