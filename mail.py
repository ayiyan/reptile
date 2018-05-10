#!/usr/bin/python
# coding:utf-8
import requests, re
url = 'http://192.168.1.1'
page = requests.get(url)
val = re.findall(('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'), page.text)
list=[]
for i in val:
    if re.findall('^192|^255|^118.118|^219.149.6|$!=1',i):
        pass
    else:
        list.append(i)
print(list)
