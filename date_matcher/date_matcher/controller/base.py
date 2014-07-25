# coding: UTF-8
__author__ = 'taisho6339'


class BaseController(object):
    def __init__(self, request):
        self.request = request