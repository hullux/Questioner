from flask import Blueprint

#login blueprint 
login_blueprint = Blueprint('login',__name__,url_prefix='/api/v1/',template_folder='templates')
signup_blueprint = Blueprint('signup',__name__,url_prefix='/api/v1/',template_folder='templates')
home_blueprint = Blueprint('home',__name__,template_folder='templates')
