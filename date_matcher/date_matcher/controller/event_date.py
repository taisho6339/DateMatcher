# coding: UTF-8

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config

from date_matcher.action.date_add_action import EventDateAddAction

from date_matcher.controller.base import BaseController
from date_matcher.controller.event_base import EventBaseController


class EventDateAddViewController(EventBaseController):
    @view_config(route_name="date_add", renderer="../templates/date_add.pt")
    def add_date_receive(self):
        if not super(EventDateAddViewController, self).validate_hash():
            return HTTPBadRequest()
        return {"event_hash": self.hash_str, "event_name": self.event.name, "event_start": self.event.start_at,
                "event_end": self.event.end_at}


class EventDateAddActionController(BaseController):
    def validate_params(self):
        params = self.request.json_body
        hash = params.get('hash', "")
        user_name = params.get('user_name', "")
        choose_method = params.get('choose_method', "")
        dates = params.get('dates', None)
        if hash == "" or user_name == "" or choose_method == "" or len(dates) == 0:
            return False
        return True


    @view_config(route_name="date_add_action", request_method="POST", renderer="json")
    def add_date_action_receive(self):
        if not self.validate_params():
            return {"status": 400, "err_message": "正しく入力してください。"}

        action = EventDateAddAction(self.request.json_body)
        is_success = action.add_to_date_table()
        if is_success:
            redirect_url = self.request.host_url + "/event?hash=" + self.request.json_body.get("hash", "");
            return {"status": 200, "redirect_url": redirect_url}
        else:
            return {"status": 400, "err_message": "正しく入力してください。"}