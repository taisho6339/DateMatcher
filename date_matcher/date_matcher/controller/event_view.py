from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config

from date_matcher.models import DBSession, Event


__author__ = 'taisho6339'
# coding: UTF-8

class EventViewController(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name="event", renderer="../templates/event.pt")
    def event_view_receive(self):
        hash_str = self.request.GET.get('hash', '')
        if hash_str == '':
            return HTTPBadRequest()

        event = DBSession.query(Event).filter(Event.hash_id == hash_str).filter(
            Event.status == Event.STATUS_ACTIVE).first()

        if event is None:
            return HTTPBadRequest()

        return {"event_name": event.name}