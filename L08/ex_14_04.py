from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups

def naive_bayes():
    #1.读取数据
    news_data = fetch_20newsgroups(subset="all")
    #2.划分训练集，测试集
    x_train,x_test,y_train,y_test = train_test_split(news_data.data,news_data.target,test_size=0.25)
    #3.进行特征抽取
    tf = TfidfVectorizer()
    x_train = tf.fit_transform(x_train)
    x_test = tf.transform(x_test) #对测试集使用同样的均值、方差、最大最小值等指标进行变换，从而保证train、test处理方式相同。
    #4.进行朴素贝叶斯算法分类
    bayes = MultinomialNB(alpha=1.0)
    bayes.fit(x_train,y_train)
    y_predict = bayes.predict(x_test)
    #print("测试集的预测结果为：",y_predict)
    print("训练集的预测准确率为：",bayes.score(x_train,y_train))
    print("测试集的预测准确率为：",bayes.score(x_test,y_test))

if __name__ == '__main__':
    naive_bayes()