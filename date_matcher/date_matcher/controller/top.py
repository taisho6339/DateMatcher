from date_matcher.controller.base import BaseController

__author__ = 'taisho6339'

from pyramid.view import view_config


class TopViewController(BaseController):
    @view_config(route_name='home', renderer='../templates/index.pt')
    def my_view(self):
        return {}