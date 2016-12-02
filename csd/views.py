from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from wechat import api
import datetime,time

# Create your views here.
@api_view(["GET","POST"])
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
        create_time = datetime.datetime.now().timetuple()
        result = "<xml><ToUserName><![CDATA[{}]]></ToUserName><FromUserName><![CDATA[{}]]></FromUserName><CreateTime>{}</CreateTime><MsgType><![CDATA[transfer_customer_service]]></MsgType></xml>".format(touser,"wj_851026",time.mktime(create_time))
    return HttpResponse(result)

@api_view(["GET"])
def getAccessToken(request):
    result = api.get_access_token()
    return HttpResponse(result)

@api_view(["GET","POST"])
def printLog(request):
    if request.http_method_names =="GET":
        print request.query_params
    elif request.http_method_names =="POST":
        print request.data
    return HttpResponse("success")