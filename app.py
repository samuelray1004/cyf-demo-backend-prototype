import json
from flask import Flask, request
import dao
from db import db

# define db filename
db_filename = "BIGYARD.db"
app = Flask(__name__)

# setup config
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_filename}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# initialize app
db.init_app(app)
with app.app_context():
    db.create_all()

# generalized response formats
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code


@app.route('/properties')
def get_properties():
    return success_response(dao.get_all_properties())

@app.route('/property', methods=['POST'])
def create_property():
    body = json.loads(request.data)
    property = dao.create_property(
        street1 = body.get("street1", "EMPTY"),
        street2 = body.get("street2", "EMPTY"),
        street_number = body.get("streetNumber", "EMPTY"),
        city = body.get("city", "EMPTY"),
        state = body.get("state", "EMPTY"),
        zip_code = body.get("zipCode", "EMPTY"),
        description = body.get("description", "EMPTY")
    )
    return success_response(property, 201)

@app.route('/properties/<int:property_id>')
def get_property(property_id):
    property = dao.get_property_by_id(property_id)
    if property is None:
        return failure_response("Property not found!")
    return success_response(property)

@app.route('/properties/<int:property_id>', methods=['POST'])
def update_property(property_id):
    body = json.loads(request.data)
    property = dao.update_property_by_id(property_id, body)
    if property is None:
        return failure_response("Property not found!")
    return success_response(property)

@app.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    property = dao.delete_property_by_id(property_id)
    if property is None:
        return failure_response("Property not found!")
    return success_response(property)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
