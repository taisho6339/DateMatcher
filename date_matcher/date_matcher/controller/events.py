# coding: UTF-8
from pyramid.httpexceptions import HTTPFound

from pyramid.view import view_config


class EventCreateController(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name="create_page", renderer="../templates/create.pt")
    def create_page_receive(self):

        if 'submitted' in self.request.params:
            action_controller = EventActionController(self.request)
            return action_controller.create_action_receive()
        else:
            # if self.request.method == 'GET':
            if self.request.matchdict['is_missed']:
                return {'is_missed': True}
            return {"is_missed": False}


class EventActionController(object):
    def __init__(self, request):
        self.request = request
        self.event_name = None
        self.detail_comment = None
        self.start_at = None
        self.end_at = None


    def validate_params(self):
        self.event_name = self.request.POST.get('event_name')
        self.detail_comment = self.request.POST.get('detail_comment', '')
        self.start_at = self.request.POST.get('start_at')
        self.end_at = self.request.POST.get('end_at')

        if self.event_name == '' or self.detail_comment == '' or self.start_at == '' or self.end_at == '':
            return False

        return True

    def create_action_receive(self):
        if self.validate_params():
            return HTTPFound(location=self.request.host_url)
        return HTTPFound(location=self.request.route_url('create_page', is_missed=True))



