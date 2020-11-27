# 					A2CL-PT

### Abstract

​	one triplet is used to learn discriminative features for each activity class, 

​	and the other one is used to distinguish the features where no activity occurs (i.e. background features) from activity-related features for each video.

### Introduction

​	Our method is built on two triplets of vectors of the feature space, and one of them is designed to distinguish background portions from the activity-related parts of a video.

​	 inspired by the angular triplet-center loss (ATCL) [10] originally designed for multi-view 3D shape retrieval.



#### Method

##### 3.1 Feature embedding

N training videos:  ${v_1}$

video-level: $y_i(j) = 1$ when the activity class $j$ is present 
$l_i$ denotes the temporal length of the feature of the video  $v_i$



##### 3.5 Classification and Localization

​	





### Code 

main: num_class 给定

 			len_features 给定

ACLPTLoss：margin1=2,margin2=1 

​							centers1,2

detection: detect_segments s,e 



### Weakly supervised



### Plus

​	Optical Flow 灰度瞬时变化率——光流矢量

​	CAS (Class Activation Sequence)

​	T-CAM (Temporal Class Activation Map)