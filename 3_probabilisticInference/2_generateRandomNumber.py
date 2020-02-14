import numpy as np
import matplotlib.pyplot as plt

# seed the random number generator
np.random.seed(42)

# initialise random_numbers, which is an empty array
random_numbers  = np.empty(100000)
# generate random number by looping over range(100000)

for i in range(100000):
    random_numbers[i]= np.random.random()

plt.hist(random_numbers)
plt.show()
