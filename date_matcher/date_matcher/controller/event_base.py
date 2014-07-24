from date_matcher import DBSession
from date_matcher.models import Event

__author__ = 'taisho6339'


class EventBaseController(object):
    def __init__(self, request):
        self.request = request

    def validate_hash(self):
        self.hash_str = self.request.GET.get('hash', '')
        if self.hash_str == '':
            return False

        self.event = DBSession.query(Event).filter(Event.hash_id == self.hash_str).filter(
            Event.status == Event.STATUS_ACTIVE).first()
        if self.event is None:
            return False

        return True