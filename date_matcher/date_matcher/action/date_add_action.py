# coding: UTF-8
from datetime import datetime, timedelta

from date_matcher.models import Date


__author__ = 'taisho6339'

from ..models import (
    DBSession,
    Event,
    User)


class EventDateAddAction(object):
    def __init__(self, params):
        self.params = params
        self.event = self.get_event_by_hash()
        self.dates = [date.get("date") for date in self.params.get("dates")]

    def get_event_by_hash(self):
        hash = self.params.get("hash")
        event = DBSession.query(Event).filter(Event.hash_id == hash).filter(
            Event.status == Event.STATUS_ACTIVE).first()
        return event


    def validate_term(self):
        date_start = datetime.strptime(self.event.start_at, '%Y/%m/%d')
        date_end = datetime.strptime(self.event.end_at, '%Y/%m/%d')

        for date in self.dates:
            date_stmp = ''
            try:
                date_stmp = datetime.strptime(date, '%Y/%m/%d')
            except ValueError:
                return False
            if not (date_start <= date_stmp and date_stmp <= date_end):
                return False
        return True

    def create_date_list(self):
        choose_method = int(self.params.get('choose_method'))
        dates = self.params.get('dates')
        date_start = datetime.strptime(self.event.start_at, '%Y/%m/%d')
        date_end = datetime.strptime(self.event.end_at, '%Y/%m/%d')

        time = date_start
        date_list = []
        while time <= date_end:
            status = int(choose_method)
            if time.strftime('%Y/%m/%d') in self.dates:
                status = choose_method ^ Date.STATUS_ACTIVE
            date_list.append(Date(time.strftime('%Y/%m/%d'), self.user._id, self.event._id, status))
            time = time + timedelta(days=1)
        return date_list


    def add_to_date_table(self):

        if not self.validate_term():
            return False

        self.user = DBSession.query(User).filter(User.event_id == self.event._id).filter(
            User.name == self.params.get("user_name")
        ).first()

        if self.user is None:
            user = User(self.params.get("user_name"), self.event._id)
            DBSession.add(user)
            self.user = DBSession.query(User).filter(User.event_id == self.event._id).filter(
                User.name == self.params.get("user_name")
            ).first()

        else:
            return False

        date_list = self.create_date_list()
        for date in date_list:
            DBSession.add(date)

        return True
