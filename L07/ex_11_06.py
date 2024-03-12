from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()
X_train,X_test,Y_train,Y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],shuffle=True,test_size=0.3)

print('训练集shape:',X_train.shape)
print('测试集shape:',X_test.shape)
print(X_train[0:5])