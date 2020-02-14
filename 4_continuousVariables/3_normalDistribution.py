import numpy as np
import matplotlib.pyplot as plt

belmont_no_outliers = [148.51, 146.65, 148.52, 150.7 , 150.42, 150.88, 151.57, 147.54,
       149.65, 148.74, 147.86, 148.75, 147.5 , 148.26, 149.71, 146.56,
       151.19, 147.88, 149.16, 148.82, 148.96, 152.02, 146.82, 149.97,
       146.13, 148.1 , 147.2 , 146.  , 146.4 , 148.2 , 149.8 , 147.  ,
       147.2 , 147.8 , 148.2 , 149.  , 149.8 , 148.6 , 146.8 , 149.6 ,
       149.  , 148.2 , 149.2 , 148.  , 150.4 , 148.8 , 147.2 , 148.8 ,
       149.6 , 148.4 , 148.4 , 150.2 , 148.8 , 149.2 , 149.2 , 148.4 ,
       150.2 , 146.6 , 149.8 , 149.  , 150.8 , 148.6 , 150.2 , 149.  ,
       148.6 , 150.2 , 148.2 , 149.4 , 150.8 , 150.2 , 152.2 , 148.2 ,
       149.2 , 151.  , 149.6 , 149.6 , 149.4 , 148.6 , 150.  , 150.6 ,
       149.2 , 152.6 , 152.8 , 149.6 , 151.6 , 152.8 , 153.2 , 152.4 ,
       152.2 ]
belmont_no_outliers = np.array(belmont_no_outliers)

np.random.seed(42)
# compute mean and std: mu, sigma
mean = np.mean(belmont_no_outliers)
sigma = np.std(belmont_no_outliers)

print(mean, sigma)

samples = np.random.normal(mean,sigma, size=10000)

def ecdf(data):
    n = len(data)
    x = np.sort(data)
    y = np.arange(1,1+n)/n
    return x,y

# get the cdf out of the samples and of data
x_theor, y_theor = ecdf(samples)
x,y = ecdf(belmont_no_outliers)

plt.plot(x_theor, y_theor)
plt.plot(x,y,marker='.', linestyle='none')
plt.xlabel('Belmont winning time(sec.)')
plt.ylabel("CDF")
plt.show()
