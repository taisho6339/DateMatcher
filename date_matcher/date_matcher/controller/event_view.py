# coding: UTF-8
from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config

from date_matcher.action.event_action import EventAction
from date_matcher.controller.event_base import EventBaseController


class EventViewController(EventBaseController):
    @view_config(route_name="event", renderer="../templates/event.pt")
    def event_view_receive(self):
        if not super(EventViewController, self).validate_hash():
            return HTTPBadRequest()

        action = EventAction(self.event)
        list = action.create_date_ranking_list()
        list = sorted(list, reverse=True)

        list = list[0:10]
        user_list = action.get_user_list()
        res_list = [item[1] + u" ---- " + str(item[0]) + u"人可能/" + str(len(user_list)) + u"人中" for
                    item in list]

        user_add_page = self.request.host_url + "/addDate?hash=" + self.hash_str
        return {"event_name": self.event.name, "event_detail": self.event.detail_comment,
                "user_add_page": user_add_page, "date_ranking": res_list}
