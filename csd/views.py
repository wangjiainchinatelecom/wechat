from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from wechat import api

# Create your views here.
@api_view(["GET"])
def checkSignature(request):
    params = request.query_params
    nonce = params["nonce"]
    signature = params["signature"]
    timestamp = params["timestamp"]
    echostr = params["echostr"]
    if api.checkSignature(signature,timestamp,nonce):
        result=echostr
    else:
        result='request is not allow!'
    return HttpResponse(result)

@api_view(["GET"])
def getAccessToken(request):
    result = api.get_access_token()
    return HttpResponse(result)