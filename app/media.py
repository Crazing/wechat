# -*- coding: utf-8 -*-
# filename: media.py
import urllib
#import poster.encode
import json
import requests
#from poster.streaminghttp import register_openers

class Media(object):
    def __init__(self):
        pass
 #       register_openers()
    #上传图片
    def upload(self, accessToken, filePath, mediaType,timeType=True):
        openFile = open(filePath, "rb")
        param = {'media': openFile}
        #postData, postHeaders = poster.encode.multipart_encode(param)
        if timeType:
            postUrl="https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=%s&type=%s" % (accessToken, mediaType)
        else:
            postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
        #request = urllib.request.Request(postUrl, postData, postHeaders)
        #urlResp = urllib.request.urlopen(request)
        #print(urlResp.read())
        r=requests.post(postUrl,files=param)
        if r.status_code==200:
            dict=r.json()
            print(dict['media_id'])
        else:
            print(r.text)

    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        urlResp = urllib.request.urlopen(postUrl)

        headers = urlResp.info().__dict__['headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print(jsonDict)
        else:
            buffer = urlResp.read()   #素材的二进制
            mediaFile = file("test_media.jpg", "wb")
            mediaFile.write(buffer)
            print("get successful")

    def delete(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/del_material?access_token=%s" % accessToken
        postData = "{ \"media_id\": \"%s\" }" % mediaId
        urlResp = urllib.request.urlopen(postUrl, postData)
        print(urlResp.read())
