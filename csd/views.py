from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

# Create your views here.
@api_view(["GET"])
def checkSignature(request):
    params = request.query_params
    nonce = params["nonce"]
    signature = params["signature"]
    timestamp = params["timestamp"]
    echostr = params["echostr"]
    result={"echostr":echostr}
    return HttpResponse(echostr)