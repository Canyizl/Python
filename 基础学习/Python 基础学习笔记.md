# Python 基础学习笔记

### 1.基础语法

（包含和C++的对比，输入输出和调试中易错点）

##### 1.1 Python中没有++，--

##### 1.2 eval（）直接算出表达式的值

##### 1.3 用format可以控制输出精度,print中可以用'+'或者','控制多输出

```python
print(format(a,'.2f'),format(b,'.3f'))
```

##### 1.4 用end控制空格，用'\r'控制换行

```python
print(each,end=' ') #空格结尾
print('\r') #换行头输出
print('\n') #隔行输出
```

##### 1.5 for控制步长

```python
for i in range(2,n+1,2): #第三个参数控制步长
    pass
```

##### 1.6 定义函数

```python
def fun(n): #没有return默认无返回（返回NONE
    pass
```

##### 1.7 chr()实现ascii转换字符，ord（）实现字符转ascii

```python
i=chr(ord(i)+3) #i后移3位 如 A - > D
```

##### 1.8 反射方法提取对应的函数	

```python
if hasattr(test, p) :#hasattr(object, name)如果在object中含有name则返回true
resutl=getattr(test,p)#getattr(object, name[, default]) 返回一个对象的属性值
```

##### 1.9 数据可视化

```python
import matplotlib.pyplot as plt

def plot_data():
    plt.scatter(X[:,0],X[:,1],c = y.flatten(),cmap='jet') #X[:,0],X[:,1]表示绘制散点图的数据点 c表示的是颜色，cmapcmap仅仅当c是一个浮点数数组的时候才使用（colormap）
    plt.xlabel('x1')
    plt.ylabel('y1')
```



### 2.Numpy库相关

##### 2.1 随机的uniform为两边闭区间

```python
x=np.random.uniform(low=1,high=2) #[1,2]
```

##### 2.2 flatten()函数

flatten只能适用于numpy对象，即array或者mat，普通的list列表不适用！

a.flatten()：a是个数组，a.flatten()就是把a降到一维，默认是按行的方向降 。

##### 2.3 numpy的特殊取法

[:, m:n]，即取所有数据的第m到n-1列数据，含左不含右

[:,n]就是取所有集合的第n个数据

[:,m:n]即取所有数据集的第m到n-1列数据

##### 2.4 numpy的标准差和均值

np.mean()是用来计算均值，np.std()是用来计算标准差

```python
from sklearn.preprocessing import StandardScaler
StandardScaler()
```

##### 2.5 argsort（）函数

```python
import numpy as np
x = np.array([1,4,3,-1,6,9])
x.argsort()
# array([3, 0, 1, 2, 4, 5], dtype=int64)
```

argsort()是将X中的元素从小到大排序后，提取对应的索引index，然后输出

##### 2.6 loadtxt()函数

```python
from numpy import loadtxt
```

对于CSV文件，读取后的数据为['1,5'  '2,4' ],用‘,’分割其中的每行数据。而参数delimiter=',' 可以指定数据的分隔符。

##### 2.7 np.random.shuffle

重新排序返回一个随机序列作用类似洗牌。

##### 2.8 np.arange()

 np.arange()函数返回一个有终点和起点的固定步长的排列，如[1,2,3,4,5]，起点是1，终点是5，步长为1。

三个参数时，第一个参数为起点，第二个参数为终点，第三个参数为步长。其中步长支持小数。

##### 2.9 shape和reshape

shape是查看数据有多少行多少列
reshape()是数组array中的方法，作用是将数据重新组织

```python
shape[0] #矩阵的行 个体个数
shape[1] #矩阵的列 特征数
numpy.arange(n).reshape(a, b)    
#依次生成n个自然数，并且以a行b列的数组形式显示
reshape(m,-1) #改变维度为m行、1列
reshape(-1,m) #改变维度为1行、m列
#-1 也可以代表自动计算，即不给出相应的值
```

##### 2.10 cumprod()函数

```python
    a = np.array([1,2,3],[4,5,6]])
    >>>a.cumsum(0)
    array([[1,2,3],
         [5,7,9]])
 	>>>a.cumprod(1)
    array([[1,2,6],
        [4,20,120]])
```

0代表列的计算，1代表行的计算，即对列和行分别累积求和、 积。

而且其结果不聚合，产生的是中间数组。

##### 2.11 logspace()函数

```python
#np.logspace(start=开始值，stop=结束值，num=元素个数，base=指定对数的底, endpoint=是否包含结束值)创建等比数列

```

##### 2.12 random.randn()和rand()

