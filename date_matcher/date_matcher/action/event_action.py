# coding: UTF-8
from datetime import datetime, timedelta

from date_matcher import DBSession
from date_matcher.models import Date, User


__author__ = 'taisho6339'


class EventAction(object):
    def __init__(self, event):
        self.event = event

    def get_user_list(self):
        return DBSession.query(User).filter(User.event_id == self.event._id).all()


    def create_date_ranking_list(self):

        event_start = datetime.strptime(self.event.start_at, '%Y/%m/%d')
        event_end = datetime.strptime(self.event.end_at, '%Y/%m/%d')

        ranking_list = []
        time = event_start
        while time <= event_end:
            score = 0
            dates = DBSession.query(Date).filter(Date.event_id == self.event._id).filter(
                Date.date == time.strftime('%Y/%m/%d')).all()
            for date in dates:
                score += date.status
            ranking_list.append((score, time.strftime('%Y/%m/%d')))
            time += timedelta(days=1)

        return ranking_list
