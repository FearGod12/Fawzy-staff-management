#!/usr/bin/python3
'''Api blueprint for fawzy staff management'''
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# import all relevant routes defined within api.v1.views
from api.v1.views.admins import *  # noqa
from api.v1.views.status import *  # noqa
from api.v1.views.staffs import *  # noqa
from api.v1.views.departments import *  # noqa
