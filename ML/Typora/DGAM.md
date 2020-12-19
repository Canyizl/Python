# 						DGAM



### Abstract

​	'What to solve' : **action-context**<sup><a href="#ref1">1</a></sup> confusion issue is common in WSAL

​	'model':  the **class-agnostic**<sup><a href="#ref1">2</a></sup> frame-wise frame attention using **CVAE**<sup><a href="#ref1">3</a></sup>  

​	running on THUMOS14

### Introduction

​	The extracted feature representations for context and action are also different. Such difference exists regardless of the action category.

​	 Generative attention mechanism to model the frame representation conditioned on frame attention. 

​	Our framework thus consists of two parts: the Discriminative and Generative Attention Modeling (DGAM). 

1. the discriminative attention modeling trains a classification model on temporally pooled features weighted by the frame attention.
2. a generative model CVAE, is learned to model the class-agnostic frame-wise distribution of representation conditioned on attention values. 

### Related Works





![DGAM](C:\Users\Administrator\Desktop\导师\for now 11 15\typora\DGAM.png)



Feature  extraction : I3D



### Conclusion



### References:

[1].<span name = "ref2">Context frames near action clips tend to be recognized as action frames themselves</span>

[2].<span name = "ref2">Class-agnostic detectors are often used as a pre-processor: to produce a bunch of interesting bounding boxes that have a high chance of containing cat, dog, car, etc. Obviously, we need a specialized classifier after a class-agnostic detector to actually know what class each bounding box contains.</span>

[3].<span name = "ref2"> Conditional Variational Auto-Encoder (VAE) model the likelihood of each frame given the attention</span>

