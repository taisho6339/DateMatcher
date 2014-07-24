__author__ = 'taisho6339'

from pyramid.view import view_config


class TopViewController(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='../templates/index.pt')
    def my_view(self):
        return {}