# coding: UTF-8
from datetime import datetime

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
            return {"is_missed": False, "event_name": "", "detail_comment": ""}


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

        date_start = datetime.strptime(self.start_at, '%Y/%m/%d')
        date_end = datetime.strptime(self.end_at, '%Y/%m/%d')

        # 必須項目は足りているか
        if self.event_name == '' or self.start_at == '' or self.end_at == '':
            return False

        # 開始と終了は適正か
        if date_end <= date_start:
            return False

        return True


    @view_config(renderer="../templates/create.pt")
    def create_action_receive(self):
        if self.validate_params():
            return HTTPFound(location=self.request.host_url)
        return {"is_missed": True, "event_name": self.event_name, "detail_comment": self.detail_comment}



