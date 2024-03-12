import numpy as np
from sklearn.datasets import fetch_20newsgroups   #获取数据集
from sklearn.feature_extraction.text import TfidfVectorizer #TF-IDF文本特征提取

#常用的一些分类方法
from sklearn.naive_bayes import MultinomialNB #朴素贝叶斯
from sklearn.tree import DecisionTreeClassifier #决策树
from sklearn.neighbors import KNeighborsClassifier #K近邻
from sklearn.linear_model import LogisticRegression #逻辑回归
from sklearn.linear_model import SGDClassifier #随机梯度下降(适合稀疏矩阵)
from sklearn.ensemble import RandomForestClassifier #随机森林
from sklearn.ensemble import AdaBoostClassifier #AdaBoost

import time
t0=time.time()
print('计时开始')

#选取20个类中7种比较典型的类别进行实验
select = ['alt.atheism','comp.graphics','misc.forsale','rec.autos',
          'sci.crypt','soc.religion.christian','talk.politics.guns']
train=fetch_20newsgroups(subset='train',categories=select)
test=fetch_20newsgroups(subset='test',categories=select)

#train=fetch_20newsgroups(subset='train')
#test=fetch_20newsgroups(subset='test')

#将文章数据向量化（TF-IDF算法）
vectorizer = TfidfVectorizer() 
train_v=vectorizer.fit_transform(train.data)
test_v=vectorizer.transform(test.data)

Classifier_str = ['MultinomialNB()','DecisionTreeClassifier()','KNeighborsClassifier()',
              'LogisticRegression()','SGDClassifier()','RandomForestClassifier()','AdaBoostClassifier()']
for i in Classifier_str:
    t2=time.time()
    model = eval(i)
    model.fit(train_v,train.target)
    print('-------------------------------------')
    print(i)
    print('准确率为:',model.score(test_v,test.target))
    print('用时:%.6fs'%(time.time()-t2))
    print('-------------------------------------')
    #y_predict=model.predict(test_v)
    #print(np.mean(y_predict==test.target))
    
t1=time.time()
print('共计用时：%.2fs'%(t1-t0))   