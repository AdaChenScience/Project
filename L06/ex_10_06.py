import numpy as np

mat = np.array([[1,-1,4], [2,1,3], [1,3,-1]]).transpose() #数据为三个行向量
C = np.cov(mat)

A = C
x = np.ones(A.shape[0])
for k in range(50): # 幂迭代，迭代次数为50
    x = A @ x
x = x / np.linalg.norm(x)
lambda1 = A @ x @ x / (x @ x) # 瑞利商
print('最大特征值为:',lambda1)
print('对应特征向量为:',x)
