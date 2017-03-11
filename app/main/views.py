# -*- coding:utf-8 -*-
import hashlib
from flask import Flask
from flask import request
from ..  import reply
from ..  import receive
from . import main


@main.route('/')
def MsgHandleGet():
    try:
        result=request.args
        data=result.to_dict()
        print("before hello")
        print("data",data)
        if len(data)==0:
            return '<h1>Hello 张哲!</h1>'
        signature=data["signature"]
        timestamp=data["timestamp"]
        nonce=data["nonce"]
        echostr=data["echostr"]
        token="wangzx123"
        list=[token,timestamp,nonce]
        list.sort()
        #sha1=hashlib.sha1()
        #map(sha1.update,list)
        #hashcode=sha1.hexdigest()
        hashcode=''.join(list)
        hashcode=hashlib.sha1(hashcode.encode("utf-8")).hexdigest()
        print("index/GET func:hashcode,signature: ",hashcode,signature)
        if hashcode==signature:
            return echostr
        else:
            return ""
    except Exception as  Argument:
        return Argument

@main.route('/',methods=['POST'])
def MsgHangdlePost():
        try:
            webData = request.get_data()
            print("Handle Post webdata is ", webData)   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = "测试自动回复"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            if isinstance(recMsg, receive.EventMsg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.Event == 'CLICK':
                    if recMsg.Eventkey == 'mpGuide':
                        content = "编写中，尚未完成"
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
            print("暂且不处理")
            return reply.Msg().send()
        except Exception as Argment:
            return Argment

