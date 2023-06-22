#!/usr/bin/pyhton3
'''API routes for staff'''

from api.v1.views import app_views
from flask import jsonify, abort, request, session
from models.staff import Staff
from models import storage


@app_views.route("/staff", methods=["GET"], strict_slashes=False)
def get_staffs():
    '''returns a list of all staffs in storage'''
    staffs = storage.all(Staff)
    return jsonify([staff.to_dict() for staff in staffs.values()])


@app_views.route("/staff/<staff_id>", methods=["GET"], strict_slashes=False)
def get_staff(staff_id):
    '''returns an staff with the given id'''
    staff = storage.get(Staff, staff_id)
    if staff is None:
        abort(404)
    return jsonify(staff.to_dict())


@app_views.route("/staff", methods=['POST'], strict_slashes=False)
def create_staff():
    """creates a new staff in storage"""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    attrs = ["surname", "firstname", "lastname", "email", "phone", "address",
             "age", "passport", "date_of_birth", "date_engaged",
             "next_of_kin_surname", "next_of_kin_firstname",
             "next_of_kin_address", "next_of_kin_id", "department_id"]
    for attr in attrs:
        if attr not in data:
            return jsonify({"error": "Missing data:" + attr}), 400
    to_check = {"email": data.get("email"), "phone": data.get("phone")}
    for key, value in to_check.items():
        staff_exists = storage.match(Staff, attr={key: value})
        if staff_exists:
            return jsonify({"error": "{} already exists".format(key)}), 400
    staff = Staff(**data)
    staff.save()
    return jsonify(staff.to_dict()), 201


@app_views.route("/staff/<staff_id>", methods=["PUT"], strict_slashes=False)
def update_staff(staff_id):
    '''updates the info of an staff with the matching id'''
    staff = storage.get(Staff, staff_id)
    if staff is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    if "id" in data:
        data.pop("id")

    for key, value in data.items():
        setattr(staff, key, value)
    staff.save()
    return jsonify(staff.to_dict()), 200


@app_views.route("/staff/<staff_id>", methods=["DELETE"], strict_slashes=False)
def delete_staff(staff_id):
    '''deletes a staff from storage'''
    staff = storage.get(Staff, staff_id)
    if staff is None:
        abort(404)
    storage.delete(staff)
    storage.save()
    return jsonify({}), 200
