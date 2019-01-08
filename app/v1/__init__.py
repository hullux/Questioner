from flask import Blueprint

#login blueprint 
login_blueprint = Blueprint('login',__name__)


from . import views