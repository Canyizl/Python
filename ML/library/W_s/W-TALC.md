# W-TALC

## 知乎:

### [1](https://zhuanlan.zhihu.com/p/40393800) 基于弱监督的视频时序动作检测的介绍

**“视频时序动作检测”**是指在可能包含一个或多个动作片段的未剪辑长视频中，定位出这些动作片段的起止时间，并指出片段具体属于哪一类动作。



**弱监督”**则是指训练集中只标记整段视频包含的动作类别，并没有片段级别的时间信息。

【[3](https://zhuanlan.zhihu.com/p/50943824)】Temporal Class Activation Maps（T-CAM）：是CAM的时序版本，训练阶段比较简单，就是将视频均分为N个segment，使用I3D提取特征，并经过attention module（注意力模块），再经过Sigmoid后变为0-1之间，最后能够得出每个片段在预测分类标签过程中的重要程度，并通过计算T-CAM得到动作发生的时间片段。



【7】W-TALC：另一个是co-activity similarity loss，在特征空间上驱使同类动作的视频片段尽可能近一些，不同类的相对远一些——用了一个ranking hinge loss来实现。





### [2](https://zhuanlan.zhihu.com/p/148782835) Reading: Weakly Temporal Action Localization

[PS](https://zhuanlan.zhihu.com/p/148782835)：个人觉得，针对W-TAL任务，最主要的问题有俩，第一是把时间域上的行为“前景帧”和“背景帧”区分开来，那怎么区分开呢？这就得学到前景帧的良好表达（基于Deep learning的算法，分类器就是MLP，可以略过不谈）; 第二就proposal的选择了，你在数据处理的时候没有提过哪些是前景哪些是背景，那就不好学习前景的表达啊。



1.在提取长视频的proposal/segments/snippets时，根据光流或者镜头的切换来抽帧，然后还可以生成一个新的背景类别来指导训练。2. 在特征或者行为分数后面给所有proposal的分数加一个attention score, attention越大，其是前景的置信度就越大。3. 采用度量学习+多实例学习的方法，学习行为前景帧更加判别性的表达。如果解决了时域上行为前景和背景的区分问题，那么这个W-TAL的任务也就能迎刃而解了吧。