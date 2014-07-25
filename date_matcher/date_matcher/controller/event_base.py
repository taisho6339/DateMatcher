from date_matcher import DBSession
from date_matcher.models import Event

__author__ = 'taisho6339'


class EventBaseController(object):
    def __init__(self, request):
        self.request = request
        self.hash_str = self.request.GET.get('hash', '')
        self.event = DBSession.query(Event).filter(Event.hash_id == self.hash_str).filter(
            Event.status == Event.STATUS_ACTIVE).first()

    def validate_hash(self):
        if self.hash_str == '':
            return False

        if self.event is None:
            return False

        return True