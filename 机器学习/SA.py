from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math

def aimFun1(x):             #求解目标函数的最小值为何处
    y=x**3-60*x**2-4*x+6
    return y

def mnth(dy,T):             #模拟退火算法的降温、概率选取过程
    if dy<0:
        return 1
    else:
        p=math.exp(-(dy)/T)
        r=np.random.uniform(low=0,high=1)
        if r<p:
            return 1

T=1000          #设定开始温度
T_min=10        #设定结束温度
alpha=0.99      #本次采用指数式下降 也可用T=T(0)/1+t
count=0         #记步器，当次数过多且无法找到满意的值时，直接结束运行。本题在10000次范围内寻找。

x=np.random.uniform(low=0,high=100) #随机一个起点
y=aimFun1(x)

while T>=T_min:
    y=aimFun1(x)
    delta=np.random.uniform(low=-0.05,high=0.05)*T  #x扰动
    xNew=x+delta
    if xNew<0 or xNew>100:       #处理越界的情况
        xNew = x - delta
    yNew=aimFun1(xNew)
    dy=yNew-y
    if mnth(dy,T):
        x=xNew
    if dy<0:            #只在找到更小值时降温
        T=T*alpha
    count+=1
    if count>10000:
        break

print(x)
print(aimFun1(x))
print(count)
