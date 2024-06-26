from ast import Not
from requests import request
import requests

class Common(object):

    def __init__(self, url_root):
        self.url_root = url_root

    def get(self, uri, prams=''):
        url = self.url_root + uri + prams
        res = requests.get(url)
        return res

    def post(self, uri, prams=''):
        url = self.url_root + uri
        if (len(prams)) > 0:
            res = requests.post(url, data=prams)
        else:
            res = requests.post(url)
        return res

    def put(self, uri, prams=None):
        '''
        RESTful风格
        封装自己的方法，uri是访问路的，params是put请求需要传递的参数，如果没有参数这里为空:
        :param uri: 访问路由
        :param params: 传递参数，String类型，默认为None
        :return: 此次访问的response
        '''
        url = self.url_root + uri
        if prams is not None:
            res = requests.put(url, data=prams)
        else:
            res = requests.put(url)
        return res
