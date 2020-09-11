# KNN算法

有监督学习中的分类算法

### 1.KNN的原理：

当预测一个新的值x的时候，根据它距离最近的K个点是什么类别来判断x属于哪个类别。（K Nearest Neighbors）



### 2.计算

#### 	2.1 点距离的计算

通常KNN算法中使用的是欧式距离

d(x,y)=√∑ (xi-yi)^2



#### 	2.2 K值选择

通过交叉验证，从选取一个较小的K值开始，不断增加K的值，然后计算验证集合的方差，最终找到一个比较合适的K值。



##### 后记:

底层实现中第一次调试失败原因：

```python
d = sqrt(np.sum((x_train - x)**2)) 
# d² = (x1)²+(x2)²+···· 此为正确解
d = sqrt(np.sum(x_train - x) ** 2)
#相差一个括号 d² = (x1+x2+····)² 导致严重偏差
```



使用sklearn来简单实现KNN算法：

主要函数：

1. train_test_split() 随机划分样本数据为训练集和测试集
2. KNeighborsClassifier(n_neighbors=6) KNN预测函数并确定k
3. knn_sk.fit() 进行样本训练
4. accuracy_score() 输出预测率