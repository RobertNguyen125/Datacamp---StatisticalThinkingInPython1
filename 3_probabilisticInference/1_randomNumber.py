# np.random.seed(): aka the pseudorandom number because it is because we manually put
# the seed for reproducibility

import numpy as np

# stimulate 4 coin flips
np.random.seed(42)
random_numbers = np.random.random(size=4) #4 flips
print(random_numbers) # NOTE: <0.5 means it is head| >0.5 for tail

head = random_numbers < 0.5
print(head)
# compute the number of heads by summing booleans (True=1, False=0)
print(np.sum(head)) # NOTE: the result is 1 -> 1 head

# Probability of getting 4 heads if we flip 4 times over again
n_all_heads = 0
for _ in range(10000):
    heads =np.random.random(size=4) < 0.5
    n_heads =np.sum(heads)
    if n_heads == 4:
        n_all_heads += 1

print(n_all_heads/10000)
