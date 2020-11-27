import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from IPython.display import Image
import pydotplus
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('../data/loan_data.txt',sep='\s+',encoding='utf-8',index_col='nameid')
print (data)

x = data.drop(['approve'],axis=1).values
print(x)
y = data['approve'].values
print(x.shape,y.shape)

# 划分训练集和测试集
x1 = x[:900]
y1 = y[:900]
x2 = x[900:]
y2 = y[900:]

# 在训练集中再划分出训练集和验证集
x_train,x_test,y_train,y_test = train_test_split(x1,y1,test_size=0.2)

# 生成决策树
clf = DecisionTreeClassifier() #默认树
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print('训练集评分:', clf.score(x_train,y_train))
print('验证集评分:', clf.score(x_test,y_test))
print('测试集评分', clf.score(x2,y2))
print("查准率：", metrics.precision_score(y_test,y_pred))
print('召回率:',metrics.recall_score(y_test,y_pred))
print('f1分数:', metrics.f1_score(y_test,y_pred))

# 混淆矩阵查看分类结果
print(confusion_matrix(y_true=y_test,y_pred=y_pred,labels=list(set(y))))
# 分类报告查看各类的评分
print(metrics.classification_report(y_test,y_pred,labels=list(set(y))))

param = {'max_depth': [5,10,20,30],'min_samples_leaf': np.arange(3,10,1),'min_impurity_decrease':np.linspace(0.01,0.4,10)}
clf = GridSearchCV(DecisionTreeClassifier(),param_grid=param,cv=8)
clf.fit(x_train,y_train)
print(clf.best_params_,clf.best_score_)

clf = DecisionTreeClassifier(max_depth=5, min_impurity_decrease=0.01, min_samples_leaf=3)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print('训练集评分:', clf.score(x_train,y_train))
print('验证集评分:', clf.score(x_test,y_test))
print('测试集评分', clf.score(x2,y2))
print("查准率：", metrics.precision_score(y_test,y_pred))
print('召回率:',metrics.recall_score(y_test,y_pred))
print('f1分数:', metrics.f1_score(y_test,y_pred))