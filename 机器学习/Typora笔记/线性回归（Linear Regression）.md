# 线性回归（Linear Regression）

### 计算方法：

##### 	1.最小二乘法

##### 	2.梯度下降法

```python
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += - (2 / N) * (y - (w_current*x + b_current))
        w_gradient += - (2 / N) * x * (y - (w_current*x + b_current))
    new_b = b_current - (b_gradient * learningRate)
    new_w = w_current - (w_gradient * learningRate)
   #梯度b : -2*(y-(wx+b))
   #梯度w : -2*x*(y-(wx+b))
    #同时两者求了每个点，还要 /总数N = float(len(points))
    #new_b = b_current - (b_gradient * learningRate)
    #一般的learningRate为1E-3
```



### 几种常见的下降法:

##### (I)bgd(批量梯度下降)：

即本次采用的方法



##### 	(II)sgd(随机梯度下降)

```python
np.random.shuffle(data)
for example in data:
		params_grad = evaluate_gradient(loss_function, example, params)
params = params - params_grad * learningRate
```

最大的缺点在于每次更新可能并不会按照正确的方向进行，但是也因此可以带来优化波动

由于波动，因此会使得迭代次数（学习次数）增多，即收敛速度变慢。不过最终其会和全量梯度下降算法一样，具有相同的收敛性



##### (III)Mbgd(小批量梯度下降)

```python
np.random.shuffle(data)
for batch in get_batches(data,batch_size=50)
```

Mini-batch 梯度下降综合了 batch 梯度下降与 stochastic 梯度下降，在每次更新速度与更新次数中间取得一个平衡，其每次更新从训练集中随机选择 m,m<n 个样本进行学习



### 优化算法：

##### 	(I)RMSprop



##### 	(II)Adam



### Non-linear Factor

##### 常见函数：

1.ReLu

 2.sigmoid