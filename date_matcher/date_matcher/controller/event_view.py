# coding: UTF-8
from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config

from date_matcher.controller.event_base import EventBaseController


class EventViewController(EventBaseController):
    @view_config(route_name="event", renderer="../templates/event.pt")
    def event_view_receive(self):
        if not super(EventViewController, self).validate_hash():
            return HTTPBadRequest()
        user_add_page = self.request.host_url + "/addDate?hash=" + self.hash_str
        return {"event_name": self.event.name, "event_detail": self.event.detail_comment,
                "user_add_page": user_add_page}
