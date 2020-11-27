from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics
import numpy as np

X = datasets.load_iris()
data = X.data
target = X.target
name = X.target_names
x,y=datasets.load_iris(return_X_y=True)
print(x.shape,y.shape)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=100)
param = {'criterion':['gini'],'max_depth':[30,50,60,100],'min_samples_leaf':[2,3,5,10],'min_impurity_decrease':[0.1,0.2,0.5]}

grid = GridSearchCV(DecisionTreeClassifier(),param_grid=param,cv=6)
grid.fit(x_train,y_train)
print('最优分类器:',grid.best_params_,'最优分数:', grid.best_score_)  # 得到最优的参数和分值

clf = DecisionTreeClassifier(criterion='gini',max_depth=30,min_impurity_decrease=0.1, min_samples_leaf=10)
clf.fit(x_train,y_train)
y_predict = clf.predict(x_test)
print('训练集分数：', clf.score(x_train,y_train),'测试集分数',clf.score(x_test,y_test))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(list(range(len(x_test))),y_test,marker='*')
ax.scatter(list(range(len(x_test))),y_predict,marker='o')  # 不管是画散点图还是折现图，都会被挡住
plt.show()