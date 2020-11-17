# Opencv

http://codec.wang/#/opencv/

##### 1.cv2.waitKey(0)卡死

添加:cv2.destroyAllWindows()

##### 2.打开摄像头

cv2.VideoCapture(0)

##### 3.鼠标绘图

cv2.setMouseCallback()

回调函数 def mouse_event(event,x,y,flags,param)

##### 4.二阶算子Laplacian

laplacian = cv2.Laplacian(img, -1)  # 使用Laplacian算子

##### 5.Canny边缘检测

edges = cv2.Canny(img, 30, 70)  # canny边缘检测

##### 6.形态学

开/闭运算 cv2.morphologyEx()

```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 定义结构元素

img = cv2.imread('j_noise_out.bmp', 0)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  # 开运算

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  # 闭运算
```

形态学梯度：膨胀图减去腐蚀图，这样会得到物体的轮廓：

```python
img = cv2.imread('school.bmp', 0)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
```



## 网课

##### 1.图像基本操作

##### 2.图像阈值