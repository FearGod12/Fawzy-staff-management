#!/usr/bin/pyhton3
'''API routes for admin'''

from api.v1.views import app_views
from flask import jsonify, abort, request, session
from models.admin import Admin
from models import storage


@app_views.route("/admin", methods=["GET"], strict_slashes=False)
def get_admins():
    '''returns a list of all admins in storage'''
    admins = storage.all(Admin)
    return jsonify([admin.to_dict() for admin in admins.values()])


@app_views.route("/admin/<admin_id>", methods=["GET"], strict_slashes=False)
def get_admin(admin_id):
    '''returns an admin with the given id'''
    admin = storage.get(Admin, admin_id)
    if admin is None:
        abort(404)
    return jsonify(admin.to_dict())


@app_views.route("/admin", methods=['POST'], strict_slashes=False)
def create_admin():
    """creates a new admin in storage"""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    attrs = ["surname", "firstname", "lastname", "email", "phone", "position",
             "password"]
    for attr in attrs:
        if attr not in data:
            return jsonify({"error": "Missing data:" + attr}), 400

    to_check = {"email": data.get("email"), "phone": data.get("phone")}
    for key, value in to_check.items():
        admin_exists = storage.match(Admin, attr={key: value})
        if admin_exists:
            return jsonify({"error": "{} already exists".format(key)}), 400

    admin = Admin(**data)
    admin.save()
    return jsonify(admin.to_dict()), 201


@app_views.route("/admin/<admin_id>", methods=["PUT"], strict_slashes=False)
def update_admin(admin_id):
    '''updates the info of an admin with the matching id'''
    admin = storage.get(Admin, admin_id)
    if admin is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    if "id" in data:
        data.pop("id")

    for key, value in data.items():
        setattr(admin, key, value)
    admin.save()
    return jsonify(admin.to_dict()), 200


@app_views.route("/admin/<admin_id>", methods=["DELETE"], strict_slashes=False)
def delete_admin(admin_id):
    '''deletes an admin from storage'''
    admin = storage.get(Admin, admin_id)
    if admin is None:
        abort(404)
    storage.delete(admin)
    storage.save()
    return jsonify({}), 200


@app_views.route("/login", methods=["POST"], strict_slashes=False)
def admin_login():
    '''validates user login and creates a session if exists'''
    from hashlib import md5
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    email = data.get["email", None]
    password = data.get["password", None]
    if password and email is not None:
        admin = storage.match(Admin, email)
        if admin:
            if admin.password == md5(password.encode()).hexdigest():
                session["id"] = admin.id
                session["email"] = admin.email
                return jsonify(admin.to_dict())
    abort(404)


@app_views.route("/logout", methods=["POST"], strict_slashes=False)
def admin_logout():
    '''logs out the current admin session'''
    session.clear()
    return jsonify({}), 200


@app_views.route("/@me", methods=["GET"], strict_slashes=False)
def admin_info():
    """returns info about the current logged in admin"""
    admin = storage.get(Admin, session.get("id", None))
    if admin is None:
        abort(404)
    return jsonify(admin.to_dict())
