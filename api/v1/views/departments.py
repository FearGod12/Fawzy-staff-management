#!/usr/bin/pyhton3
'''API routes for department'''

from api.v1.views import app_views
from flask import jsonify, abort, request, session
from models.department import Department
from models import storage


@app_views.route("/department", methods=["GET"], strict_slashes=False)
def get_departments():
    '''returns a list of all departments in storage'''
    departments = storage.all(Department)
    return jsonify([department.to_dict() for department in
                    departments.values()])


@app_views.route("/department/<department_id>", methods=["GET"],
                 strict_slashes=False)
def get_department(department_id):
    '''returns a department with the given id'''
    department = storage.get(Department, department_id)
    if department is None:
        abort(404)
    return jsonify(department.to_dict())


@app_views.route("/department", methods=['POST'], strict_slashes=False)
def create_department():
    """creates a new department in storage"""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    if "name" not in data:
        return jsonify({"error": "Missing data: name"}), 400

    department = Department(**data)
    department.save()
    return jsonify(department.to_dict()), 201


@app_views.route("/department/<department_id>", methods=["PUT"],
                 strict_slashes=False)
def update_department(department_id):
    '''updates the info of an department with the matching id'''
    department = storage.get(Department, department_id)
    if department is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    if "id" in data:
        data.pop("id")

    for key, value in data.items():
        setattr(department, key, value)
    department.save()
    return jsonify(department.to_dict()), 200


@app_views.route("/department/<department_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_department(department_id):
    '''deletes a department from storage'''
    department = storage.get(Department, department_id)
    if department is None:
        abort(404)
    storage.delete(department)
    storage.save()
    return jsonify({}), 200
