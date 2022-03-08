from .run import *
from .views import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# SQLAlchemy Instances
# app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
# Sign Model
class Sign(db.Model):
    __tablename__ = "Sign"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(256))
    ## ruling-planet = [Relacion con la tabla de planetas]
    ## element = [Relacion con la tabla de elementos]
    ## modality = [Relacion con la tabla de modalida]

    def __init__(self, name, description):
        self.name = name
        self.description = description

db.create_all()

# Schemas
class SignSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')

sign_schema = SignSchema()
signs_schema = SignSchema(many=True)

