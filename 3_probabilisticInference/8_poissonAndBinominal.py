# You just heard that the Poisson distribution is a limit of the Binomial distribution for rare events.
# This makes sense if you think about the stories.
# Say we do a Bernoulli trial every minute for an hour, each with a success probability of 0.1.
# We would do 60 trials, and the number of successes is Binomially distributed, and we would expect to get about 6 successes.
# This is just like the Poisson story we discussed in the video, where we get on average 6 hits on a website per hour.
# So, the Poisson distribution with arrival rate equal to np approximates a Binomial distribution for n Bernoulli trials with probability p of success (with n large and p small).
# Importantly, the Poisson distribution is often simpler to work with because it has only one parameter instead of two for the Binomial distribution.

import numpy as np 
# Draw 10,000 samples out of Poisson distribution: samples_poisson
samples_poisson =np.random.poisson(10, size=10000)

# Print the mean and standard deviation
print('Poisson:     ', np.mean(samples_poisson),
                       np.std(samples_poisson))

# Specify values of n and p to consider for Binomial: n, p
n,p = [20,100,1000], [0.5,0.1,0.01]


# Draw 10,000 samples for each n,p pair: samples_binomial
for i in range(3):
    samples_binomial = np.random.binomial(n[i],p[i], size=10000)
# Print results
print('n =', n[i], 'Binom:', np.mean(samples_binomial),
                                 np.std(samples_binomial))
