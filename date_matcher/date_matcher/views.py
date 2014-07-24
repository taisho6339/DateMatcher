# coding: UTF-8

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    )

import pprint


@view_config(route_name='home', renderer='templates/index.pt')
def my_view(request):

    return {}


# @view_config(route_name="create_page",renderer="templates/create.pt")
# def create_page_receive(request):
#     pprint(request)
#     # is_missed = request.matchdict['is_missed']
#     # if is_missed is None:
#     #     return {"is_missed":False}
#     return {"is_missed":True}

# @view_config(route_name="create_action")
# def create_action_receive(request):
#     return HTTPFound(location = request.route_url('create_page', pagename=request.matchdict['pagename']))
