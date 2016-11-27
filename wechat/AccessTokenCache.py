#coding : utf-8
import datetime
import urllib,urllib2
import constants
import json


class AccessTokenCache(object):
    _access_token =''
    _expires_in = 0
    _start_time={}
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(AccessTokenCache, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def getCurrentToken(self):
        if self.is_valid():
            return self._access_token
        else:
            token_obj = get_access_token()
            self._access_token=token_obj.get("access_token")
            self._expires_in = token_obj.get("expires_in")
            self._start_time=datetime.datetime.now()
            return self._access_token

    def is_valid(self):
        if self._expires_in :
            return self._start_time+datetime.timedelta(seconds=self._expires_in)>datetime.datetime.now()
        else:
            return False


def get_access_token():
    appid=constants.APPID
    secret=constants.APPSECRET
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(appid,secret)
    req = urllib2.Request(url)
    print req
    res_data = urllib2.urlopen(req)
    res=res_data.read()
    return json.loads(res)