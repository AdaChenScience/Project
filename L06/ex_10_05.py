import numpy as np

mat = np.array([[1,-1,4], [2,1,3], [1,3,-1]]).transpose() #数据为三个行向量
C = np.cov(mat)
print(C)