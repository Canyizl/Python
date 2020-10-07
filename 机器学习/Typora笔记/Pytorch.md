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

Alexnet 2012

Vgg 2014 : pooling后损失信息，pooling后翻倍来弥补损失

Resnet 2015 (首选)

plus：感受野



### 卷积网络模块构建

一般 卷积层+relu层，池化层可以写成一个套餐

注意卷积最后结果还是一个特征图，需要把图转换成向量才能做分类或者回归任务。



### 基于经典网络架构训练图像分类模型

##### torchvision

##### 数据预处理部分:

​	数据增强: torchvision中transforms模块自带功能，比较实用

​	数据预处理： torchvision中transforms也帮我们实现好了，直接调用即可

​	DataLoader模块之间读取batch数据

##### 网络模块设置：

​	加载预训练模型，torchvision中有很多经典网络架构，可以用人家训练好的权重参数来继续训练，也就是所谓的迁移学习。

​	需要注意的是别人训练好的任务不同，需要把最后的head层改一改，一般也就是最后的全连接层，改成我们自己的任务。

​	训练时可以全部重头训练，也可以只训练最后我们任务的层，因为前几层都是做特征提取的，本质任务目标相同。

##### 网络模型保存与测试：

​	模型保存的时候可以带有选择性，例如在验证集中如果当前效果好则保存

​	读取模型进行实际测试

##### Data Augmentation 数据增强的作用：

​	对图像做翻转、旋转、缩放等操作，更高效地利用数据。

制作好数据源：

​	data_transforms中指定了所有图像预处理操作

​	imageFolder假设所有的文件按文件夹保存好，每个文件夹下存储同一类别的图片，文件夹的名字为分类的名字。

```python
data_transforms = {
	'train': transforms.Compose([transforms.RandomRotation(45), #随机选择，-45到45度之间随机选
   transforms.CenterCrop(224), #从中心开始裁剪 224*224
   transforms.RandomHorizontalFlip(p=0.5), #随机水平翻转 选择一个概率
   transforms.RandomVerticalFlip(p=0.5) #随机垂直翻转
  transforms.ColorJitter(brightness=0.2,contrast=0.1,saturation=0.1,hue=0.1), #参数1为亮度，参数2为对比度，参数3为饱和度，参数4为色相。
   transforms.RandomGrayscale(p=0.025) #概率转换成灰度率                              
   transforms.ToTensor(),
   transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225]) #均值，标准差
   ]),
    'valid': transforms.Compose([transforms.Resize(256),
transforms.CenterCrop(224),                           transforms.ToTensor(),
transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
  ]),
}
```

