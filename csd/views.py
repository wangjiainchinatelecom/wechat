# coding:utf-8
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from wechat import api
import datetime,time,xmltodict,json
from common import views as common_api
from common import utils

# Create your views here.
def checkSignature(request):
    if request.method == "GET":
        params = request.query_params
        nonce = params.get("nonce")
        signature = params.get("signature")
        timestamp = params.get("timestamp")
        echostr = params.get("echostr")
        if api.checkSignature(signature,timestamp,nonce):
            result=echostr
        else:
            result='request is not allow!'
    if request.method == "POST":
        xml = request.body
        msg_json = xmltodict.parse(xml).get("xml")
        FromUserName = msg_json.get("FromUserName")
        ToUserName = msg_json.get("ToUserName")
        MsgType = "text"
        Content = u"收到消息{}".format(msg_json.get("Content"))
        result = returnXmlMsg(FromUserName,ToUserName,MsgType,Content)
    return HttpResponse(result)


#获取token
def getAccessToken(request):
    result = utils.get_access_token()
    return HttpResponse(result)


#查询会话列表
def get_session_list(request):
    result = json.dumps(common_api.getwaitcase())
    return HttpResponse(result)


def send_message(request):
    data = json.loads(request.body)
    touser = data.get("touser")
    msgtype = data.get("msgtype")
    content = data.get("content")
    result = json.dumps(common_api.send_msg(touser,msgtype,content))
    return HttpResponse(result)


def returnXmlMsg(FromUserName,ToUserName,MsgType,Content,createTime=None):
    returnXml = ''
    if not createTime:
        createTime = time.mktime(datetime.datetime.now().timetuple())
    if MsgType == 'text':
        returnXml = '<xml>\
                        <FromUserName>{}</FromUserName>\
                        <ToUserName>{}</ToUserName>\
                        <CreateTime>{}</CreateTime>\
                        <MsgType>text</MsgType>\
                        <Content>{}</Content>\
                    </xml>'.format(FromUserName,ToUserName,createTime,Content)
    return returnXml
