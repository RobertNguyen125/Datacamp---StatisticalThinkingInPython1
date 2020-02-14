# Bernoulli trial as a flip of a possibly biased coin. Specifically, each coin flip has a
# probability p of landing heads (success) and probability 1−p of landing tails (failure).
import numpy as np
import matplotlib.pyplot as plt
def perform_bernoulli_trial(n,p):
    n_success = 0
    for i in range (n):
        random_numbers = np.random.random()
        if random_numbers < p:
            n_success+=1
    return n_success

# Bank have 100 mortgages and some will default, the probability of default is p =0.05
np.random.seed(42)
#initialise the number of default
n_defaults = np.empty(1000) # this is an array with 1000 empty slots
# compute the number of default
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trial(100,0.05)

plt.hist(n_defaults, normed=True)
plt.xlabel('No of default out of 100 loans')
plt.ylabel('Probability')
plt.show()
