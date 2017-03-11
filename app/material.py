# -*- coding: utf-8 -*-
# filename: material.py
import urllib
import json
import requests

class Material(object):
    def __init__(self):
        pass
    #上传图文图片
    def upload(self, accessToken, filePath):
        openFile = open(filePath, "rb")
        param = {'media': openFile}
        postUrl="https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=%s"%accessToken
        r=requests.post(postUrl,files=param)
        if r.status_code==200:
            dict=r.json()
            #print(dict['url'])
            print(r.text)
        else:
            print(r.text)
    def add_news(self, accessToken, news):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(postUrl, news)
        print(urlResp.read())
