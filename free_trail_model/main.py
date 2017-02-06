
import numpy as np
import matplotlib.pyplot as plt
mu, sigma = 0, 0.1
V0 = 50
alpha = 0.9
T = 100
epsilon = np.random.normal(mu, [alpha**i*V0 for i in range(T)], T)
X0 = 10
X = [X0 + sum(epsilon[:i]) for i in range(T)]
plt.plot(X)
plt.show()
