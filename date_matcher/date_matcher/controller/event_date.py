# coding: UTF-8
from pyramid.httpexceptions import HTTPBadRequest

from pyramid.view import view_config

from date_matcher.controller.event_base import EventBaseController


class EventDateAddController(EventBaseController):
    def __init__(self, request):
        self.request = request

    @view_config(route_name="date_add", renderer="../templates/date_add.pt")
    def add_date_receive(self):
        if not super(EventDateAddController, self).validate_hash():
            return HTTPBadRequest()
        return {"event_hash": self.hash_str, "event_name": self.event.name}

