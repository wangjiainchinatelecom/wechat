# coding:utf-8
import hashlib
import constants
import urllib,urllib2
import AccessTokenCache

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


'''
获取token
'''
def get_access_token():
    access_token =AccessTokenCache.AccessTokenCache()
    token = access_token.getCurrentToken()
    return token
