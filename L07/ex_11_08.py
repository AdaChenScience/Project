import numpy as np
from sklearn.datasets import load_iris

# 欧氏距离计算
def distEclud(x,y):
    return np.sqrt(np.sum((x-y)**2))

iris_dataset = load_iris()
data=iris_dataset.data

avg=np.average(data,axis=0)
print('平均值为:',avg)

distance=[distEclud(data[i],avg) for i in range(data.shape[0])]
print('前十个数据点到中心点的欧式距离为:',distance[0:10])