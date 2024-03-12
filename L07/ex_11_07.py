from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris_dataset = load_iris()
X_train,X_test,Y_train,Y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],shuffle=True,test_size=0.3)

# 数据标准化（通常对于Logistic回归是一个好的做法）
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 创建Logistic回归模型
clf = LogisticRegression(max_iter=1000)  # max_iter定义了求解算法的最大迭代次数

# 训练模型
clf.fit(X_train, Y_train)

# 进行预测
Y_pred = clf.predict(X_test)

# 计算和打印准确度
accuracy = accuracy_score(Y_test, Y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")