```python
#np.random.rand()返回一个或一组服从“0~1”均匀分布的随机样本值。随机样本取值范围是[0,1)，不包括1

#np.random.randn(d0,d1,d2……dn) 
#1)当函数括号内没有参数时，则返回一个浮点数； 
#2）当函数括号内有一个参数时，则返回秩为1的数组，不能表示向量和矩阵； 
#3）当函数括号内有两个及以上参数时，则返回对应维度的数组，能表示向量或矩阵； 
#本函数可以返回一个或一组服从标准正态分布的随机样本值。添加一个高斯噪声
```



### 3.sklearn相关

##### 3.1 train_test_split()函数

```python
from sklearn.model_selection import train_test_split
train_X,test_X,train_y,test_y = train_test_split(train_data,train_target,test_size=0.3,random_state=5)
#train_data 待划分样本数据
#train_target 待划分的标签
#test_size 测试数据比例 默认为0.75 也可150代表test数据有150个
#random_state 设置随机数种子，保证每次都是同一个随机数。若为0或不填，则每次得到数据都不一样
```

##### 3.2 KNeighborsClassifier()函数

```python
from sklearn.neighbors import KNeighborsClassifier
class sklearn.neighbors.KNeighborsClassifier(n_neighbors=5, weights=’uniform’, algorithm=’auto’, leaf_size=30, 
p=2, metric=’minkowski’,metric_params=None, n_jobs=None, **kwargs)
#n_neighbors:int,默认值是5 即为k值
#weight： 'uniform'表示权重相同 'distance'表示权重是距离的倒数，越近影响越大
#algorithm： 计算找出k的算法
#leaf_size： int 默认30
#p: int 默认为2	1：曼哈顿距离	2:欧式距离
#其他一般不设置
```

##### 3.3 accuracy_score()函数

```python
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_predict)
#accuracy_score比较容易理解，但是它不能告诉你响应值的潜在分布，并且它也不能告诉你分类器犯错的类型。
```

##### 3.4 GridSearchCV 交叉验证

```python
from sklearn.model_selection import GridSearchCV
lasso_model = GridSearchCV(model,param_grid={'alpha':alpha_can},cv=5) #cv=5 5折的交叉验证
```

##### 3.5 Polynomialfeatures()

```python
#进行特征的构造,使用多项式的方法来进行的，如果有a，b两个特征，那么它的2次多项式为（1,a,b,a^2,ab, b^2）
```

##### 3.6 LogisticRegression

```python
LogisticRegression(penalty='l2',  C=1.0)
#penalty 惩罚项 可以为l1\l2
#C 正则化系数。越小则正则化越强。
```

##### 3.7 LabelEncoder 文本标签数字化

```python
from sklearn.preprocessing import LabelEncoder
#将文本标签转化为数字
le = preprocessing.LabelEncoder()
le.fit(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
print (le.classes_)
y = le.transform(y)
print ('Last Version, y = \n', y)
```

##### 3.8 StandardScaler() 

```python
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
StandardScaler()
#计算训练集的平均值和标准差
```

##### 3.9 predict()与predict_proba()

```python
#predict是训练后返回预测结果，是标签值。
#predict_proba返回的是一个 n 行 k 列的数组， 第 i 行 第 j 列上的数值是模型预测 第 i 个预测样本为某个标签的概率，并且每一行的概率和为1。
```

##### 3.10  DecisionTreeClassifier(),DecisionTreeRegressor()

```python
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
model = DecisionTreeClassifier(criterion='entropy')
dt = DecisionTreeRegressor(criterion='mse')
#默认为熵，也可以用gini。
#还有参数max_depth,min_samples_split(如果该结点包含的样本数目大于base,则有可能对其分支)、min_samples_leaf(若将该结点分支后，得到的每个子节点样本数目都大于base,则完成分支，不然不再分。).
```



### 4.其他机器学习相关函数记录

##### 4.1 Counter对象、common函数

```python
from collections import Counter

# most_common(n) 按照counter的计数，按照降序，返回前n项组成的list; n忽略时返回全部
Counter('abracadabra').most_common(3)
[('a', 5), ('r', 2), ('b', 2)]

a = [1,4,2,3,2,3,4,2]  
print Counter(a)  
Counter({2: 3, 3: 2, 4: 2, 1: 1})
```

用于KNN底层实现中，统计最多的Neighbors。



##### 4.2 pandas的read_csv(最简单的方式)

```python
import pandas as pd
data = pd.read_csv('Advertising.csv')
#sep='\s+',encoding='utf-8' 可用于txt文件
```



##### 4.3 pandas的 .drop()

```python
frame.drop(['a'])
frame.drop(['Ohio'], axis = 1)
#drop函数默认删除行，列需要加axis = 1
```

 