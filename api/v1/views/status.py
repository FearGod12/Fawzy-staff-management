#!/usr/bin/python3
"""This is a test route"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'],
                 strict_slashes=False)
def status():
    """A test route to check if API endpoint is running"""
    return jsonify({"status": "OK"}), 200
