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



### 3.sklearn相关

##### 3.1 train_test_split()函数

```python
from sklearn.model_selection import train_test_split
train_X,test_X,train_y,test_y = train_test_split(train_data,train_target,test_size=0.3,random_state=5)
#train_data 待划分样本数据
#train_target 待划分的标签
#test_size 测试数据比例
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