import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt


x = np.linspace(0,1,100)
n = len(x)

def k(x,y):
    d = x - y
    return np.exp(-100*LA.norm(d)**2)

C = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        C[i,j] = k(x[i],x[j])

u = np.random.randn(n)

U, s, V = LA.svd(C, full_matrices=True)

z = np.dot(np.dot(U,np.diag(np.sqrt(s))),u)
m = 30 - 10*(x-0.5)*(x - 0.5)
plt.plot(x,m+z,x,m)
plt.show()
