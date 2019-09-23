#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests,sys
print "-----------------------------------------"
print "--------------maikefee.com---------------"
print "-----------------------------------------"
print "--------------单文件检测-------------------"


headers={
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
"DNT": "1",
"X-Forwarded-For": "8.8.8.8",
"Connection": "close",
"content-type": "text/xml",
"Accept-Charset": "ZWNobyAiaSBhbSBiYWNrZG9vciI7",
"Accept-Encoding": "gzip,deflate",
"Upgrade-Insecure-Requests": "1"
}

try:
    response = requests.get(sys.argv[1],headers=headers)  # 输入任意存在php路径
    if(response.text.find("backdoor")>0):
        print "backdoor exist!"
    else:
        print "None!"
    pass
except:
    print("python phpstudy_rec_backdoor_check.py http://xxx.php  (xxx.php为任意存在的php文件)")



