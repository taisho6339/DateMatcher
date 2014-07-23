

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    )


@view_config(route_name='home', renderer='templates/index.pt')
def my_view(request):
    return dict(page="sample")

@view_config(route_name="create_page",renderer="templates/create.pt")
def create(request):
    return {'status':200}

@view_config(route_name="create_action",renderer="json")
def create_action(request):
    return {'status':200}




