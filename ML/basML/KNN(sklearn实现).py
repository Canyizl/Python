from numpy import loadtxt
import numpy as np

with open('../data/wine.csv','r') as raw_data:
    data = loadtxt(raw_data,delimiter=',')

def normalization(row,column,x):
    result=np.empty([row, column])
    j = 0
    for j in range(column):
        result[: , j] = (x[: ,j] - np.mean(x[: , j])) / np.std(x[:, j])
    return result


X1 = data[:, 1:]
y1 = data[:, :1]
y = []
for i in y1:
    y.append(int(i))
X1_shape = X1.shape
X1_row = X1_shape[0]
X1_column = X1_shape[1]
X = normalization(X1_row, X1_column, X1)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=666)
from sklearn.neighbors import KNeighborsClassifier
best_score = 0
best_param = -1
for k in range(1,20):
    knn_sk = KNeighborsClassifier(n_neighbors=k)
    knn_sk.fit(X_train,y_train)
    y_predict = knn_sk.predict(X_test)
    from sklearn.metrics import accuracy_score
    score = accuracy_score(y_test,y_predict)
    if score > best_score :
        best_score = score
        best_param = k
print(best_score)
print(best_param)