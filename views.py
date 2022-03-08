from .models import Sign, signs_schema, db, sign_schema
from .run import *
from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
# 

# from core.models import Sign, signs_schema, db, sign_schema

# Endpoints
#===================================>
# app = Flask(__name__)
# db = SQLAlchemy(app)
# ma = Marshmallow(app)

#Index Endpoint
#=========================>
@app.route('/', methods=['GET'])
def index():
    return 'Index its working!!!'

# Sign endpoint
#=========================>

# List Signs
@app.route('/signs', methods=['GET'])
def get_signs():
    ## Gets all objects in the 'Sign' table and returns them.
    all_signs = Sign.query.all()
    result = signs_schema.dump(all_signs)

    return signs_schema.jsonify(result)

# Create Signs
@app.route('/sign', methods=['POST'])
def create_sign():
    ## Gets the contents of the request and saves them in a variable
    name = request.json['name']
    description = request.json['description']

    ## Create the schema and saves them in a variable
    new_sign = Sign(name, description)
    db.session.add(new_sign)
    db.session.commit()

    return sign_schema.jsonify(new_sign)

# Detail Sign
@app.route('/signs/<id>', methods=['GET'])
def get_sign(id):
    #Gets a single sign object
    sign = Sign.query.get(id)
    return sign_schema.jsonify(sign)

# Update Sign
@app.route('/signs/<id>', methods=['PUT'])
def update_sign(id):
    sign = Sign.query.get(id)
    name = request.json['name']
    description = request.json['description']
    
    sign.name = name
    sign.description = description

    db.session.commit()
    return sign_schema.jsonify(sign)

# Delete Sign
@app.route('/signs/<id>', methods=['DELETE'])
def delete_sign(id):
    sign = Sign.query.get(id)
    db.session.delete(sign)
    db.session.commit()

    return sign_schema.jsonify(sign)
