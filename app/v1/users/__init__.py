from flask import Blueprint

simple_page = Blueprint('simple_page',__name__,url_prefix='/api/v1/')
home_blueprint = Blueprint('home',__name__,url_prefix='/api/v1/')
login_blueprint = Blueprint('login',__name__,url_prefix='/api/v1/')
signup_blueprint = Blueprint('signup',__name__,url_prefix='/api/v1/')