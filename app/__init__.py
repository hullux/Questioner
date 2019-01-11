import os

# from flask_api import FlaskAPI 
from flask_sqlalchemy import SQLAlchemy

from flask import Flask

#imporing the configuration dictionary object from the instance module 
from instance.config import app_config

from .api.v1.meetups import meetups_blueprint
from .api.v1.questions import questions_blueprint
from .api.v1.users import login_blueprint,signup_blueprint, home_blueprint


#initializinng sqlalchemy 
# db = SQLAlchemy()

def create_app(config_name):
    '''initializing/creating the flask app(object)'''
    app = Flask(__name__,instance_relative_config=True,template_folder='templates',static_folder='static',static_url_path='')
    app.config.from_object(app_config[config_name])#using development app configurations
    app.config.from_pyfile("config.py")

    #registering the blueprints here 
    app.register_blueprint(home_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(signup_blueprint)
    app.register_blueprint(questions_blueprint)
    app.register_blueprint(meetups_blueprint)
      
    return app