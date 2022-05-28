import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

values  = np.random.uniform(-10, 10, 1000000)
plt.hist(values, 50)
plt.show()


x = np.arange(-3, 3, 0.001)
plt.plot(x, norm.pdf(x))