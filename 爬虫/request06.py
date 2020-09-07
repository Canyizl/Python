import requests
import json
#批量获取不同企业的id
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
id_list = [] #存储企业的id
all_data_list = [] #存储所有企业的详情数据
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400'
}
#参数的封装
for page in range(1,6):
    page = str(page)
    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
    }
    json_ids = requests.post(url=url,headers=headers,data=data).json()
    for dic in json_ids['list']:
        id_list.append(dic['ID'])

#获取企业详细数据
post_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for id in id_list:
    data = {
        'id' : id
    }
    detail_json = requests.post(url=post_url,headers=headers,data=data).json()
    #print(detail_json,'-------ending------')
    all_data_list.append(detail_json)
#持久化存储all_data_list
fp=open('./alllData.json','w',encoding='utf-8')
json.dump(all_data_list,fp=fp,ensure_ascii=False)
print('over!!!')