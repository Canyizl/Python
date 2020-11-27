from sklearn.svm import SVC
import scipy.io as sio #简单的处理数据从mat中导入

#trainning data
trainData = sio.loadmat('./spamTrain.mat')
#Test data
testData = sio.loadmat('./spamTest.mat')

X,y=trainData['X'],trainData['y']
Xtest,ytest=testData['Xtest'],testData['ytest']

Cvalues = [3,10,30,0.1,0.03]
best_score = 0
best_param = 0

for c in Cvalues:
    svc = SVC(C=c,kernel='linear')
    svc.fit(X,y.flatten())
    score = svc.score(Xtest,ytest.flatten())
    if score > best_score:
        best_score = score
        best_param = c
print(best_score,best_param)

svc = SVC(0.03,kernel='linear') #代入最佳参数检测
svc.fit(X,y.flatten())
score_train = svc.score(X,y.flatten())
score_test= svc.score(Xtest,ytest.flatten())
print(score_train,score_test)