import os
import numpy as np

dane = np.genfromtxt(os.path.join(os.getcwd(), 'data', 'sample.csv'), delimiter=' ')

mean = np.mean(dane, axis=0)
median = np.median(dane, axis=0)
std = np.std(dane, axis=0)

print(mean)
print(median)
print(std)

