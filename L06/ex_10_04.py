import numpy as np

A = np.array([[2, 1], [4, 5]])
x = np.ones(A.shape[0])
for k in range(50): # 幂迭代，迭代次数为50
    x = A @ x
x = x / np.linalg.norm(x)
lambda1 = A @ x @ x / (x @ x) # 瑞利商
print('最大特征值为:',lambda1)