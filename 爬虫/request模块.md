## request模块

#### 参考教程：

​		2020年Python爬虫全套实战课程

​		 使用软件：pycharm



#### 如何使用：（requests模块的编码流程）

			- 指定url	
			- 发起请求
			- 获取响应数据
			- 持久化存储



#### 环境安装：

```
pip install requests
```



#### 实战编码:

 - 需求：爬取搜狗首页的页面数据



#### 实战巩固

 - 需求：爬取搜狗指定词条对应的搜索结果页面（简易网页采集器）
   	- UA检测
      	- UA伪装

- 需求：破解百度翻译
  - post请求（携带了参数）
  - 响应数据是一组json数据
  
- 需求：爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据

  - 动态加载数据（笨方式：直接对url发请求；便捷方法：抓包工具）

  - 首页中对应的企业信息数据通过Ajax动态请求到

  - 通过对详情页url的观察发现:

    - url的域名都一样，只有携带参数id不一样

      http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList

    - id值可以通过首页对应的AJAX中的json串获取

    - 域名和id值拼接出完整的企业对应详情页的url

  - 详情页的企业详情数据也是动态加载出来的

    - http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
    - 观察后发现：
      - 所有的post请求的url是一样的，只有id不一样。
      - 如果可以批量获取多家的企业的id后，就可以将id和url形成一个完整的详情页对应数据的ajax请求的url

    

##### //data和param的区别

params的时候之间接把参数加到url后面，只在get请求时使用

data用于post请求时