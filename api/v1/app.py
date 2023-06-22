#!/usr/bin/python3
'''Api Backend of Fawzy staff managemennt'''
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv


app = Flask(__name__)
app.secret_key = getenv("FSM_SECRET_KEY")
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """404 not found"""
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def close_storage(exception=None):
    '''closes any active sqlalchemy session'''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, threaded=True)
