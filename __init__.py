"""
    REST-API aplication for astro issues
    Author: Lautaro Vallejos
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .views import *
# import models, run, views
# import os
# basedir = os.getcwd()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@127.0.0.1:3306/astromysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
db.init_app(app)

from . import views

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

# Resources
#===================================>
# from unicodedata import name
# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# import os

# # App init
# #===================================>
# basedir = os.getcwd()

# app = Flask(__name__)
# # Database Configuration
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@127.0.0.1:3306/astromysql'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# #app.config['SQLALCHEMY_BINDS'] = 'mysql+pymysql://root:admin@127.0.0.1:3306/astromysql'

# # Plugins Instances
# #===================================>
# db = SQLAlchemy(app)
# ma = Marshmallow(app)

# Table Models Database
#===================================>

# Signs model DB
#=========================>
# class Sign(db.Model):
#     __tablename__ = "Sign"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), unique=True)
#     description = db.Column(db.String(256))
#     ## ruling-planet = [Relacion con la tabla de planetas]
#     ## element = [Relacion con la tabla de elementos]
#     ## modality = [Relacion con la tabla de modalida]

#     def __init__(self, name, description):
#         self.name = name
#         self.description = description

# db.create_all()

# class SignSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'name', 'description')

# sign_schema = SignSchema()
# signs_schema = SignSchema(many=True)

# Endpoints
#===================================>

# Index Endpoint
#=========================>
# @app.route('/', methods=['GET'])
# def index():
#     return 'Index its working!!!'

# # Sign endpoint
# #=========================>

# # List Signs
# @app.route('/signs', methods=['GET'])
# def get_signs():
#     ## Gets all objects in the 'Sign' table and returns them.
#     all_signs = Sign.query.all()
#     result = signs_schema.dump(all_signs)

#     return signs_schema.jsonify(result)

# # Create Signs
# @app.route('/sign', methods=['POST'])
# def create_sign():
#     ## Gets the contents of the request and saves them in a variable
#     name = request.json['name']
#     description = request.json['description']

#     ## Create the schema and saves them in a variable
#     new_sign = Sign(name, description)
#     db.session.add(new_sign)
#     db.session.commit()

#     return sign_schema.jsonify(new_sign)

# # Detail Sign
# @app.route('/signs/<id>', methods=['GET'])
# def get_sign(id):
#     #Gets a single sign object
#     sign = Sign.query.get(id)
#     return sign_schema.jsonify(sign)

# # Update Sign
# @app.route('/signs/<id>', methods=['PUT'])
# def update_sign(id):
#     sign = Sign.query.get(id)
#     name = request.json['name']
#     description = request.json['description']
    
#     sign.name = name
#     sign.description = description

#     db.session.commit()
#     return sign_schema.jsonify(sign)

# # Delete Sign
# @app.route('/signs/<id>', methods=['DELETE'])
# def delete_sign(id):
#     sign = Sign.query.get(id)
#     db.session.delete(sign)
#     db.session.commit()

#     return sign_schema.jsonify(sign)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)
#     app.run(debug=True)

# import core.views 