import numpy as np

mat = np.array([[2, 1], [4, 5]])
eigenvalue, featurevector = np.linalg.eig(mat)

print("该矩阵特征值：\n", eigenvalue)
print("特征向量（对应列向量）：\n", featurevector)
