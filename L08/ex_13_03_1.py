import numpy as np
import pandas as pd
import math
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 读取数据集
def read_data():
    iris = load_iris()
    #col是列名
    col = list(iris["feature_names"])
    #在iris数据集中，标签在"data"数组里，标记在"target"数组里
    m1 = pd.DataFrame(iris.data,index=range(150),columns=col)
    m2 = pd.DataFrame(iris.target,index=range(150),columns=["class"])
    #将上述两张DataFrame表连接起来，how是DataFrame参数，可以不写，这里用外连接。不清楚外连接的可以看下SQL语句
    iris = m1.join(m2,how='outer')
    return iris

# 划分数据集
def data_split(iris, test_ratio):
    n=len(iris)
    index=np.random.permutation(n)
    index=index[0:int(n*test_ratio)]
    Test = iris.take(index)
    Train = iris.drop(index)
    datasets = [Test, Train]
    return datasets

# KNN算法
def KNN(Train, Test, GT, k):
    Train_num = Train.shape[0]
    tests = np.tile(Test, (Train_num, 1)) - Train
    distance = (tests ** 2) ** 0.5
    result = distance.sum(axis=1)
    results = result.argsort()
    label = []
    for i in range(k):
        label.append(GT[results[i]])
    return label

def cross_define_K(Train, Test, GT):
    precision = []

    for k in range(1,50):
        #print(k)
        true = 0
        for i in Test:
            Test1 = [i[0],i[1],i[2],i[3]]
            result = KNN(Train,Test1,GT,k)
            collection = Counter(result)
            result = collection.most_common(1)
            if result[0][0] == i[4]:
                true += 1
        success = true / len(Test)
        precision.append(success)

    k1 = range(1,50)
    plt.plot(k1,precision,label='line1',color='g',marker='.',markerfacecolor='pink',markersize=10)
    plt.xlabel('K')
    plt.ylabel('Precision')
    plt.title('KNN')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # 读取iris数据集
    iris = read_data()
    # 对数据集进行划分（训练集，测试集）
    datasets = data_split(iris,0.2)
    
    # 将训练集的GT隐去
    Train = datasets[1].drop(columns=['class']).values
    # 读取训练集的GT
    GT = datasets[1]['class'].values
    # 读取测试集
    Test = datasets[0].values

    cross_define_K(Train,Test,GT)
    # 设置KNN的k值
    k = 3

    true = 0
    for i in Test:
        Test = [i[0],i[1],i[2],i[3]]
        result = KNN(Train,Test,GT,k)
        
        # KNN返回的是测试数据与训练数据相近的n个预测值
        collection = Counter(result)
        result = collection.most_common(1)
        #print(result[0][0])

        # 选取其中出现最多的结果进行验证
        if result[0][0] == i[4]:
            true += 1
    
    success = true/len(datasets[0])
    print('success:',success)