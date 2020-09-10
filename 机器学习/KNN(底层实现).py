import numpy as np
from numpy import loadtxt
from math import sqrt
from collections import Counter

def normalization (row, column, arr):       #数据归一化(本题采用Z标准化)
    result = np.empty([row, column])
    j = 0
    for j in range(column):
        result[:, j] = (arr[:, j]-np.mean(arr[:, j])) / np.std(arr[:, j]) #Z标准化： x-均值 / 标准差
    return result

def KNN (k, X_train, y_train, x):
    distances=[]
    for x_train in X_train:
        d = sqrt(np.sum((x_train - x)**2))
        distances.append(d)
    np.argsort(distances)
    nearest = np.argsort(distances)
    topK_y=[y_train[i] for i in nearest[:k]]
    votes = Counter(topK_y)
    votes.most_common(1)[0][0] #most_common(1)输出第一多的编号和次数，[0][0]则选中了数，此处即种类编号
    return votes.most_common(1)[0][0] #取为预测值

#文件读取
with open('../data/wine.csv','r',encoding='UTF-8') as raw_data:
    data = loadtxt(raw_data,delimiter=',')

#数据处理
X1=data[:, 1:]
y1=data[:, :1] #第0行即首行为种类，单独处理成y
y=[]
for i in y1:
    y.append(int(i))
all_index = np.random.permutation(len(X1)) #随机取样 此处取随机索引
test_rate = 0.3                           #测试比例划分为7:3
test_size = int(len(X1)*test_rate)

X1_shape = X1.shape
X1_row = X1_shape[0]   #X1的行(row)，代表X的个数
X1_column = X1_shape[1]   #X1的列(column)，代表单个X的特征值
X = normalization(X1_row, X1_column, X1) #处理完毕的值放进X中进行下一步

#底层实现
test_index = all_index[:test_size]    #测试的索引
train_index = all_index[test_size:]   #训练的索引

X_train = np.array(X)[train_index]    #对于测试数据X，根据索引构造X_train
y_train = np.array(y)[train_index]
X_test = np.array(X)[test_index]
y_test = np.array(y)[test_index]

y_predict = [KNN(6, X_train, y_train, x) for x in X_test]
np.array(y_predict)
true = np.sum(y_predict == y_test)/len(y_test) #正确率
print('预测正确率为：',true)