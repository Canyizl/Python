# Yolo

##### YOLO-V1 核心思想:

​	conv + 7X7X30

​	30----> 5+5+20

​	5: (x,y,w,h),c

​	x,y:中心点	w,h: 宽度和高度	 c：自信度

​	5: 有两种框（一个横向一个纵向）

​	20：20类物体

##### YOLO-V2-聚类提取先验框：

​	faster-rcnn系列选择的先验比例都是常规的，不一定完全符合数据集。

##### YOLO-V3：

​	核心网络架构：

​			没有池化和全连接层，全部卷积

​			下采样通过stride为2实现

​			3种scale，更多先验框

​			基本上当下经典做法全融入了

```python
#https://github.com/AlexeyAB/darknet
#作者Git	
```



##### 相关误差标准

IOU：交区域和并区域的比值

TP ：True positives

TN :  True Negatives

FP :  False Positives	

FN:  False Negatives

Precision : TP / (TP+FP)

Recall: TP / (TP+FN)

AP: 利用不同的Precision和Recall的点的组合，画出来的曲线下面的面积。