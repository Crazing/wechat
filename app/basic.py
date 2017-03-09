# -*- coding: utf-8 -*-
# filename: basic.py
import urllib
import time
import json

class Basic:
    basic_end=True
    __accessToken=''
    __leftTime=0
    def __init__(self):
        pass
        #self.__accessToken = ''
        #self.__leftTime = 0
    def __real_get_access_token(self):
        appId = "wx3978663e0db66976"
        appSecret = "795241b7ec2e2ecae0f52b6e12aa6553"

        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
               "client_credential&appid=%s&secret=%s" % (appId, appSecret))
        urlResp = urllib.request.urlopen(postUrl)
        urlResp = json.loads(urlResp.read().decode("utf-8"))
        
        Basic.__accessToken = urlResp['access_token']
        Basic.__leftTime = urlResp['expires_in']
    @staticmethod
    def get_access_token():
        if Basic.__leftTime < 10:
            Basic().__real_get_access_token()
        return Basic.__accessToken

    def run(self):
        while(Basic.basic_end):
            if self.__leftTime > 10:
                time.sleep(2)
                self.__leftTime -= 2
            else:
                self.__real_get_access_token()
    @staticmethod
    def flush_access_token():
        Basic().__real_get_access_token()
