# from .models import *
# from .views import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# import os
# from core import app
# basedir = os.getcwd()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@127.0.0.1:3306/astromysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
db.init_app(app)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
