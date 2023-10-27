import random
import numpy as np

def f(x): return 9*x+8

X=np.linspace(0,10,30)
Y=[f(i) for i in X]+np.random.normal(0,1,30)

print(X)
print(Y)