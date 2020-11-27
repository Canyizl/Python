import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def sigmoid(n):
    result = 1/(1+np.exp(-n))
    return result

def initialize(dim):
    w = np.zeros((dim,1))
    b = 0
    return w,b

def propagate(w,b,X,y):
    m = X.shape[0] #m代表X的总个数
    A = sigmoid(np.dot(w.T,X)+b)
    cost = -(np.sum(y*np.log(A)+(1-y)*np.log(1-A)))/m
    dZ = A - y
    dw = (np.dot(X,dZ.T))/m
    db = (np.sum(dZ))/m
    grads = {'dw':dw,
             'db':db
            }
    return grads,cost

def optimize(w,b,X,y,lr,iterations=2000):
    costs = [] #定义一个cost数字，可以看迭代后的cost图
    for i in range (iterations):
        grads,cost = propagate(w,b,X,y)
        dw = grads['dw']
        db = grads['db']
        w = w - lr*dw
        b = b - lr*db
        if i % 100 == 0:
            costs.append(cost)
            print ('After iteration %i cost:%f'%(i,cost))
        params={
            'w':w,
            'b':b
        }
        grads={
            'dw':dw,
            'db':db
        }
    return params,grads,costs

def predict(w,b,X):
    m = X.shape[1]
    y_predict = np.zeros((1,m))
    A = sigmoid(np.dot(w.T,X)+b)
    for i in range(m):
        if A[0,i] > 0.5:
            y_predict[0,i]=1
        else:
            y_predict[0,i]=0
    return y_predict

def Logistic_model(X_train,y_train,X_test,y_test,lr=0.001,iterations=2000):
    dim = X_train.shape[0]
    w,b = initialize(dim)  #初始化w,b
    params,grads,cost = optimize(w,b,X_train,y_train,lr,iterations)
    w = params['w']
    b = params['b']
    train_predict = predict(w,b,X_train)
    test_predict = predict(w,b,X_test)
    accuracy_train = 1 - np.mean(np.abs(train_predict - y_train))
    accuracy_test = 1 - np.mean(np.abs(test_predict - y_test))
    print("Accuracy on train set:",accuracy_train )
    print("Accuracy on test set:",accuracy_test )

    d = {'cost':cost,'train_predict':train_predict,
         'w':w,'b':b,'lr':lr,'iterations':iterations,'train_acy':accuracy_train,
        }
    return d

def plot_data():
    plt.scatter(X1[:,0],X1[:,1],c=y1.flatten(),cmap='jet')
    plt.xlabel('x1')
    plt.ylabel('y1')
    plt.show()

#数据读取
import scipy.io as sio
data = sio.loadmat('./data/ex6data3.mat') #选取了之前某数据的前两行X特征，以及对应的Y值进行分类。
X1,y1=data['X'],data['y']
Xval,yval=data['Xval'],data['yval']

#plot_data()

X_train,y_train = X1[:,:2],np.array([y1.flatten()])
X_test,y_test = Xval[:,:2],np.array([yval.flatten()])
train_set_x_flatten = X_train.reshape(X_train.shape[0],-1).T
test_set_x_flatten = X_test.reshape(X_test.shape[0],-1).T

d = Logistic_model(train_set_x_flatten,y_train,test_set_x_flatten,y_test,lr=0.001,iterations=3000)