import numpy as np
from sklearn.linear_model import LinearRegression

def f(x): return 9*x+8

X=np.linspace(0,10,30)
Y=[f(i) for i in X]+np.random.normal(0,1,30)
print(type(X),type(Y))

model=LinearRegression()
model.fit(X.reshape(-1,1),Y)
print(model.coef_)
print(model.intercept_)