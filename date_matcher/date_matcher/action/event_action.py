# coding: UTF-8
import transaction

from date_matcher.utilities.util import make_hash


__author__ = 'taisho6339'

from ..models import (
    DBSession,
    Event
)


class EventActionModel(object):
    def __init__(self, params):
        self.params = params

    def add_to_table(self):
        hash_str = make_hash(30)
        with transaction.manager:
            event = Event(self.params['event_name'], hash_str, self.params['detail_comment'], self.params['start_at'],
                          self.params['end_at'])
            DBSession.add(event)
