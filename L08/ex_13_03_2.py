import sklearn.datasets as datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

feature = iris['data']  
target = iris['target']  
x_train, x_test, y_train, y_test = train_test_split(feature, target, test_size=0.2, shuffle=True) 

knn = KNeighborsClassifier(n_neighbors=3) 
knn = knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)
y_true = y_test
print('knn分类结果:', y_pred)
print('实际分类结果:', y_true)
print(knn.score(x_test, y_test))