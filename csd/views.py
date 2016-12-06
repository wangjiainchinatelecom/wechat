from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from wechat import api
import datetime,time,xmltodict

# Create your views here.
def checkSignature(request):
    params = request.query_params
    nonce = params.get("nonce")
    signature = params.get("signature")
    timestamp = params.get("timestamp")
    echostr = params.get("echostr")
    touser = params.get("openid")
    if request.method == "GET":
        if api.checkSignature(signature,timestamp,nonce):
            result=echostr
        else:
            result='request is not allow!'
    if request.method == "POST":
        xml_demo = "<xml><ToUserName><![CDATA[gh_3b94bedd4725]]></ToUserName>" \
                   "<FromUserName><![CDATA[oBkphwBVZDhsqGPrGEl-6jopQlCw]]></FromUserName>" \
                   "<CreateTime>1480988559</CreateTime>"\
                   "<MsgType><![CDATA[text]]></MsgType>"\
                   "<Content><![CDATA[3]]></Content>"\
                   "<MsgId>6360797427111793535</MsgId>"\
                   "</xml>"
        xml = request.body
        create_time = datetime.datetime.now().timetuple()
        result = "<xml><ToUserName><![CDATA[{}]]></ToUserName><FromUserName><![CDATA[{}]]></FromUserName><CreateTime>{}</CreateTime><MsgType><![CDATA[transfer_customer_service]]></MsgType></xml>".format(touser,"wj_851026",time.mktime(create_time))
    return HttpResponse(result)


def getAccessToken(request):
    result = api.get_access_token()
    return HttpResponse(result)


def printLog(request):
    if request.http_method_names =="GET":
        print request.query_params
    elif request.http_method_names =="POST":
        print request.data
    return HttpResponse("success")