# coding:utf-8
import urllib,urllib2,json,hashlib
from wechat import AccessTokenCache,constants

def post(url,body,header=None):
    req = urllib2.Request(url,body)
    req.add_header("Content-Type","application/x-www-form-urlencoded")
    if header:
        req.add_header(header.get("key"),header.get("value"))
    print req.get_full_url()
    print req.get_data()
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return json.loads(res)


def get(url):
    print url
    res_data = urllib2.urlopen(url)
    res = res_data.read()
    return json.loads(res)


'''
获取token
'''
def get_access_token():
    access_token =AccessTokenCache.AccessTokenCache()
    token = access_token.getCurrentToken()
    return token


'''
接入参数检查
'''
def checkSignature(signature,timestamp,nonce):
    token = constants.tonken
    list = [token,timestamp,nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update,list)
    hashcode = sha1.hexdigest()
    if hashcode == signature:
        return True
    else:
        return False
