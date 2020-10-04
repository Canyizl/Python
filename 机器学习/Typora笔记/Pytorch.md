# Pytorch

### 构建网络模型

##### 1.权重参数初始化

（前向传播）

##### 	2.计算隐层

##### 	3.加入激活函数

##### 	4.预测结果

##### 	5.通计算损失

##### 6.打印损失值

##### 7.反向传播计算

##### 8.更新参数

##### 9.每次迭代后清空



### Mnist 分类任务

##### 网络基本构建与训练方法，常用函数解析

##### torch.nn.function模块

##### nn.Module模块

​	**torch.nn.functional 很多层和函数在这里都会见到**

 那么什么时候用nn.Module,什么时候用nn.functional呢？一般情况下，如果模型有可学习的参数，最好用nn.Module,其他用nn.functional相对更简单

​	**创建一个model来更简化代码**

必须继承nn.Module且在其构造函数中需要调用nn.Module的构造函数

无需写反向传播函数，nn.Module能够利用autograd自动实现

Module中的可学习参数可以通过named_parameters()或者parameters()返回迭代器

​	**用TensorDataset和DataLoader来简化**

```python
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
```

一般在训练时候加上model.train(),正常使用BatchNorm && Dropout

测试时候一般选择model.eval(),这样就不会使用



### 卷积神经网络

作用：分类与检索



##### Dropout

随机扔掉一定比例的神经元

​	在训练数据上防止了单元之间共同起作用

​	隐层的单元不再依赖于其他单元

​	迫使每一个单元学习到有效的特征

##### Pooling(池化)

​	降低输出规模、增加可解释性

​	光滑数据、避免丢失过多信息

​	Max Pooling/Min/Mean/Random

##### BN

Batch Normalization



##### 卷积网络一般架构

数据---->数据规则化、核卷积、非线性映射/激励、池化---->数据规则化、 核卷积、非线性映射/激励、池化----->全连接----->分类器

规则化：白化、去均值

卷积：维度提升、过完备基

非线性映射：稀疏化、边界消除

pooling：特征聚集、降维、光滑



##### 卷积层涉及参数：

​	滑动窗口步长

​	卷积核尺寸

​	边缘填充

​	卷积核个数

卷积结果计算公式：

 H2 = （H - F + 2P）/ S + 1

H为原图长度，F为卷积核的长度，P为边缘0的行数，S为步长



##### 经典网络

Alexnet