from flask import Blueprint

questions_blueprint = Blueprint('questions',__name__,template_folder='templates',static_folder='static',url_prefix='/api/v1/')